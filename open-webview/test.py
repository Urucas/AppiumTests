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

class OpenWebViewTests(unittest.TestCase):

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


    def test_context_is_changed(self):
        sleep(.5)
        contexts = self.driver.contexts
        self.assertIsNotNone(contexts)

        self.assertEqual(contexts[0], "NATIVE_APP")
        el = self.driver.find_element_by_id("openWebviewBtt")
        self.assertIsNotNone(el)
        el.click()
        sleep(1.5)

        contexts = self.driver.contexts
        print contexts
        has_webview = False
        for i in range(0, len(contexts)):
            search = re.search('WEBVIEW', contexts[i])
            if search is not None:
                has_webview = True

        sleep(1.3)
        self.assertEquals(has_webview, True)
        self.driver.quit()


if __name__ == '__main__':
    # run test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(OpenWebViewTests)
    unittest.TextTestRunner(verbosity=2).run(suite)


