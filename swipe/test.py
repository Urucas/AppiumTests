impor os
from time import sleep

import unittest
import argparse
import json
import re

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import random

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SwipeTests(unittest.TestCase):

    def setUp(self):
        desired_caps =  {
            "deviceName":"Android",
            "app" : PATH("./App-debug.apk"),
            "app-package":"com.lal.focusprototype.app",
            "appWaitActivity": "com.lal.focusprototype.app.MainActivity",
            "browserName" : "",
            "platformName":"Android",
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def tearDown(self):
        # end the session
        self.driver.quit()


    def has_card(self):
        try:
            el = self.driver.find_element_by_id("cardStack")
            return el
        except:
            return None

    def test_swipe(self):
        sleep(1)

        size = self.driver.get_window_size()
        width = size["width"]
        start_x = int(width/2)
        start_y = int(size["height"]/2)

        sleep(.5)
        el = self.has_card()
        while el is not None:

            swipe_x = width-10
            if random.random() > 0.5:
                swipe_x = 10

            action = TouchAction(self.driver)
            action.press(x=start_x, y=start_y).wait(300).move_to(x=swipe_x,y=start_y).release()
            action.perform()
            sleep(.5)

            el = self.has_card()
            sleep(.5)

if __name__ == '__main__':
    # run test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(SwipeTests)
    unittest.TextTestRunner(verbosity=2).run(suite)


