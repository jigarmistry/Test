import requests
from bs4 import BeautifulSoup

class SessionGoogle:
    def __init__(self, url_login, url_auth, login, pwd):
        self.ses = requests.session()
        login_html = self.ses.get(url_login)
        soup_login = BeautifulSoup(login_html.content,"xml").find('form').find_all('input')
        my_dict = {}
        for u in soup_login:
            if u.has_attr('value'):
                my_dict[u['name']] = u['value']
        # override the inputs without login and pwd:
        my_dict['Email'] = login
        my_dict['Passwd'] = pwd
        self.ses.post(url_auth, data=my_dict)

    def get(self, URL):
        return self.ses.get(URL,stream=True,timeout=None).text

url_login = "https://accounts.google.com/ServiceLogin?service=finance"
url_auth = "https://accounts.google.com/ServiceLoginAuth"
session = SessionGoogle(url_login, url_auth, "parasdoshipu@gmail.com", "algoforme12")

session.get("https://www.google.com/finance/portfolio?action=view&pid=3&authuser=2&ei=sAg8WLn-MYviugSQ_4WQBA&output=csv")