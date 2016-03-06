import os
from time import sleep

import unittest
import argparse
import json
import re
import os
import subprocess

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class FlagSecure(unittest.TestCase):

    def setUp(self):
        keys_path = PATH("./keys.json")
        with open(keys_path) as data:
          keys = json.load(data)
        app_path = PATH("./app-debug.apk")
        result = subprocess.check_output(["sauce-uploader", 
          keys["user"], keys["accessKey"], app_path])
        response = json.loads(result)
        try:
          filename = response["filename"]
        except Exception, e:
          print e
          print result
          self.driver.quit()
       
        desired_caps =  {
            "deviceName": "Android Emulator",
            "host": "ondemand.saucelabs.com",
            "port": 80,
            "app" : "sauce-storage:%s" % filename,
            "username" : keys["user"],
            "accessKey": keys["accessKey"],
            "app-package":"com.urucas.appiumtests",
            "appWaitActivity": "com.urucas.appiumtests.activities.MainActivity",
            "browserName" : "",
            "platformName":"Android",
            "appium-version" : "1.4.7"
        }
        self.driver = webdriver.Remote("http://ondemand.saucelabs.com:80/wd/hub", desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_textview_is_reached(self):
        sleep(.5)
        contexts = self.driver.contexts
        self.assertIsNotNone(contexts)
        self.assertEqual(contexts[0], "NATIVE_APP")
        el = self.driver.find_element_by_id("openFlagBtt")
        self.assertIsNotNone(el)
        el.click()
        sleep(.5)
        
        el = self.driver.find_element_by_id("textView")
        self.assertIsNotNone(el)
        sleep(.5)
        
        el = self.driver.find_element_by_id("secureBtt")
        el.click()
        sleep(5)
        
        el = self.driver.find_element_by_id("textView")
        self.assertIsNotNone(el)
        sleep(1.5)
        
        # el = self.driver.find_element_by_id("insecureBtt")
        # el.click()
        sleep(5)
        

if __name__ == '__main__':
    # run test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(FlagSecure)
    unittest.TextTestRunner(verbosity=2).run(suite)