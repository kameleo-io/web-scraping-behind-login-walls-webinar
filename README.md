# Web Scraping Behind Login Wall Webinar
On 2024-07-03 we created a webinar with Evgeny Fomenko from [iProxy](https://iproxy.online?utm_source=kameleo_github). During the webinar [Kameleo](https://kameleo.io?utm_source=GitHub)'s CEO and Co-founder, Tamás Deák showcased how Kameleo can be used to scrape behind login walls, and bypass any anti-bot system. Here we share the code that was used during the demo.

## Step-by-step guide
To run the examples you will need to do some preparation. If you are stuck, we can [help you](https://help.kameleo.io/hc/en-us/requests/new).

### 1. Start Kameleo.CLI
To run the following code examples, you need to run Kameleo.CLI on your machine.

### 2. Change proxy credentials
During the demo we used iProxy's product as a proxy. The following values should be changed, so you can access and control your own proxy
- proxy_host
- proxy_port
- proxy_username
- proxy_password
- ip_renewal_url

### 3. Prepare some virtual browser profiles
To easily start scraping behind login wall, create new Kameleo profiles, and log in to an existing website with them. Keep them in Kameleo's workspace, and add `ip:profile_name` key:values to the profile store sqlite file. This way you will be able to load back the profiles later. [Contact support](https://help.kameleo.io/hc/en-us/requests/new) if you have any issues.

### 4. Operation
Start `app.py` to run the example.
1. Code will request a new IP
2. Code will determine the IP address
3. Code will search for any virtual browser profile that was previously used with the given IP
4. Code will launch the found profile, and drive it with playwright

If IP from the pool was not used before, code will create a new virtual browser profile for that.

## Support
We really want you to succeed with this project. So please [contact our support team](https://help.kameleo.io/hc/en-us/requests/new) if you have any issues. We will help you with the examples, and we will also provide you with prepared .kameleo profiles