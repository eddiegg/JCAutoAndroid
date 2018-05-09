from appium import webdriver
import unittest
import time
import subprocess

class testDemo(unittest.TestCase):


    def setUp(self):
        subprocess.Popen('appium',shell=False)
        time.sleep(10)
        self.desired_caps={
            'platformName': 'Android',
            'deviceName': 'c06dcad0',
            'appPackage':'io.appium.android.apis',
            'appActivity':'io.appium.android.apis.ApiDemos'
        }
        self.driver=webdriver.Remote('http://0.0.0.0:4723/wd/hub',self.desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_demo(self):
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='Preference']").click();
        time.sleep(1)
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='9. Switch']").click();

if __name__ == '__main__':
    unittest.main()