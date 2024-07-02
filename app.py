from kameleo.local_api_client import KameleoLocalApiClient
from kameleo.local_api_client.builder_for_create_profile import BuilderForCreateProfile
from kameleo.local_api_client.models import Server
from playwright.sync_api import sync_playwright
from proxy_management import *
from profile_store import *
import time

# Proxy details
proxy_host = 'x240.fxdx.in'
proxy_port = 14520
proxy_username = 'kameleo'
proxy_password = 'demo'

# Initialize Kameleo Local Api Client that communicates with Kameleo on localhost:5050
kameleo_port = 5050
client = KameleoLocalApiClient(
    endpoint=f'http://localhost:{kameleo_port}',
    retry_total=0
)

# Init profile store (an sqlite db)
init_profile_store()

# Renew IP through proxy management url
renew_ip()

# Check what ip we have right now
ip = get_ip_via_proxy(proxy_host, proxy_port, proxy_username, proxy_password)

# Lookup which profile was used before with this IP
profile_name = lookup_profile_by_ip(ip)

profile = None
if profile_name is not None:
    profiles = client.list_profiles()
    for p in profiles:
        if p.name == profile_name:
            profile = p
            break
else:
    base_profiles = client.search_base_profiles(
        device_type='desktop',
        browser_product='chrome'
    )

    name_of_new_account = 'new_account@mail.com'

    # Create a new profile with recommended settings
    # Choose one of the Base Profiles
    create_profile_request = BuilderForCreateProfile \
        .for_base_profile(base_profiles[0].id) \
        .set_name(name_of_new_account) \
        .set_start_page('about:newtab') \
        .set_proxy('socks5', Server(host=proxy_host, port=proxy_port, id=proxy_username, secret=proxy_password)) \
        .set_recommended_defaults() \
        .build()
    profile = client.create_profile(body=create_profile_request)
    client.start_profile(profile.id)

    # Login manually to new account
    time.sleep(5)

    client.stop_profile(profile.id)
    insert_profile_by_ip(ip, name_of_new_account)

client.start_profile(profile.id)

# Start the Kameleo profile and connect with Playwright through CDP
browser_ws_endpoint = f'ws://localhost:{kameleo_port}/playwright/{profile.id}'
with sync_playwright() as playwright:
    browser = playwright.chromium.connect_over_cdp(endpoint_url=browser_ws_endpoint)
    context = browser.contexts[0]
    page = context.new_page()

    # Use any Playwright command to drive the browser
    # and enjoy full protection from bot detection products
    page.goto('https://www.facebook.com/marketplace/100232032143091/propertyrentals/?exact=false')
    for i in range(5):
        page.mouse.wheel(0, 15000)
        time.sleep(2)

# Stop the browser by stopping the Kameleo profile
client.stop_profile(profile.id)
