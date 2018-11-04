import os
import sys
sys.path.append(os.getcwd())

import pytest
from Base.read_yaml import ReadYAML
import allure
from Page.page_in import PageIn


# 获取 yaml 数据
def get_data():
    arrs = []
    for data in ReadYAML("login_data.yml").read_yaml().values():
        arrs.append((data.get("username"), data.get("password"), data.get("expect_result"), data.get("expect_toast")))

    return arrs


class TestLogin():

    @allure.step("实例化 PageIn")
    def setup_class(self):
        # 实例化 PageIn
        self.page = PageIn()
        self.login = self.page.page_get_login()

        # 点击 我
        self.login.page_click_login_me()
        # 点击 已有账号，登录
        self.login.page_login_name_ok_link()

    @allure.step("关闭驱动")
    def teardown_class(self):
        # 关闭驱动
        allure.attach("关闭驱动", "")
        self.login.driver.quit()

    # 添加步骤描述
    @allure.step("开始执行测试登录脚本...")
    # 参数化
    @pytest.mark.parametrize("username,password,expect_result,expect_toast", get_data())
    def test_login(self, username, password, expect_result, expect_toast):
        # 登录 正向逆向逻辑问题
        # 正向登录
        if expect_result:
            try:
                # 输入用户名
                self.login.page_login_username(username)
                # 输入密码
                self.login.page_login_password(password)
                # 点击登录
                self.login.page_login_btn()
                # 获取昵称
                result_nick = self.login.page_login_nickname()
                #  断言
                assert expect_result in result_nick
                # 点击设置
                self.login.page_login_setting()
                # 滑动 从消息推送-->滑到-->修改密码
                self.login.page_drag_drop()
                # 点击 退出
                self.login.page_login_logout()
                # 确认 退出
                self.login.page_login_logout_ok()
                # 点击 我
                self.login.page_click_login_me()
                # 点击 已有账号，登录
                self.login.page_login_name_ok_link()

            except Exception:
                # 截图
                self.login.base_get_screenshot()
                # 失败图片写入报告
                with open("./Imags/faild.png", "rb") as f:
                    allure.attach("正向登录失败原因", f.read(), allure.attach_type_PNG)
                # 抛异常
                raise
        # 逆向登录
        else:
            try:
                # 输入用户名
                self.login.page_login_username(username)
                # 输入密码
                self.login.page_login_password(password)
                # 点击登录
                self.login.page_login_btn()
                # 获取 toast
                result_toast = self.login.base_get_toast(expect_toast)
                #  断言
                allure.attach("开始断言...", "")
                assert expect_toast in result_toast

            except Exception:
                # 截图
                self.login.base_get_screenshot()
                # 失败图片写入报告
                with open("./Imags/faild.png", "rb") as f:
                    allure.attach("逆向登录失败原因", f.read(), allure.attach_type_PNG)
                # 抛异常
                raise
