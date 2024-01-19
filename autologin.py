import pyautogui as pag
import time
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime

pag.FAILSAFE = True
pag.PAUSE = 1
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options)

def login_to_stride(email, password):
    webbrowser.open('https://login.k12.com/', new=0, autoraise=True)
    pag.click(200, 350)
    pag.typewrite(email)
    time.sleep(.5)
    pag.typewrite(['\t'])
    pag.typewrite(password)
    time.sleep(.5)
    pag.press('\n')

def time_conv(t):
    old_time = datetime.strptime(t,'%I:%M %p')
    new_time = datetime.strftime(old_time,'%H%M')
    return int(new_time)

def my_schedule():
        time.sleep(5)
        schedule = driver.find_element(By.ID,'sidebar-nav').find_element(By.TAG_NAME,'li').find_element(By.TAG_NAME,'a')
        schedule.click()
        time.sleep(5)
        try:
            classes = driver.find_element(By.XPATH,'//*[@id="components"]/div/div[2]/div/div[2]/div/div[3]/table/tbody').find_elements(By.TAG_NAME,'tr')
            for i in classes:
                required = i.find_element(By.XPATH,'.//td/a/span/span[1]/span[2]/span[2]').get_attribute('innerText')
                if (required == 'Required'):
                    class_time = i.find_element(By.XPATH,'.//td/a/span/span[2]/span').get_attribute('innerText')
                    class_time_a = time_conv(class_time.split(' - ')[0])
                    class_time_b = time_conv(class_time.split(' - ')[1])
                    time_now = int(datetime.now().strftime("%H%M"))
                    if (time_now > class_time_a and time_now < class_time_b):
                        chrome2_options = Options()
                        chrome2_options.add_experimental_option("detach", True)
                        chrome2_options.add_experimental_option("excludeSwitches", ['enable-automation']);
                        driver2 = webdriver.Chrome(chrome2_options)
                        class_url = i.find_element(By.XPATH,'.//td/a').get_attribute('data-url')
                        driver2.get(f'https://login.k12.com/{class_url}')
                        time.sleep(10 * 60)
                        driver2.refresh()
                        time.sleep((class_time_b - class_time_a) * 60)
                        driver2.close()
                    else:
                        print ('no classes right now')
        except:
            print ('no find')
def main():
    driver.get('https://login.k12.com/')
    time.sleep(5)
    email = 'UsernameHere'
    password = 'PasswordHere'

    try:
        login_email_field = driver.find_element(By.ID, 'okta-signin-username')
        login_email_field.send_keys(email)
        login_pass_field = driver.find_element(By.ID, 'okta-signin-password')
        login_pass_field.send_keys(password)
        login_log_field = driver.find_element(By.ID, 'okta-signin-submit')
        login_log_field.click()
    except:
        print('no login needed')

    my_schedule()

if __name__ == "__main__":
    driver.get('https://login.k12.com/')
    main()
    while True:
        main()
        time.sleep(300)


