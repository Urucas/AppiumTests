import os
from time import sleep

import unittest
import argparse
import json
import re
import os

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class FlagSecure(unittest.TestCase):

    def setUp(self):
        desired_caps =  {
            "deviceName":"Android",
            "app" : PATH("./app-debug.apk"),
            "app-package":"com.urucas.appiumtests",
            "appWaitActivity": "com.urucas.appiumtests.activities.MainActivity",
            "browserName" : "",
            "platformName":"Android",
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

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
        
        self.driver.save_screenshot(PATH('./screen.png'))
        sleep(.5)
        size = os.stat(PATH('./screen.png')).st_size
        self.assertNotEqual(0, size)
        
        el = self.driver.find_element_by_id("secureBtt")
        el.click()
        sleep(.5)
        self.driver.save_screenshot(PATH('./screen_secure.png'))
        sleep(.5)
        size = os.stat(PATH('./screen_secure.png')).st_size
        self.assertEqual(0, size) 
        
        el = self.driver.find_element_by_id("insecureBtt")
        el.click()
        sleep(.5)
        self.driver.save_screenshot(PATH('./screen_insecure.png'))
        sleep(.5)
        size = os.stat(PATH('./screen_insecure.png')).st_size
        self.assertNotEqual(0, size)
        
        os.unlink(PATH('./screen.png'))
        os.unlink(PATH('./screen_secure.png'))
        os.unlink(PATH('./screen_insecure.png'))
          

if __name__ == '__main__':
    # run test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(FlagSecure)
    unittest.TextTestRunner(verbosity=2).run(suite)