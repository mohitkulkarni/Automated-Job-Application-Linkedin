# -------------------------------Linkedin Automation - Automated Job Application----------------------------------------

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=" \
              "python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=" \
              "false&position=1&pageNum=0"


def url_update():
    new_url = driver.window_handles[0]
    driver.switch_to.window(new_url)



count = 0
chrome_driver_path = "C:\Program Files (x86)\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(LINKEDIN_URL)

driver.maximize_window()


# login
login = driver.find_element_by_class_name("nav__button-secondary")
login.click()
print("TEST1 ...... goto login")
url_update()


username = driver.find_element_by_id("username")
username.send_keys("mandre.tunes12@gmail.com")
password = driver.find_element_by_id("password")
password.send_keys("iammandre")

enter = driver.find_element_by_class_name("btn__primary--large ")
enter.send_keys(Keys.ENTER)
print("TEST2 ...... login success")

# select job title
titles = driver.find_elements_by_class_name("jobs-search-results__list-item")


for title in titles:
    print("called")
    url_update()
    title.click()
    print("TEST3 ...... select title")

    time.sleep(1)
    # click save Button
    url_update()
    save = driver.find_element_by_css_selector(".jobs-save-button")
    save.click()
    print("TEST4 ...... save")

    url_update()
    count += 1
    print(f"job Saved : {count}")

    try:
        # follow
        # follow_company_name = driver.find_element_by_css_selector(".artdeco-entity-lockup__subtitle")
        # follow_head = driver.find_element_by_link_text(follow_company_name.text)
        # follow_head.click()
        # print("TEST5 ...... follow page")

        # time.sleep(1.5)
        # follow = driver.find_element_by_css_selector("button.follow  ")
        # follow.click()
        # time.sleep(1)
        print("no error")

    except NoSuchElementException:
        print("error")
        pass
    finally:
        applied_count = count+1
        print(f"job Saved : {applied_count}")

