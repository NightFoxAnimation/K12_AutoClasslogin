import pyautogui as pag
import time
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime

# Set the position of the mouse cursor on the screen
pag.FAILSAFE = True
pag.PAUSE = 1
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']);
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options)
# driver.minimize_window()
# already_in_class = False

def login_to_stride(email, password):
    # chrome_options.add_argument("--headless")
    webbrowser.open('https://login.k12.com/', new=0, autoraise=True)
    pag.click(200, 350)
    # Typag.click(248, 375)pe in email and password into the input fields
    pag.typewrite(email)
    time.sleep(.5)
    pag.typewrite(['\t']) # Tab to move to the next field (password)
    pag.typewrite(password)
    time.sleep(.5)
    pag.press('\n')
    #pag.typewrite(['\r']) # Enter key to submit login form

def time_conv(t):
    # print (t)
    old_time = datetime.strptime(t,'%I:%M %p')
    new_time = datetime.strftime(old_time,'%H%M')
    # print (new_time)
    return int(new_time)

def my_schedule():
         # Click on the "Join" button to start attending the class
       #pag.click(248, 375) # Modify these coordinates to match your screen resolution and position of the "Join" button
        # driver = webdriver.Chrome()
        # driver.get('https://login-learn.k12.com/#dashboard')
        # time.sleep(1)
        time.sleep(5)
        schedule = driver.find_element(By.ID,'sidebar-nav').find_element(By.TAG_NAME,'li').find_element(By.TAG_NAME,'a')
        schedule.click()
        time.sleep(5)
        try:
            # classes = driver.find_element(By.CLASS_NAME,'enrollment-data-table').find_element(By.TAG_NAME,'table').find_element(By.TAG_NAME,'tbody').find_elements(By.TAG_NAME,'tr')
            classes = driver.find_element(By.XPATH,'//*[@id="components"]/div/div[2]/div/div[2]/div/div[3]/table/tbody').find_elements(By.TAG_NAME,'tr')
            # print (classes)
            for i in classes:
                required = i.find_element(By.XPATH,'.//td/a/span/span[1]/span[2]/span[2]').get_attribute('innerText')
                if (required == 'Required'):
                    class_time = i.find_element(By.XPATH,'.//td/a/span/span[2]/span').get_attribute('innerText')
                    class_time_a = time_conv(class_time.split(' - ')[0])
                    class_time_b = time_conv(class_time.split(' - ')[1])
                    time_now = int(datetime.now().strftime("%H%M"))
                    # print (f'class_time_a: {class_time_a}, class_time_b: {class_time_b}, time_now: {time_now}')
                    # print (time_now > class_time_a and time_now < class_time_b)
                    if (time_now > class_time_a and time_now < class_time_b):
                        # print ('go to class')
                        # chrome_options.arguments.remove("--headless")
                        # time.sleep(2)
                        # i.find_element(By.XPATH,'.//td/a').click()
                        chrome2_options = Options()
                        chrome2_options.add_experimental_option("detach", True)
                        chrome2_options.add_experimental_option("excludeSwitches", ['enable-automation']);
                        driver2 = webdriver.Chrome(chrome2_options)
                        class_url = i.find_element(By.XPATH,'.//td/a').get_attribute('data-url')
                        driver2.get(f'https://login.k12.com/{class_url}')
                        # already_in_class = True
                        time.sleep(10 * 60)
                        driver2.refresh()
                        time.sleep((class_time_b - class_time_a) * 60)
                        # print ((class_time_b - class_time_a) * 60)
                        # time.sleep(10)
                        driver2.close()
                        # already_in_class = False
                        # driver.maximize_window()i
                        # chrome_options.remove_argument("--headless")
                    else:
                        print ('no classes right now')
        except:
            print ('no find')

# Main function to call login and attend functions in sequence
def main():
    driver.get('https://login.k12.com/')
    time.sleep(5)
    email = 'gamundson'
    password = 'Oklahoma2022'

    try:
        #login_email_field = driver.find_element_by_id('okta-signin-username')
        login_email_field = driver.find_element(By.ID, 'okta-signin-username')
        # login_email_field.click()
        # pag.typewrite(email)
        login_email_field.send_keys(email)

        #login_pass_field = driver.find_element_by_id('okta-signin-password')
        login_pass_field = driver.find_element(By.ID, 'okta-signin-password')
        # login_pass_field.click()
        # pag.typewrite(password)
        #login_to_stride(email, password)
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


