from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_option_to_add_offer_to_cart(browser):
	browser.get(link)
	#time.sleep(10)

	basket_button = browser.find_element(By.CSS_SELECTOR,'button.btn-add-to-basket')
	
	assert basket_button, 'add_to_cart_button does not exist'