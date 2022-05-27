from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os
import math

def func(x):
	return math.log(abs(12*math.sin(int(x))))

link = 'http://suninjuly.github.io/redirect_accept.html'
try: 
	browser = webdriver.Chrome(executable_path=r'D:\GoogleDrive\chromedriver.exe') #executable_path=r'D:\GoogleDrive\chromedriver.exe'
	browser.get(link)

	# Ваш код, который заполняет обязательные поля
	button = browser.find_element_by_css_selector("button.btn")
	button.click()
	
	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)
	
	x = browser.find_element_by_id('input_value').text
	y = str(func(x))


	#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	

	input1 = browser.find_element_by_id('answer')
	input1.send_keys(y)

	button = browser.find_element_by_css_selector("button.btn")
	button.click()



	# Отправляем заполненную форму
	

	# Проверяем, что смогли зарегистрироваться
	# ждем загрузки страницы
	

except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')
finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	browser.quit()