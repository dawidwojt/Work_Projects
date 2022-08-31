# This code is a script that do invoice cancellation automatically.
# The invoice to cancellation may be specified by PPE number or client ID.
# Due to a fact that only one way can work at a time, PPE number option is commented out and scipt works with client ID.
# All that needs to be done is pasting client IDs (or PPE numbers) into a text file.

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


# Na podstawie numerów PPE
#ppe_numbers = []
# with open('ppe.txt','r') as f:
#    ppe_numbers = f.read().split()
#    print(ppe_numbers)


# for PPE in ppe_numbers:
#    driver = webdriver.Edge("C:/Users/wojtadaw/PycharmProjects/msedgedriver")
#    driver.get('http://website.pl:8081/sps-mdm/configuration/objects?_cid=CIDd3bcfd8d2a9b4d8a8ac2fdbaa1740dcd')
#    sleep(4)
#    data_od = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[4]/div/div[1]/div[1]/div[2]/div/div/div[2]/form/table[1]/tbody/tr[2]/td[2]/div/input')
#    data_od.click()
#    data_od.send_keys("2020-07-18")
#    numer_PPE = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[4]/div/div[1]/div[1]/div[2]/div/div/div[2]/form/table[1]/tbody/tr[4]/td[2]/div/input')
#    numer_PPE.send_keys(PPE)
#    odswiez = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[4]/div/div[1]/div[1]/div[2]/div/div/div[2]/form/table[1]/tbody/tr[9]/td[2]/a/div')
#    odswiez.click()
#    sleep(10)
#    odczyty = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[4]/div/div[1]/div[2]/div[2]/div/div/div/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/span[3]/a')
#    odczyty.click()
#    sleep(3)
#    billing = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[4]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div/div/div/div[3]/a[8]')
#    billing.click()
#    sleep(2)
#    wybrany_miesiac = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[4]/div/div[1]/div[7]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div[2]/table/tbody/tr[2]/td[1]/input')
#    wybrany_miesiac.click()
#    wyslij_billing = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[4]/div/div[1]/div[7]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/a[1]/div')
#    wyslij_billing.click()
#    sleep(1)
#    potwierdz_wyslij_billing=driver.find_element(By.XPATH,'/html/body/div[13]/div[3]/div/button[1]')
#    potwierdz_wyslij_billing.click()
#    sleep(5)
#    print(f"{PPE} udostępnione...")

# Na podstawie ID
id_numbers = []
with open('id.txt', 'r') as f:
    id_numbers = f.read().split()
    print(id_numbers)

for id in id_numbers:
    driver = webdriver.Edge("C:/Users/wojtadaw/PycharmProjects/msedgedriver")
    id_str = str(id)
    driver.get(
        f'http://website.pl:8081/sps-mdm/configuration/readingViewer?id={id_str}')
    sleep(4)
    billing = driver.find_element(By.XPATH,
                                  '/html/body/div[2]/div/div/div[4]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div/div/div/div[3]/a[8]')
    billing.click()
    sleep(2)
    wybrany_miesiac = driver.find_element(By.XPATH,
                                          '/html/body/div[2]/div/div/div[4]/div/div[1]/div[7]/div[2]/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div[2]/table/tbody/tr[2]/td[1]/input')
    wybrany_miesiac.click()
    wyslij_billing = driver.find_element(By.XPATH,
                                         '/html/body/div[2]/div/div/div[4]/div/div[1]/div[7]/div[2]/div/div[2]/div/div/div[2]/div[2]/div/a[1]/div')
    wyslij_billing.click()
    sleep(1)
    potwierdz_wyslij_billing = driver.find_element(
        By.XPATH, '/html/body/div[13]/div[3]/div/button[1]')
    potwierdz_wyslij_billing.click()
    sleep(5)
    print(f"{id} udostępnione...")
