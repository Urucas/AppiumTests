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

class OpenBrowserTests(unittest.TestCase):

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


    def has_tabs(self):
        tab = self.driver.find_elements_by_class_name("android.widget.TabWidget")
        if len(tab) == 0:
            return False
        return True

    def is_on_app_list(self):
        tab = self.driver.find_element_by_class_name("android.widget.TabWidget")
        if tab is None:
            return False

        els = tab.find_elements_by_class_name("android.widget.TextView")
        el = None
        for el in els:
            if el.get_attribute("text") == "Apps":
                break

        if el is None:
            return False

        if el.get_attribute("selected") == "true":
            return True

        return False


    def search_chrome_button(self):
        els = self.driver.find_elements_by_class_name("android.widget.TextView")
        el = None
        for el in els:
            if el.get_attribute("text") == "Chrome":
                return el

        return None


    def has_chrome_opened(self):
        els = self.driver.find_elements_by_class_name("android.widget.TextView")
        for el in els:
            if el.get_attribute("text") == "Chrome":
                return True
        return False

    def test_browser_is_opened(self):
        sleep(.5)
        contexts = self.driver.contexts
        self.assertIsNotNone(contexts)
        self.assertEqual(contexts[0], "NATIVE_APP")
        el = self.driver.find_element_by_id("openBrowserBtt")
        self.driver.save_screenshot(PATH('./screen.png'))
        self.assertIsNotNone(el)
        el.click()
        sleep(.5)
        el = self.driver.find_element_by_id("openBrowserBtt")
        self.assertIsNotNone(el)
        el.click()
        sleep(.3)

        # if the user has 2 browsers then we click on Chrome button
        el = self.search_chrome_button()
        if el is not None:
            el.click()

        # wait a bit for page to load
        sleep(5)

        # press home button
        self.driver.press_keycode(3)
        sleep(1)


        # press switch app button
        self.driver.press_keycode(187)
        sleep(1)

        # close chrome app
        size = self.driver.get_window_size()
        x = size["width"] - 100
        y = size["height"] - 300

        while self.has_chrome_opened():
            self.driver.swipe(x, y, 10, y, 600)
            sleep(.8)

        # close chrome app list
        self.driver.press_keycode(187)
        sleep(.1)

        # click on the launcher icon
        els = self.driver.find_elements_by_class_name("android.widget.TextView")
        el = None
        for el in els:
            if el.get_attribute("text") == "" or el.get_attribute("text") == "Apps":
                break

        self.assertIsNotNone(el)
        el.click()
        sleep(.5)

        if self.has_tabs():
            el = None
            while self.is_on_app_list():
                el = self.search_chrome_button()
                if el is not None:
                    break

                self.driver.swipe(x, y, 10, y, 600)
                sleep(.6)


        else:
            el = None
            for i in range(0,4):
                el = self.search_chrome_button()
                if el is not None:
                    break

                self.driver.swipe(x, y/2, 10, y/2, 600)
                sleep(.6)

        # click on chrome button
        self.assertIsNotNone(el)
        el.click()
        sleep(.3)

        contexts = self.driver.contexts
        print contexts
        has_webview = False
        for i in range(0, len(contexts)):
            search = re.search('WEBVIEW', contexts[i])
            if search is not None:
                has_webview = True

        self.assertEquals(has_webview, True)
        self.driver.quit()


if __name__ == '__main__':
    # run test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(OpenBrowserTests)
    unittest.TextTestRunner(verbosity=2).run(suite)


