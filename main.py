from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import time


driver = webdriver.Chrome()


driver.get("https://oldmy.sdu.edu.kz/index.php?mod=course_reg")


username_field = driver.find_element("name","username")
password_field = driver.find_element("name","password")


username_field.send_keys("username")
password_field.send_keys("password")

login_button = driver.find_element("xpath", "/html/body/div/div[5]/div/form/input[2]")
login_button.click()


search_type_dropdown = Select(driver.find_element("id","idCmbSearchType"))
search_type_dropdown.select_by_value("by_search")



show_button = driver.find_element("id","idBtnShow")
show_button.click()

time.sleep(1)


search_input = driver.find_element("id", "search_dk")
search_input.send_keys("CSS 415")

time.sleep(1)

search_button_xpath = "//input[@value=' Search ']"
search_button = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, search_button_xpath))
)
search_button.click()

time.sleep(1)


def is_section_available(section_id):
    section_xpath = f"//tr[@id='{section_id}']"
    try:
        section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, section_xpath))
        )
        return "sections selectable" in section.get_attribute("class")
    except TimeoutException:
        return False



time.sleep(1)

section_id = "norm56255"


while not is_section_available(section_id):
    search_button_xpath = "//input[@value=' Search ']"
    search_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, search_button_xpath))
    )
    search_button.click()

    time.sleep(1.5)

    section_id = "norm56255"


if is_section_available(section_id):
    radio_button1_xpath = "//input[@id='rbs56254']"
    radio_button1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, radio_button1_xpath))
    )
    radio_button1.click()

    time.sleep(1)


    # radio_button2_xpath = "//input[@id='59091']"
    # radio_button2 = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, radio_button2_xpath))
    # )
    # radio_button2.click()
    #
    # time.sleep(1)


    section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//tr[@id='{section_id}']"))
    )

    radio_button3_xpath = "//input[@name='mufSQ[]' and @value='4314']"
    radio_button3 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, radio_button3_xpath))
    )
    radio_button3.click()

    time.sleep(1)


    add_button_xpath = "//a[@class='button' and contains(@onclick, 'AddCourse')]"
    add_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, add_button_xpath))
    )
    add_button.click()


    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert_text = alert.text
    print(f"Alert Text: {alert_text}")
    alert.accept()



# time.sleep(500)


# driver.quit()
