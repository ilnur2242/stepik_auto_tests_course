from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time



link = 'http://suninjuly.github.io/selects1.html'
#link = 'http://suninjuly.github.io/registration2.html' # bug
try: 
	browser = webdriver.Chrome(executable_path=r'D:\GoogleDrive\chromedriver.exe') #executable_path=r'D:\GoogleDrive\chromedriver.exe'
	browser.get(link)

	# Ваш код, который заполняет обязательные поля
	num1 = browser.find_element_by_id('num1').text
	num2 = browser.find_element_by_id('num2').text


	select = Select(browser.find_element_by_tag_name("select"))
	select.select_by_value(str(int(num1)+int(num2)))


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