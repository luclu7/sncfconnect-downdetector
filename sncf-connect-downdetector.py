#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from influxdb import InfluxDBClient

client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('sncf-connect')


options = webdriver.FirefoxOptions()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)

driver.get("https://moncompte.sncf.com/prehome")
content = driver.find_element_by_css_selector(".login-account__header__title")
if content.text == "SERVICE INDISPONIBLE":
    print("c'est kc")
    client.write_points(["status value=false"], database='sncf-connect', time_precision='ms', protocol='line')
else:
    print("isoké")
    client.write_points(["status value=true"], database='sncf-connect', time_precision='ms', protocol='line')

driver.close()
