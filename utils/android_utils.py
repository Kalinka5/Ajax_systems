def android_get_desired_capabilities():
    # I used these capabilities to make tests on my device.
    # {
    #     "appium:autoGrantPermissions": true,
    #     "appium:automationName": "uiautomator2",
    #     "appium:newCommandTimeout": 500,
    #     "appium:noSign": true,
    #     "platformName": "Android",
    #     "appium:resetKeyboard": true,
    #     "appium:takesScreenshot": true,
    #     "appium:appPackage": "com.ajaxsystems",
    #     "appium:appActivity": "com.ajaxsystems.ui.activity.LauncherActivity"
    # }
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '10',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': '11bd127d',
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
    }
