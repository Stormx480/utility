from selenium import webdriver
from robobrowser import RoboBrowser
import requests
import time


def start_driver(proxy=False):
    for i in range(5):
        try:
            if proxy:
                proxy = proxy.split(":")
                server_adress = proxy[0]
                port_number = int(proxy[1])
                profile = webdriver.FirefoxProfile()
                profile.set_preference("network.proxy.type", 1)
                profile.set_preference("network.proxy.http", server_adress)
                profile.set_preference("network.proxy.http_port", port_number)
                profile.set_preference('network.proxy.ssl_port', port_number)
                profile.set_preference('network.proxy.ssl', server_adress)
                profile.update_preferences()
                driver = webdriver.Firefox(firefox_profile=profile)
            else:
                driver = webdriver.Firefox()
            break
        except Exception as ex:
            print(ex)
            print("Не удалось открыть selenium firefox в api.py/AllUsersControll.start_driver()")
            continue

    return driver


class vk_session:

    def __init__(self, root_path, proxy="", cookies=""):
        self.is_signed = False
        self.proxy = proxy
        self.root_path = root_path
        session = requests.session()
        if proxy:
            session.proxies.update({'http': 'http://' + proxy, 'ssl': proxy ,'https': 'https://' + proxy})
        headers = {
            "ACCEPT": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "ACCEPT_ENCODING": "gzip, deflate, sdch",
            "ACCEPT_LANGUAGE": "ru-RU,ru;",
            "CONNECTION": "keep-alive",
            "REFERER": root_path,
            "UPGRADE_INSECURE_REQUESTS": "1",
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        }
        session.headers = headers
        if cookies:
            session.cookies = cookies
        self.browser = RoboBrowser(session=session, timeout=4, history=False)
        self.browser.parser = 'lxml'

    def connect(self):

        self.browser.open(self.root_path)
        print("connected")

    def sign_in(self, username, password, captcha):
        try:
            form = self.browser.get_forms()[0]

            form["email"] = username
            form["pass"] = password
            if captcha:
                pass
                #form["captcha_key"] = vk_captcha.decode(page=self.browser.parsed, root_path=self.root_path)
            self.browser.submit_form(form)
        except:
            print(username)
            raise

    def get_forms(self, path):

        self.browser.open(path)

        form = self.browser.get_form()

        print(form)

        links = self.browser.find("div", {'id':'profile_message_send'})

        print(type(links))
        print(links)


if __name__ == '__main__':
    #start_driver()
    username = ''
    password = ''

    session = vk_session(root_path="http://m.vk.com", proxy=False, cookies=False)
    session.connect()

    session.sign_in(username, password, False)
    print('Вошли в аккаунт')

    session.get_forms('')
