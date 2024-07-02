import requests


def renew_ip(ip_renewal_url='https://i.fxdx.in/api-rt/changeip/X4rakjGvxI/xYYWG6SKKEESN'):
    try:
        response = requests.get(ip_renewal_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4XX, 5XX)
        data = response.json()
        return data
    except requests.RequestException as error:
        print(f"An error occurred: {error}")
        return None


def get_ip_via_proxy(host, port, username, password):
    # Construct the proxy URL with authentication
    proxy_url = f"http://{username}:{password}@{host}:{port}"

    # Set up the proxies dictionary for the requests call
    proxies = {
        "http": proxy_url,
        "https": proxy_url,
    }

    try:
        # Use requests to fetch the IP address via the proxy
        response = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4XX, 5XX)

        # Extract the IP address from the response
        ip_address = response.json()['origin']
        return ip_address
    except requests.RequestException as error:
        print(f"Error fetching IP via proxy: {error}")
        return None
