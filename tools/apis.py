from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.select import Select 

def sandhi_api(txt1, txt2):
    
    driver = webdriver.Chrome("/home/piyush/Downloads/chromedriver")
    driver.minimize_window()
    driver.get("http://sanskrit.uohyd.ac.in/scl/")

    tools = driver.find_element_by_xpath('//*[@id="menu"]/li[1]/a')
    actions = ActionChains(driver)
    actions.move_to_element(tools).perform()
    
    driver.implicitly_wait(10)
    splitter = driver.find_element_by_xpath('//*[@id="sandhi-joiner"]')
    splitter.click()

    driver.find_element_by_xpath('//*[@id="text"]').send_keys(txt1)
    driver.find_element_by_xpath('//*[@id="text1"]').send_keys(txt2)
    driver.find_element_by_xpath('//*[@id="submit-sandhi"]').click()

    time.sleep(5)
    result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="AoutoNumber1"]/tbody/tr[2]/td[3]/center/font')))
    return result.text


def sandhi_splitter_api(txt1, type):
    
    driver = webdriver.Chrome("/home/piyush/Downloads/chromedriver")
    driver.minimize_window()
    driver.get("http://sanskrit.uohyd.ac.in/scl/")

    tools = driver.find_element_by_xpath('//*[@id="menu"]/li[1]/a')
    actions = ActionChains(driver)
    actions.move_to_element(tools).perform()
    
    driver.implicitly_wait(10)
    splitter = driver.find_element_by_xpath('//*[@id="sandhi-splitter"]')
    splitter.click()

    # Select पदच्छेदः
    sandhi_type= Select(driver.find_element_by_xpath('//*[@id="sandhi_type"]'))
    sandhi_type.select_by_visible_text(type)

    driver.find_element_by_xpath('//*[@id="word"]').send_keys(txt1)
    driver.find_element_by_xpath('//*[@id="submit-sandhi"]').click()

    time.sleep(5)

    output_div = driver.find_element_by_xpath('//*[@id="finalout"]')
    result = ""
    first = True
    for word in output_div.find_elements_by_tag_name('a'):
        if (len(word.text) == 0):
            break
        if(not(first)):
            result += " + "
        else:
            first = False
        result += word.text
    return result

def eng_to_sans_api(word):
    url = "https://sanskritdictionary.com/?q=" + word + "&display=devanagari"
    driver = webdriver.Chrome("/home/piyush/Downloads/chromedriver")
    driver.minimize_window()
    driver.get(url)

    result = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[5]/td[2]/table/tbody/tr/td/div/table/tbody/tr[3]/td[1]')
    return result.text


def sans_to_eng_api(word): 

    url = "https://sanskritdictionary.com/?q=" + word + "&lang=en&action=Search"
    driver = webdriver.Chrome("/home/piyush/Downloads/chromedriver")
    driver.minimize_window()
    driver.get(url)
    
    result = driver.find_element_by_xpath('/html/body/table[1]/tbody/tr[3]/td[2]/table/tbody/tr/td/div/table/tbody/tr[3]/td[2]')
    return result.text