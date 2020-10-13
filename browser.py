import cookie_browser3
import argparse
import json
import os
import tempfile


def main():
    # login_data = cookie_browser3.Chrome().load_login_data()
    arg = argparse.ArgumentParser()
    arg.add_argument('action', type=str)
    arg.add_argument('browser', type=str)
    arg.add_argument('domain', type=str)
    args = arg.parse_args()

    action = args.action
    browser = args.browser
    domain = args.domain
    if action == "login_data":
        if browser == "chrome":
            login_data = cookie_browser3.Chrome().load_login_data()
            login_data_json = json.dumps(login_data)
            print(login_data_json)
    elif action == "cookies":
        cookies = []
        if browser == "opera":
            cookies = cookie_browser3.opera(domain_name=domain)
        elif browser == "chrome":
            cookies = cookie_browser3.chrome(domain_name=domain)
        elif browser == "firefox":
            cookies = cookie_browser3.firefox(domain_name=domain)
        cookies_list = []

        for cookie in cookies:
            cookie_dict = {
                'name': cookie.name,
                'value': cookie.value,
                'domain': cookie.domain,
                'path': cookie.path,
                'secure': cookie.secure,
                'expires': cookie.expires
            }
            cookies_list.append(cookie_dict)

        cookies_json = json.dumps(cookies_list)
        print(cookies_json)


if __name__ == '__main__':
    main()
