import allure
import Page
from Base.Base import Base


class PageLogin(Base):

    # 点击我的
    # allure.attach("点击 我的","")
    @allure.step("点击 我的")
    def page_click_login_me(self):
        self.base_click(Page.login_me)

    # 点击 已有账号登录
    @allure.step("点击 已有账号登录")
    def page_login_name_ok_link(self):
        self.base_click(Page.login_name_ok_link)

    # 输入用户名
    @allure.step("输入用户名")
    def page_login_username(self, username):
        allure.attach("输入用户名: %s" % username, "")
        self.base_send_keys(Page.login_username, username)

    # 输入密码
    @allure.step("输入密码")
    def page_login_password(self, password):
        allure.attach("输入密码: %s" % password, "")
        self.base_send_keys(Page.login_password, password)

    # 点击 登录
    @allure.step("点击 登录")
    def page_login_btn(self):
        self.base_click(Page.login_btn)

    # 获取昵称 断言
    @allure.step("开始断言...")
    def page_login_nickname(self):
        return self.base_get_text(Page.login_nickname)

    # 点击 设置
    @allure.step("点击 设置")
    def page_login_setting(self):
        self.base_click(Page.login_setting)

    # 滑动 消息推动 ———> 修改密码
    @allure.step("滑动 消息推动 ———> 修改密码")
    def page_drag_drop(self):
        # 定位 消息推动
        el1 = self.base_find_element(Page.login_msg_send)
        # 定位 修改密码
        el2 = self.base_find_element(Page.login_modify_pwd)
        # 滑动
        self.base_drag_and_drop(el1, el2)

    # 点击 退出按钮
    @allure.step("点击 退出按钮")
    def page_login_logout(self):
        self.base_click(Page.login_logout)

    # 确认 退出
    @allure.step("确认 退出")
    def page_login_logout_ok(self):
        self.base_click(Page.login_logout_ok)
