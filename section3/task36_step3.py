import pytest
import time
import math
from selenium import webdriver

task_answer = []

links = ["https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1", 
"https://stepik.org/lesson/236897/step/1", 
"https://stepik.org/lesson/236898/step/1", 
"https://stepik.org/lesson/236899/step/1", 
"https://stepik.org/lesson/236903/step/1", 
"https://stepik.org/lesson/236904/step/1", 
"https://stepik.org/lesson/236905/step/1"]

@pytest.fixture(scope="function")
def browser():
	print("\nstart browser for test..")
	browser = webdriver.Chrome(executable_path=r'D:\GoogleDrive\chromedriver.exe')
	yield browser
	print("\nquit browser..")
	browser.quit()

@pytest.mark.parametrize('link', links)
def test_guest_should_see_login_link(browser:webdriver.Chrome, link):
	browser.get(link)
	time.sleep(5)
	input1 = browser.find_element_by_css_selector("textarea.ember-text-area")
	answer = math.log(int(time.time()))
	input1.send_keys(answer)
	time.sleep(2)

	browser.find_element_by_css_selector('button.submit-submission').click()
	time.sleep(3)
	fidback = browser.find_element_by_css_selector('.smart-hints__hint').text
	
	if fidback != "Correct!":
		with open('file.txt','a') as file:
			file.write(fidback + "\n")
	

	#browser.find_element_by_css_selector('#')
