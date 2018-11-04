import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self, driver):
        self.driver = driver
    # 查找元素方法 封装-->此方法给click、input等方法使用

    def base_find_element(self, loc, timeout=30, poll_frequency=0.5):
        """
            1. 封装查找元素的时候，记得使用 显示等待
            2. 使用driver.find_element(By.XPAHT,"....")
            3. 最后要通过return进行返回元素
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    # 点击方法 封装
    def base_click(self, loc):
        self.base_find_element(loc).click()

    # 输入方法 封装
    def base_send_keys(self, loc, text):
        # 输入方法：要先清除操作
        el = self.base_find_element(loc)
        # 清除操作
        el.clear()
        # 输入元素内容
        el.send_keys(text)

    # 截图方法 封装
    def base_get_screenshot(self):
        # 组合图片保存路径及文件名：
        img_path = os.getcwd()+os.sep+"Imags"+os.sep+"faild.png"
        # 注意：调用的时候使用的是pytest，一定要路径问题 建议使用 os.getcwd（）
        self.driver.get_screenshot_as_file(img_path)

    # 获取toast 封装
    def base_get_toast(self, message):
        msg = By.XPATH, "//*[contains(@text, '"+message+"')]"
        # 查找元素 方法 调用获取文本方法，并返回
        return self.base_find_element(msg, poll_frequency=0.1).text

    # 获取 文本信息 封装
    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    # 元素滑动 封装
    def base_drag_and_drop(self, el1, el2):

        self.driver.drag_and_drop(el1, el2)
