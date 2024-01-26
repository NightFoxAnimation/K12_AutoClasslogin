import pyautogui as pag
import time
import webbrowser
import json
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
chrome_options.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2,
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2,
    "profile.default_content_setting_values.notifications": 2,
  })
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-infobars")
driver = webdriver.Chrome(chrome_options)
email = 'gamundson'
password = 'Oklahoma2022'

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
                    if (time_now >= class_time_a and time_now <= class_time_b):       
                        chrome2_options = Options()
                        chrome2_options.add_experimental_option("detach", True)
                        chrome2_options.add_experimental_option("excludeSwitches", ['enable-automation']);
                        chrome_options.add_argument("--disable-infobars")
                        chrome2_options.add_experimental_option("prefs", { \
                            "profile.default_content_setting_values.media_stream_mic": 2,
                            "profile.default_content_setting_values.media_stream_camera": 2,
                            "profile.default_content_setting_values.geolocation": 2,
                            "profile.default_content_setting_values.notifications": 2,
                        })
                        driver2 = webdriver.Chrome(chrome2_options)
                        driver2.get('https://login.k12.com/')
                        time.sleep(5)
                        try:
                            login_email_field = driver2.find_element(By.ID, 'okta-signin-username')  
                            login_email_field.send_keys(email)
                            login_pass_field = driver2.find_element(By.ID, 'okta-signin-password')
                            login_pass_field.send_keys(password)
                            login_log_field = driver2.find_element(By.ID, 'okta-signin-submit')
                            login_log_field.click()
                        except:
                            print('no class login needed')

                        time.sleep(5)
                        schedule = driver2.find_element(By.ID,'sidebar-nav').find_element(By.TAG_NAME,'li').find_element(By.TAG_NAME,'a')
                        schedule.click()
                        time.sleep(5)
                        try:
                            classes2 = driver2.find_element(By.XPATH,'//*[@id="components"]/div/div[2]/div/div[2]/div/div[3]/table/tbody').find_elements(By.TAG_NAME,'tr')
                            for x in classes2:
                                required = x.find_element(By.XPATH,'.//td/a/span/span[1]/span[2]/span[2]').get_attribute('innerText')
                                if (required == 'Required'):
                                    class_time_x = x.find_element(By.XPATH,'.//td/a/span/span[2]/span').get_attribute('innerText')
                                    class_time_x_a = time_conv(class_time_x.split(' - ')[0])
                                    class_time_x_b = time_conv(class_time_x.split(' - ')[1])
                                    time_now_x = int(datetime.now().strftime("%H%M"))
                                    if (time_now_x >= class_time_x_a and time_now_x <= class_time_x_b):
                                        current_window_x = driver2.current_window_handle
                                        x.find_element(By.XPATH,'.//td/a').click()
                                        time.sleep(10)
                                        for h_x in driver2.window_handles:
                                            if (h_x != current_window_x):
                                                driver2.switch_to.window(h_x)
                                                break
                                        driver2.refresh()
                                        print ((class_time_x_b - time_now_x))
                                        time.sleep((class_time_x_b - time_now_x) * 60)
                                        driver2.quit()
                                    else:
                                        print ('no driver2 classes right now')
                                        driver2.quit()
                                else:
                                    print ('no driver2 classes required')
                                    driver2.quit()
                        except Exception as error:
                            print (f'driver2 no find. error: {error}')
                    else:
                        print ('no classes right now')
        except Exception as error:
            print (f'no find. error: {error}')
            
def main():
    driver.get('https://login.k12.com/')
    time.sleep(5)
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