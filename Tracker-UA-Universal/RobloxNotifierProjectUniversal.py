#####################################################################################
#  Created by: Dhillon, Gurpreet
#  Project #1
#  Roblox limited price notifier
#
#  Description: The objective of this project is to retrieve the price of a given
#               roblox item and notify you by email when your price requirements are met.
#               This works best with collectibles as other items in catalog have constant
#               prices. If you are using this for personal use, you can modify the popup
#               to only ask for the url and price (Ex: give email, subject, and user agent
#               a default value).
#
#  Notes:       This program is intended to be run from the Pycharm IDE.
#  Date created: July 2020
#####################################################################################
import PySimpleGUI as sg
import smtplib
import time
import requests
from bs4 import BeautifulSoup

sg.theme('Green')
col = [     [sg.Text('WE WILL NOTIFY YOU WHEN PRICE IS LOWER THAN YOUR THE PRICE YOU ENTERED')],
            [sg.Text('Item URL'),  sg.InputText('',size=(25,1),key ='-page url-')],  #robloxurl
            [sg.Text('ENTER YOUR UPPER LIMIT')],
            [sg.Text('The Price'),  sg.InputText('',size=(25,1),key ='-boundary-')],  #price
            [sg.Text('PLEASE ENTER YOUR EMAIL')],
            [sg.Text('@EMAIL|'),  sg.InputText('',size=(25,1),key ='-email-')],    #email
            [sg.Text('PLEASE ENTER THE MESSAGE YOU WANT TO RECEIVE WHEN WE SEND YOU AN EMAIL')],
            [sg.Text('The msg-'),  sg.InputText('',size=(25,1), key ='-subject-')], #subject
            [sg.Text('FOR THE NEXT FIELD, PLEASE ENTER YOUR USER AGENT:')],
            [sg.Text('UsrAgent'),  sg.InputText('',size=(25,1), key ='-useragent-')],
            [sg.Button('Ok'), sg.Button('Cancel')]]

layout = [[sg.Column(col)]]

location = (1200, 0)
window = sg.Window('Roblox Collectible Item Notifier', location=location).Layout(layout)
event, values = window.read(close=True)
page_url = values['-page url-']
subject = values['-subject-']
boundary2 = int(values['-boundary-'])
email = values['-email-']
UAgent = str(values['-useragent-'])
window.close()






headers = {"User-Agent":  UAgent}
def check_price():
    page = requests.get(page_url, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    title = soup2.find("h2").get_text()
    price = soup2.find("span", {"class": "text-robux-lg wait-for-i18n-format-render"}).get_text()
    price = price.replace(' ', '')
    price = price.replace(',', '')
    converted_price = int(price)

    if converted_price < boundary2:
        send_mail()
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    #Enter email and password here, Ex: server.login('email@gmail.com','abc123')
    #I would suggest making a new email just for this and allow less secure apps to login
    server.login('', '')
    #subject = "Price Change"
    body = "Check link: " + page_url
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        # Enter the same email here
        '',
        email,
        msg
    )
    sg.theme('Green')
    event, values = sg.Window('',
                              [[sg.Text('ALERT! EMAIL HAS BEEN SENT!')],
                               [sg.Button('OK')]], location= (1200,0)).read(close=True)

    server.quit()
while True:
 if not (event == sg.WIN_CLOSED or event == 'Cancel'):
      check_price()
      break
 elif event == sg.WIN_CLOSED or event == 'Cancel':
      break


# After making the program work successfully by entering in the required components (as well as entering a fake email in the code), 
# you can convert this into a exe file. To do so, Open your terminal and locate the directory containing the py script and icon image. 
# Then download pyinstaller by running 'pip install pyinstaller'. 
# Afterwords, run this command: pyinstaller --onefile --windowed --icon=icon.ico RobloxNotifierProject.py
#
# Note: Make sure you are running this in the directory containing the py script and icon.ico image.
#       Once the command is ran successfully, you can ignore _pycache_ and the build file, the
#       exe file should be in the dist folder.



























