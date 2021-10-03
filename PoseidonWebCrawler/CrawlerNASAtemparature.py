#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
[Cralwer NASA temparature]
https://www.ncdc.noaa.gov/cag/global/time-series/nhem/land_ocean/all/8/1880-2021
-land
-ocean
'''

#Notice: Please set your Download location as the same folder as default.

# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, os, shutil

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        #webdriver.Safari()
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        continents=['Northern Hemisphere','Southern Hemisphere','Africa','Asia','Europe','North America','Oceania','South America']
        driver = self.driver
        #clear it.
        if os.path.exists('data.csv'):
            os.remove('data.csv')
        
        #[Land]
        driver.get("https://www.ncdc.noaa.gov/cag/global/time-series/globe/land/all/8/1880-2021")
        driver.find_element_by_id("lat_band").click()
        for conti in continents:
            Select(driver.find_element_by_id("lat_band")).select_by_visible_text(conti)
            driver.find_element_by_id("submit").click()
            driver.find_element_by_id("monitoring-content").click()
            driver.find_element_by_xpath("//img[@alt='csv']").click()
            time.sleep(5)
            os.rename('data.csv', 'land_'+str(conti)+'.csv')
            time.sleep(2)
        time.sleep(3)
        
        #[Ocean]
        driver.get("https://www.ncdc.noaa.gov/cag/global/time-series/globe/ocean/all/8/1880-2021")
        driver.find_element_by_id("lat_band").click()
        for conti in continents:
            Select(driver.find_element_by_id("lat_band")).select_by_visible_text(conti)
            driver.find_element_by_id("submit").click()
            driver.find_element_by_id("monitoring-content").click()
            driver.find_element_by_xpath("//img[@alt='csv']").click()
            time.sleep(5)
            os.rename('data.csv', 'ocean_'+str(conti)+'.csv')
            time.sleep(2)
        time.sleep(3)

        os.makedirs( 'OriginalNASA_temparature', 0o777 )
        for conti in continents:
            shutil.move('land_'+str(conti)+'.csv', './OriginalNASA_temparature/land_'+str(conti)+'.csv')
            shutil.move('ocean_'+str(conti)+'.csv', './OriginalNASA_temparature/ocean_'+str(conti)+'.csv')

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
