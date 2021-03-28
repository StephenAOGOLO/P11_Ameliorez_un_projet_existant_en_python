from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.chrome.webdriver import WebDriver as wdc
from selenium import webdriver
from substitute.operations import *
from substitute.models import *
from pathlib import Path
import time, os, sys

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
            cls.selenium = wdc(executable_path="D:\\STEPHEN_AO\\05_THE_PYTHON_APPLICATION_DEVELOPER\\PROJECTS\\11_Ameliorez_un_projet_existant_en_python\\P_11\\1.2\\Pure_Beurre\\substitute\\project_tester\\chromedriver.exe")
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
        cls.stored_version = cls.text_json["fr"]["browser"]["version"]
        cls.colette_story = cls.text_json["fr"]["home"]["colette_story"]
        cls.remy_story = cls.text_json["fr"]["home"]["remy_story"]
        cls.selenium.implicitly_wait(10)
        cls.selenium.get('%s%s' % (cls.live_server_url, "/substitute/home/"))
        print(cls.live_server_url + "/substitute/home/")
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        print("\nTEARDOWN\n")
        cls.selenium.quit()
        super().tearDownClass()

    def test_02_logout(self):
        print("\nLOGOUT\n")
        time.sleep(2)
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

    def test_01_login(self):
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

    def test_03_version(self):
        print("\nVERSION\n")
        time.sleep(2)
        current_tag = self.selenium.find_element_by_id("version_tag")
        current_version = current_tag.find_element_by_tag_name("h4").text
        print(self.stored_version, " <-> "+current_version)
        self.assertEqual(self.stored_version, current_version)

    def test_04_colette_story(self):
        print("\nCOLETTE STORY\n")
        time.sleep(2)
        self.selenium.find_element_by_id("colette-story").click()
        time.sleep(2)
        print(self.selenium.current_url, " <-> "+self.colette_story)
        self.assertEqual(self.selenium.current_url, self.colette_story)
        self.selenium.back()

    def test_05_remy_story(self):
        print("\nREMY STORY\n")
        time.sleep(2)
        self.selenium.find_element_by_id("remy-story").click()
        time.sleep(2)
        print(self.selenium.current_url, " <-> " + self.remy_story)
        self.assertEqual(self.selenium.current_url, self.remy_story)
        self.selenium.back()

    def test_06_product_picture(self):
        print("\nPRODUCT PICTURE\n")
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
        self.a_category = Category.objects.create(name="product",
                                                  id_name="product")
        self.an_aliment = Aliment.objects.create(name="product",
                                                 category=self.a_category.name,
                                url_image="https://static.openfoodfacts.org/images/products/730/040/048/1571/front_fr.78.200.jpg",
                                url="https://fr.openfoodfacts.org/produit/7300400481571/wasa-tartine-croustillante-leger")

        self.a_category.save()
        self.an_aliment.save()
        time.sleep(2)
        searched_aliment = self.selenium.find_element_by_id("home-searchbar")
        searched_aliment.send_keys(self.an_aliment.name)
        time.sleep(2)
        self.selenium.find_element_by_id("button-searchbar").click()
        time.sleep(2)
        self.selenium.find_element_by_id("product-picture").click()
        print(self.selenium.current_url, " <-> " + self.an_aliment.url)
        self.assertEqual(self.selenium.current_url, self.an_aliment.url)
        self.selenium.back()

    def test_07_account_activation(self):
        print("\nACCOUNT ACTIVATION\n")
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
        self.another_user_clear_password = "anotherselenium.1234"
        time.sleep(2)
        main_url = self.live_server_url
        self.selenium.find_element_by_class_name("login").click()
        time.sleep(2)
        self.assertEqual(
            self.selenium.current_url,
            main_url + reverse("substitute:login")
        )
        self.selenium.find_element_by_id("create_account").click()
        self.assertEqual(
            self.selenium.current_url,
            main_url + reverse("substitute:register")
        )
        time.sleep(2)
        username_input = self.selenium.find_element_by_id("id_username")
        username_input.send_keys("another")
        time.sleep(2)
        username_input = self.selenium.find_element_by_id("id_email")
        username_input.send_keys("another_chrome_user@purebeurre.com")
        time.sleep(2)
        username_input = self.selenium.find_element_by_id("id_password1")
        username_input.send_keys(self.another_user_clear_password)
        time.sleep(2)
        username_input = self.selenium.find_element_by_id("id_password2")
        username_input.send_keys(self.another_user_clear_password)
        time.sleep(2)
        self.selenium.find_element_by_id("button-create").click()
        time.sleep(2)
        first_activate_msg = self.selenium.find_element_by_id("first-activate-msg").text
        second_activate_msg = self.selenium.find_element_by_id("second-activate-msg").text
        self.assertEqual(
            first_activate_msg,
            "Nous vous avons envoyé un E-mail d'activation."
        )
        self.assertEqual(
            second_activate_msg,
            'Merci de Verifier et cliquer sur le lien "ACTIVER MON COMPTE"'
        )
        time.sleep(2)
        #self.selenium.find_element_by_id("back-home").click()


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
                executable_path="D:\\STEPHEN_AO\\05_THE_PYTHON_APPLICATION_DEVELOPER\\PROJECTS\\11_Ameliorez_un_projet_existant_en_python\\P_11\\1.2\\Pure_Beurre\\substitute\\project_tester\\chromedriver.exe")
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
                executable_path="D:\\STEPHEN_AO\\05_THE_PYTHON_APPLICATION_DEVELOPER\\PROJECTS\\11_Ameliorez_un_projet_existant_en_python\\P_11\\1.2\\Pure_Beurre\\substitute\\project_tester\\chromedriver.exe")
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



