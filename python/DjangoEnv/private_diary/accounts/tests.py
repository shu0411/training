from django.test import LiveServerTestCase
from django.urls import reverse_lazy
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class TestLogin(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        #cls.selenium = WebDriver(executable_path='C:/Users/user/Training/chromedriver-win64/chromedriver.exe')
        service = Service(executable_path='C:/Users/user/Training/chromedriver-win64/chromedriver.exe')
        cls.selenium = WebDriver(service=service)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
    
    #ログインのテスト
    def test_login(self):
        #ログインページを開く
        self.selenium.get('http://localhost:8000' + str(reverse_lazy('account_login')))
        
        #ユーザー名とパスワードを入力してログイン
        #username_input = self.selenium.find_element_by_name("login")
        #username_input.send_keys('testuser')
        #password_input = self.selenium.find_element_by_name("password")
        #password_input.send_keys('0216shu0211')
        #self.selenium.find_element_by_class_name('btn').click()
        username_input = self.selenium.find_element(By.NAME, 'login')
        username_input.send_keys('testuser')
        password_input = self.selenium.find_element(By.NAME, 'password')
        password_input.send_keys('0216shu0211')
        self.selenium.find_element(By.CLASS_NAME, 'btn').click()

        self.assertEqual('日記一覧 | Private Diary', self.selenium.title)