from appium import webdriver

def init_driver(no_reset=True):
    des_cap={}
    des_cap["PlatformName"]="Android"
    des_cap["PlatformVersion"]="10"
    des_cap["deviceName"]="1"
    des_cap["appPackage"]="com.tencent/wework"
    des_cap["appActivity"]=".login.controller.LoginWxAuthActivity"
    des_cap["automationName"]="Uiautomator2"
    des_cap["no_reset"]=no_reset
    driver=webdriver.Remote("http://127.0.01:4723/hub/wd",des_cap)

    return driver