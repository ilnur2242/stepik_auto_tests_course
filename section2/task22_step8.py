from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os



link = 'http://suninjuly.github.io/file_input.html'
#link = 'http://suninjuly.github.io/registration2.html' # bug
try: 
	browser = webdriver.Chrome(executable_path=r'D:\GoogleDrive\chromedriver.exe') #executable_path=r'D:\GoogleDrive\chromedriver.exe'
	browser.get(link)

	# Ваш код, который заполняет обязательные поля
	
	
	
	#browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	

	input1 = browser.find_element_by_name('firstname')
	input1.send_keys("il")

	input1 = browser.find_element_by_name('lastname')
	input1.send_keys("val")

	input1 = browser.find_element_by_name('email')
	input1.send_keys("val@fake")

	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir,'file.txt')
	input1 = browser.find_element_by_id('file')
	input1.send_keys(file_path)


	# Отправляем заполненную форму
	button = browser.find_element_by_css_selector("button.btn")
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