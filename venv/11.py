from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def check_tip_calculation():
    my_driver = webdriver.Chrome(executable_path='C:/temp/chromedriver_win32/chromedriver.exe')
    my_driver.get("file:///D:/Documents/DevOpsExperts/lesson%204/tip_calc/index.html")
    my_driver.find_element_by_id("billamt").send_keys(100)
    my_driver.find_element_by_id("peopleamt").send_keys(5)
    my_driver.find_element_by_xpath('//*[@id="serviceQual"]/option[3]').click()
    my_driver.find_element_by_id('calculate').click()
    my_driver.find_elements()
    result = my_driver.find_element_by_id("tip")
    if result.text == "4.00":
        print("test finished successfully")
    else:
        print(result.text)
    # my_driver.refresh()
    # print(my_driver.current_url)
    # print(my_driver.title)
    # locators by ID  Name  LinkText  PatrialLinkText  ClassName  Xpath
    # my_driver.close()

for i in range(3):
    check_tip_calculation()
    sleep(2)


my_driver.find_element_by_id("billamt").send_keys(100 + Keys.TAB)