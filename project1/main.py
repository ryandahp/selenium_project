from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import telegram
import time

bot = telegram.Bot(token='1445857270:AAGzj_4Xjvl-YfkjOX4w4uZl0gBttR9F8iU')

#driver = webdriver.Firefox()
driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=DesiredCapabilities.FIREFOX)

driver.get("https://indodax.com/chart/USDTIDR")

a = ['1', '2', '3']
while True:
    if not a:
        a = ['1', '2', '3']
    b = a.pop(-1)
    image_name = "image_" + str(b) + ".png"
    driver.save_screenshot(image_name)
    bot.send_photo(chat_id='1059673471', photo=open(image_name, 'rb'))
    time.sleep(60)

