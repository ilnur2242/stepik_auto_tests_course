from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def func(x):
	return math.log(abs(12*math.sin(int(x))))

link = 'http://suninjuly.github.io/execute_script.html'
#link = 'http://suninjuly.github.io/registration2.html' # bug
try: 
	browser = webdriver.Chrome(executable_path=r'D:\GoogleDrive\chromedriver.exe') #executable_path=r'D:\GoogleDrive\chromedriver.exe'
	browser.get(link)

	# Ваш код, который заполняет обязательные поля
	x = browser.find_element_by_id('input_value').text
	y = str(func(x))
	
	
	button = browser.find_element_by_css_selector("button.btn")
	#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	browser.execute_script("window.scrollBy(0, 100);")

	input1 = browser.find_element_by_id('answer')
	input1.send_keys(y)

	input1 = browser.find_element_by_id('robotCheckbox')
	input1.click()

	input1 = browser.find_element_by_id('robotsRule')
	input1.click()

	# Отправляем заполненную форму
	
	button.click()

	# Проверяем, что смогли зарегистрироваться
	# ждем загрузки страницы
	

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	browser.quit()