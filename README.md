<h1 align="center">
    <a href="https://github.com/NightFoxAnimation" target="_blank">
        <img src="/stuff/NightFox%20new%20circle.png" width="224px" alt="Gabriel Amundson">
            <br>
            Gabriel Amundson
            </a>
        </h1>
        <h4 align="center">Just some guy</h4>

# K12_AutoClasslogin
### A Python script automatically login to your k12 profile sees if the class is required or optional then joins if it is time

Go to the Releases Page on the right and click the K12_AutoClasslogin.zip file.

Extract the ZIP file where you want it to run. 

Navigate to the extracted folder.

Find the autologin.py file and open it in a notebook or your preferred Python editor.

Locate the following section of code: 

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

Replace 'YourUsername' with your K12 Username and 'YourPassword' with your password.

Save the file.

Go back to the extracted folder, right-click in the folder (not on the files), and select "Open in Terminal."

![](https://github.com/NightFoxAnimation/K12_AutoClasslogin/blob/main/stuff/expl%20(1).gif)

Paste and run the following command to install the required dependencies:

    pip install -r requirements.txt

After the installation is complete, navigate to the extracted folder, right-click, and create a new text document.

Name the file as you prefer, open it, and paste the following code:

    @echo off
    py autologin.py

Save the file. Go back to the folder, and change the file extension from .txt to .bat.

Right-click the new .bat document, select "Create Shortcut," and move the shortcut file to an easily accessible location, such as your desktop.

Double-click the shortcut, and it should run.


## Run Minimized:

Right-click on the shortcut you created.

Select "Properties."

In the "Run" dropdown, choose "Minimized."

Click "OK."


## Run at Startup:

Press Win + R to open the Run dialog.

Type shell:startup and press Enter. This opens the Startup folder.

Copy the shortcut file.

Paste the shortcut into the Startup folder.
