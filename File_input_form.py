from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os



try:


    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name=browser.find_element_by_name('firstname')
    first_name.send_keys('Alexander')

    last_name=browser.find_element_by_name('lastname')
    last_name.send_keys('Baranok')

    e_mail=browser.find_element_by_name('email')
    e_mail.send_keys('s_98baranok@gmail.com')


    #Загружаем файл
    current_dir=os.path.abspath(os.path.dirname(__file__))

    file_path=os.path.join(current_dir,'file.txt')

    choose_file=browser.find_element_by_id('file')

    choose_file.send_keys(file_path)












    button = browser.find_element_by_css_selector('.btn.btn-primary')
    button.click()




    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(3)




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
     time.sleep(5)
    # закрываем браузер после всех манипуляций
     browser.quit()