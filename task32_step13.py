from selenium import webdriver
import time
import unittest

driver_path = r'D:\GoogleDrive\chromedriver.exe'
link2 = 'http://suninjuly.github.io/registration2.html'
link1 = 'http://suninjuly.github.io/registration1.html'

class TestRegistration1(unittest.TestCase):
	def setUp(self):
		self.link = link1
		self.browser = webdriver.Chrome(driver_path)
		self.browser.get(self.link)

	def tearDown(self):
		self.browser.quit()

	def test_input_first_name(self):
		browser = self.browser
		input1 = browser.find_elements_by_css_selector(".first_block .first")
		self.assertEqual(len(input1),1,"NoSuchElementException:FirstName")
		input1[0].send_keys('il')

	def test_input_second_name(self):
		browser = self.browser
		input1 = browser.find_elements_by_css_selector(".first_block .second")
		self.assertEqual(len(input1),1,"NoSuchElementException:SecondName")
		input1[0].send_keys('val')

	def test_input_email(self):
		browser = self.browser
		input1 = browser.find_elements_by_css_selector(".first_block .third")
		self.assertEqual(len(input1),1,"NoSuchElementException:Email")
		input1[0].send_keys('il@fake.com')


	def test_registration(self):
		#executable_path=r'D:\GoogleDrive\chromedriver.exe'
		browser = self.browser
		browser.get(self.link)

		self.test_input_first_name()
		self.test_input_second_name()
		self.test_input_email()

		# Отправляем заполненную форму
		button = browser.find_element_by_css_selector("button.btn")
		button.click()

		time.sleep(1)

		# находим элемент, содержащий текст
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		# записываем в переменную welcome_text текст из элемента welcome_text_elt
		welcome_text = welcome_text_elt.text
		self.assertEqual("Congratulations! You have successfully registered!",welcome_text,'NoSuchElementException:WelcomeText')

class TestRegistration2(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Chrome(driver_path)
		self.link = link2
		self.browser.get(self.link)

	def tearDown(self):
		self.browser.quit()

	def test_input_first_name(self):
		browser = self.browser
		input1 = browser.find_elements_by_css_selector(".first_block .first")
		self.assertEqual(len(input1),1,"NoSuchElementException:FirstName")
		input1[0].send_keys('il')

	def test_input_second_name(self):
		browser = self.browser
		input1 = browser.find_elements_by_css_selector(".first_block .second")
		self.assertEqual(len(input1),1,"NoSuchElementException:SecondName")
		input1[0].send_keys('val')

	def test_input_email(self):
		browser = self.browser
		input1 = browser.find_elements_by_css_selector(".first_block .third")
		self.assertEqual(len(input1),1,"NoSuchElementException:Email")
		input1[0].send_keys('il@fake.com')


	def test_registration(self):
		#executable_path=r'D:\GoogleDrive\chromedriver.exe'
		browser = self.browser
		browser.get(self.link)

		self.test_input_first_name()
		self.test_input_second_name()
		self.test_input_email()

		# Отправляем заполненную форму
		button = browser.find_element_by_css_selector("button.btn")
		button.click()

		time.sleep(1)

		# находим элемент, содержащий текст
		welcome_text_elt = browser.find_element_by_tag_name("h1")
		# записываем в переменную welcome_text текст из элемента welcome_text_elt
		welcome_text = welcome_text_elt.text
		self.assertEqual("Congratulations! You have successfully registered!",welcome_text,'NoSuchElementException:WelcomeText')

if __name__ == "__main__":
	unittest.main()