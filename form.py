from selenium import webdriver
import time
import random

web = webdriver.Chrome()
for i in range(392):
    web.get('https://docs.google.com/forms/d/e/1FAIpQLSe2CXlpRxPlGN3dPPlz1dNeLtPo3SbdryahnW1TvVrgu_qIOA/viewform')
    time.sleep(0.0001)

    avg_mnthr = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div['+str(random.randint(1, 5))+']')
    avg_mnthr.click()
    dept = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div['+str(random.randint(1, 7))+']')
    dept.click()
    salary = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div['+str(random.randint(1, 3))+']')
    salary.click()

    last_evln = random.random()*0.9+0.1
    l_e = web.find_element('xpath' , '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    l_e.send_keys(str(last_evln)[:3])
    sat_l = random.random()*0.9+0.1
    s_l = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
    s_l.send_keys(str(sat_l)[:3])
    if(last_evln>0.4 ):
        status= web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[2]/div/span')
        status.click()
    else :
        status= web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[2]/div/span')
        status.click()

    tnr = random.randint(1, 7)
    nm = web.find_element('xpath' , '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')
    nm.send_keys(str(tnr)[:3])
    n_p =random.randint(1, 7)
    nam = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
    nam.send_keys(str(n_p)[:3])
    # time.sleep(100000)

    # submit = web.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    # submit.click()



