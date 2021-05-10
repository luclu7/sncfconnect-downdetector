#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from influxdb import InfluxDBClient
from datetime import datetime

client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('sncf-connect')

now = datetime.now()

options = webdriver.FirefoxOptions()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)

driver.get("https://moncompte.sncf.com/prehome")
content = driver.find_element_by_css_selector(".login-account__header__title")
if content.text == "CONNECTEZ-VOUS":
    print(now.isoformat()+": UP")
    client.write_points(["status value=1"], database='sncf-connect', time_precision='ms', protocol='line')
else:
    print(now.isoformat()+": DOWN")
    client.write_points(["status value=0"], database='sncf-connect', time_precision='ms', protocol='line')

driver.close()
