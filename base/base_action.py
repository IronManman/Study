from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
class BaseAction():
    def __init__(self,driver):
        self.driver=driver

    #找元素的二次封装方法
    def find_element(self,feature,timeout=5,poll=1):
        feature_by,feature_values=feature
        element=WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(feature_by,feature_values))
        return element

    #点击的二次封装
    def click(self,feature):
        self.find_element(feature).click()


