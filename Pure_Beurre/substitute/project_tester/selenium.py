from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver as wdc
from selenium.webdriver.opera.webdriver import WebDriver as wdo
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options as opt
#from selenium.webdriver.chrome import options as opt
from substitute.operations import *
from substitute.models import *
from pathlib import Path
import time, os

BASE_DIR = Path(__file__).resolve().parent.parent


class SeleniumTestsChrome(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        print("\nSETUP\n")
        super().setUpClass()
        cls.text_page = Text.objects.create(
            language="fr",
            mentions_title = "title",
            mentions_id_fn = "mentions_id_fn",
            mentions_id_ln = "mentions_id_ln",
            mentions_id_ph = "mentions_id_ph",
            mentions_id_m = "mentions_id_m",
            mentions_id_pn = "mentions_id_pn",
            mentions_id_s = "mentions_id_s",
            mentions_a_rcs = "mentions_a_rcs",
            mentions_a_fn = "mentions_a_fn",
            mentions_a_cgv = "mentions_a_cgv",
            mentions_cookies = "mentions_cookies",
            home_s = "home_s",
            home_c = "home_c",
            home_bm = "home_bm",
        )
        cls.a_user_clear_password = "selenium.1234"
        cls.a_user_chrome = User.objects.create_user(username="chrome_user", email="chrome_user@purebeurre.com", password=cls.a_user_clear_password)
        cls.a_user_chrome.save()
        cls.a_customer_chrome = Customer(user=cls.a_user_chrome)
        cls.a_customer_chrome.save()
        if os.name == 'nt':
            cls.selenium = wdc(executable_path="D:\\STEPHEN_AO\\05_THE_PYTHON_APPLICATION_DEVELOPER\\PROJECTS\\08_Creez_une_plateforme_pour_amateur_de_nutella\\projet\\P8_1.1\\Pure_Beurre\\substitute\\project_tester\\chromedriver.exe")
            cls.text_json = open_js_file(".\\substitute\\static\\substitute\\json\\text.json")

        else:
            cls.wdc_options = webdriver.ChromeOptions()
            cls.wdc_options.add_argument('--headless')
            cls.wdc_options.add_argument('--disable-gpu')
            cls.wdc_options.add_argument('--window-size=1280x1696')
            cls.wdc_options.add_argument('--disable-infobars')
            cls.wdc_options.add_argument('--disable-dev-shm-usage')
            cls.wdc_options.add_argument('--no-sandbox')
            cls.wdc_options.add_argument('--remote-debugging-port=9222')
            cls.wdc_options.add_argument('http://localhost')
            print(cls.wdc_options.arguments)
            cls.selenium = wdc(executable_path=os.path.join(BASE_DIR, 'project_tester/chromedriver'), options=cls.wdc_options)
            cls.text_json = open_js_file(os.path.join(BASE_DIR, "static/substitute/json/text.json"))

        cls.stored_version = cls.text_json["version"]
        cls.selenium.implicitly_wait(10)
        cls.selenium.get('%s%s' % (cls.live_server_url, "/substitute/home/"))
        print(cls.live_server_url + "/substitute/home/")

    @classmethod
    def tearDownClass(cls):
        print("\nTEARDOWN\n")
        cls.selenium.quit()
        super().tearDownClass()

    def test_logout(self):
        print("\nLOGOUT\n")
        self.text_page = Text.objects.create(
            language="fr",
            mentions_title = "title",
            mentions_id_fn = "mentions_id_fn",
            mentions_id_ln = "mentions_id_ln",
            mentions_id_ph = "mentions_id_ph",
            mentions_id_m = "mentions_id_m",
            mentions_id_pn = "mentions_id_pn",
            mentions_id_s = "mentions_id_s",
            mentions_a_rcs = "mentions_a_rcs",
            mentions_a_fn = "mentions_a_fn",
            mentions_a_cgv = "mentions_a_cgv",
            mentions_cookies = "mentions_cookies",
            home_s = "home_s",
            home_c = "home_c",
            home_bm = "home_bm",
        )
        time.sleep(2)
        main_url = self.live_server_url
        self.selenium.find_element_by_class_name("logout").click()
        time.sleep(2)
        self.assertEqual(
            self.selenium.current_url,
            main_url + reverse("substitute:home")
        )

    def test_login(self):
        print("\nLOGIN\n")
        time.sleep(2)
        main_url = self.live_server_url
        self.selenium.find_element_by_class_name("login").click()
        time.sleep(2)
        self.assertEqual(
            self.selenium.current_url,
            main_url + reverse("substitute:login")
        )
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys(self.a_user_chrome.username)
        time.sleep(2)
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys(self.a_user_clear_password)
        time.sleep(2)
        self.selenium.find_element_by_class_name("connect-user").click()
        time.sleep(2)
        main_url = self.live_server_url
        self.assertEqual(
            self.selenium.current_url,
            main_url + reverse("substitute:account")
        )

    def test_version(self):
        print("\nVERSION\n")
        current_version = self.selenium.find_element_by_id("version_tag")
        if self.assertEqual(self.stored_version, current_version):
            return 0
        return 1


class SeleniumTestsError404(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        print("\nSETUP\n")
        super().setUpClass()
        cls.text_page = Text(
            language="fr",
            mentions_title = "title",
            mentions_id_fn = "mentions_id_fn",
            mentions_id_ln = "mentions_id_ln",
            mentions_id_ph = "mentions_id_ph",
            mentions_id_m = "mentions_id_m",
            mentions_id_pn = "mentions_id_pn",
            mentions_id_s = "mentions_id_s",
            mentions_a_rcs = "mentions_a_rcs",
            mentions_a_fn = "mentions_a_fn",
            mentions_a_cgv = "mentions_a_cgv",
            mentions_cookies = "mentions_cookies",
            home_s = "home_s",
            home_c = "home_c",
            home_bm = "home_bm",
        )
        cls.text_page.save()
        if os.name == 'nt':
            cls.selenium = wdc(
                executable_path="D:\\STEPHEN_AO\\05_THE_PYTHON_APPLICATION_DEVELOPER\\PROJECTS\\08_Creez_une_plateforme_pour_amateur_de_nutella\\projet\\P8_1.1\\Pure_Beurre\\substitute\\project_tester\\chromedriver.exe")
        else:
            cls.wdc_options = webdriver.ChromeOptions()
            cls.wdc_options.add_argument('--headless')
            cls.wdc_options.add_argument('--disable-gpu')
            cls.wdc_options.add_argument('--window-size=1280x1696')
            cls.wdc_options.add_argument('--disable-infobars')
            cls.wdc_options.add_argument('--disable-dev-shm-usage')
            cls.wdc_options.add_argument('--no-sandbox')
            cls.wdc_options.add_argument('--remote-debugging-port=9222')
            cls.wdc_options.add_argument('http://localhost')
            print(cls.wdc_options.arguments)
            cls.selenium = wdc(executable_path=os.path.join(BASE_DIR, 'project_tester/chromedriver'),
                               options=cls.wdc_options)

        cls.selenium.get(cls.live_server_url)

    @classmethod
    def tearDownClass(cls):
        print("\nTEARDOWN\n")
        cls.selenium.quit()
        super().tearDownClass()

    def test_404(self):
        print("\nTEST 404\n")
        time.sleep(2)
        alert = self.selenium.find_element_by_id("404-area")
        self.assertEqual(alert.find_element_by_tag_name("h1").text,
                         "Cette page est introuvable !!!!")


class SeleniumTestsError500(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        print("\nSETUP\n")
        super().setUpClass()
        cls.text_page = Text(
            language="fr",
            mentions_title = "title",
            mentions_id_fn = "mentions_id_fn",
            mentions_id_ln = "mentions_id_ln",
            mentions_id_ph = "mentions_id_ph",
            mentions_id_m = "mentions_id_m",
            mentions_id_pn = "mentions_id_pn",
            mentions_id_s = "mentions_id_s",
            mentions_a_rcs = "mentions_a_rcs",
            mentions_a_fn = "mentions_a_fn",
            mentions_a_cgv = "mentions_a_cgv",
            mentions_cookies = "mentions_cookies",
            home_s = "home_s",
            home_c = "home_c",
            home_bm = "home_bm",
        )
        cls.text_page.save()
        cls.a_user_clear_password = "error.1234"
        cls.a_user_chrome = User.objects.create_user(username="user_error_500", email="user_error_500@purebeurre.com", password=cls.a_user_clear_password)
        cls.a_user_chrome.save()
        if os.name == 'nt':
            cls.selenium = wdc(
                executable_path="D:\\STEPHEN_AO\\05_THE_PYTHON_APPLICATION_DEVELOPER\\PROJECTS\\08_Creez_une_plateforme_pour_amateur_de_nutella\\projet\\P8_1.1\\Pure_Beurre\\substitute\\project_tester\\chromedriver.exe")
        else:

            cls.wdc_options = webdriver.ChromeOptions()
            cls.wdc_options.add_argument('--headless')
            cls.wdc_options.add_argument('--disable-gpu')
            cls.wdc_options.add_argument('--window-size=1280x1696')
            cls.wdc_options.add_argument('--disable-infobars')
            cls.wdc_options.add_argument('--disable-dev-shm-usage')
            cls.wdc_options.add_argument('--no-sandbox')
            cls.wdc_options.add_argument('--remote-debugging-port=9222')
            cls.wdc_options.add_argument('http://localhost')
            print(cls.wdc_options.arguments)
            cls.selenium = wdc(executable_path=os.path.join(BASE_DIR, 'project_tester/chromedriver'),
                               options=cls.wdc_options)
        cls.selenium.get('%s%s' % (cls.live_server_url, "/substitute/home/"))

    @classmethod
    def tearDownClass(cls):
        print("\nTEARDOWN\n")
        cls.selenium.quit()
        super().tearDownClass()


