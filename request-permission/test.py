import os
from time import sleep

import unittest
import argparse
import json
import re

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class RequestPermissionTests(unittest.TestCase):

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


    def test_request_permission(self):
        sleep(.5)
        contexts = self.driver.contexts
        el = self.driver.find_element_by_id("openRequestBtt")
        self.assertIsNotNone(el)
        el.click()
        sleep(.5)

        el = self.driver.find_element_by_id("requestBtt")
        self.assertIsNotNone(el)
        el.click()
        sleep(.3)

        # search for allow button
        el = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
        self.assertIsNotNone(el)
        el.click()
        sleep(.3)

        # check for new request permission state
        el = self.driver.find_element_by_id("stateTextView")
        self.assertIsNotNone(el)
        self.assertIn("granted", el.text)
        sleep(.3)

        # click request permission again
        el = self.driver.find_element_by_id("requestBtt")
        self.assertIsNotNone(el)
        el.click()
        sleep(.3)

        # search for deny button
        el = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_deny_button")
        self.assertIsNotNone(el)
        el.click()
        sleep(.5)

        # check for new request permission state
        el = self.driver.find_element_by_id("stateTextView")
        self.assertIsNotNone(el)
        self.assertIn("denied", el.text)
        sleep(.3)




if __name__ == '__main__':
    # run test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(RequestPermissionTests)
    unittest.TextTestRunner(verbosity=2).run(suite)


