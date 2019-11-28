# -*- coding: utf-8 -
import os
import sys
import logging
from time import sleep
from common.logger import Log
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
log = Log()


class BaseView(object):

    def __init__(self, driver):
        self.driver = driver

    # 获取一个页面,参数为url
    def get(self, *loc):
        return self.driver.get(*loc)

    # 普通元素定位
    # by_id  find_element(By.id,'xxx')或find_element_by_id('')
    # by_name  find_element(By.name,'xxx')或find_element_by_name('')
    # by_xpath  find_element(By.xpath,'xxx')或find_element_by_xpath('')
    # by_class_name  find_element(By.className,'xxx')或find_element_by_class_name('')
    # by_link_text  find_element(By.linkText,'xxx')或find_element_by_link_text('')
    # by_partial_link_text  find_element(By.partialLinkText,'xxx')或find_element_by_partial_link_text('')
    # by_tag_name  find_element(By.tagName,'xxx')或find_element_by_tag_name('')
    # by_css_selector  find_element(By.cssSelector,'xxx')或find_element_by_css_selector('')
    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    # 元素定位返回一个数组list，一般用于判断元素是否存在
    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    # 获取屏幕大小
    def get_window_size(self):
        return self.driver.get_window_size()

    # 滑动屏幕
    def swipe(self, star_x, star_y, end_x, end_y, duration):
        return self.driver.swipe(star_x, star_y, end_x, end_y, duration)

    # 时间等待(隐形等待)
    def implicitly_wait(self, t):
        return self.driver.implicitly_wait(t)

    # 时间等待(显性等待)
    def web_driver_wait(self, t, s):
        # 由于不长使用,不再进行具体的封装
        # 每经过s秒就查看一次指定元素是否可见,如果操作ts薄超时异常
        return WebDriverWait(self.driver, t, s)  # 可以配合until或者until_not方法，再辅助以一些判断条件，就可以构成这样一个场景


class Common(BaseView):

    # ```````````````````````````````````app设备权限授权操作````````````````````````````````````
    # 手机gps权限
    device_gps_btn = (By.ID, 'com.android.packageinstaller:id/permission_allow_button')

    # 允许访问位置
    def check_device_gps_btn(self):
        log.info("===检查是否允许访问位置===")
        try:
            element = self.find_element(*self.device_gps_btn)
        except NoSuchElementException:
            log.info('不需要进行gps授权!')
        else:
            log.info('进行gps授权')
            element.click()

    # 手机短信权限
    device_message_btn = (By.ID, 'com.android.packageinstaller:id/permission_allow_button')

    # 允许访问短信
    def check_device_message_btn(self):
        log.info("===检查是否允许访问短信===")
        try:
            element = self.find_element(*self.device_message_btn)
        except NoSuchElementException:
            log.info('不需要进行短信授权!')
        else:
            log.info('进行短信授权')
            element.click()

    # 手机照片权限
    device_photo_btn = (By.ID, 'com.android.packageinstaller:id/permission_allow_button')

    # 允许访问照片
    def check_device_photo_btn(self):
        log.info("===检查是否允许访照片、媒体内容和文件权限===")
        try:
            element = self.find_element(*self.device_photo_btn)
        except NoSuchElementException:
            log.info('不需要进行照片授权!')
        else:
            log.info('进行照片授权')
            element.click()
            sleep(2)
            element.click()

    # 手机通讯录权限
    device_phone_btn = (By.ID, 'com.android.packageinstaller:id/permission_allow_button')

    # 允许通讯录短信
    def check_device_phone_book_btn(self):
        log.info("===检查是否允许访问通讯录权限===")
        try:
            element = self.find_element(*self.device_phone_btn)
        except NoSuchElementException:
            log.info('不需要进行通讯录授权!')
        else:
            log.info('进行通讯录授权')
            element.click()

    # 允许所有设备权限
    def check_device_permissions(self):
        # 允许访问位置
        self.check_device_gps_btn()
        # 允许照片短信
        self.check_device_photo_btn()
        # 允许通讯录短信
        self.check_device_phone_book_btn()

    # ```````````````````````````````````app设备滑屏操作操作````````````````````````````````````
    # 获取屏幕尺寸
    def get_screen_size(self):
        x = self.get_window_size()['width']
        y = self.get_window_size()['height']
        return x, y

    # 向下/下滑动操作的封闭,用于整个屏幕的滑动(自定义滑动次数)
    def device_screen_swipe(self, way, n):
        # 滑动方法
        size = self.get_screen_size()
        x1 = int(size[0] * 0.3)
        x2 = int(size[0] * 0.1)
        x3 = int(size[0] * 0.9)
        y1 = int(size[1] * 0.1)
        y2 = int(size[1] * 0.8)
        if way == 'up':
            for i in range(n):
                sleep(0.3)
                self.swipe(x1, y2, x1, y1, 1000)
            log.info('app屏幕,整体上滑' + str(n) + '次')
        elif way == 'down':
            for i in range(n):
                sleep(0.3)
                self.swipe(x1, y1, x1, y2, 1000)
            log.info('app屏幕,整体下滑' + str(n) + '次')
        elif way == 'left':
            for i in range(n):
                sleep(0.3)
                self.swipe(x3, y1, x2, y1, 1000)
            log.info('app屏幕,整体左滑' + str(n) + '次')
        elif way == 'right':
            for i in range(n):
                sleep(0.3)
                self.swipe(x2, y1, x3, y1, 1000)
            log.info('app屏幕,整体右滑' + str(n) + '次')
        else:
            print('way参数错误')
        # 等待2s使滑动结束
        sleep(0.5)

    # 向下滑动操作的封闭, 用于选择日期插件操作（年-月-日）
    def device_date_swipe(self, way, n):
        size = self.get_screen_size()
        x1 = int(size[0] * 0.3)
        y1 = int(size[1] * 0.715)
        y2 = int(size[1] * 0.8)
        if way == 'up':
            for i in range(n):
                sleep(0.3)
                self.swipe(x1, y2, x1, y1, 1000)
            log.info('app日期插件,上滑' + str(n) + '次')
        elif way == 'down':
            for i in range(n):
                sleep(0.3)
                self.swipe(x1, y1, x1, y2, 1000)
            log.info('app日期插件,下滑' + str(n) + '次')
        self.swipe(x1, y1, x1, y2, 1000)
        # 等待0.5s使滑动结束
        sleep(0.5)

    # 滑动选择页面元素
    # occupation_type = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/'
    #                              'android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
    #                              'android.widget.FrameLayout/android.view.View[2]/android.view.View/'
    #                              'android.view.View[2]/android.widget.ScrollView/android.view.View/android.view.View')
    # class_type = (By.CLASS_NAME, 'android.widget.ScrollView')
    # class2_type = (By.CLASS_NAME, 'android.view.View')
    # class3_type = (By.CLASS_NAME, 'android.widget.TextView')

    # 下拉选项滑动
    # def down_option(self):
    #     self.find_element(*self.occupation_type).click()   # 有时候可能用上
    #     sleep(1)
    #     self.swipe_up2()
    #     self.swipe(689, 1070, 697, 1025, 1000)
    #     self.find_element(*self.ok_type).click()

    # # 长按滑动（用于借款协议页面）
    # def device_screen_slide(self):
    #     size = self.get_screen_size()
    #     action1 = TouchAction(self.driver).long_press(x=size[0] * 0.5, y=size[1] * 0.7).wait(1000).move_to(
    #         x=size[0] * 0.5, y=size[1] * 0.2).wait(1000).release()
    #     action1.perform()

    # ```````````````````````````````````app设备自带程序元素操作````````````````````````````````````
    # 相机元素(拍照按钮)
    device_photo_graph_type = (By.ID, 'com.android.camera2:id/shutter_button')
    # 相机元素(完成拍照按钮)
    device_photo_affirm_type = (By.ID, 'com.android.camera2:id/done_button')

    # 拍照功能
    def click_device_photo_graph_action(self):
        self.find_element(*self.device_photo_graph_type).click()
        self.find_element(*self.device_photo_affirm_type).click()

    device_phone_book_list_type = (By.ID, 'android:id/list')
    device_phone_book_list2_type = (By.CLASS_NAME, 'android.view.ViewGroup')
    device_phone_book_list3_type = (By.ID, 'com.android.contacts:id/cliv_data_view')

    # 选择通讯中的联系人
    def click_device_phone_book_action(self, n):
        device_phone_book_type = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/'
                                            'android.widget.FrameLayout[2]/android.widget.FrameLayout/'
                                            'android.widget.LinearLayout/android.widget.FrameLayout/'
                                            'android.widget.ListView/android.view.ViewGroup[' + str(n) + ']')

        # 因为contact_type中不能小于0所以使用是n要求大于0
        if n < 1:
            print('n不能小于0')
        else:
            try:
                self.find_element(*device_phone_book_type)
            except NoSuchElementException:
                self.find_element(*self.device_phone_book_list_type).find_elements(
                    *self.device_phone_book_list2_type)[n].find_element(*self.device_phone_book_list3_type).click()
            else:
                self.find_element(*device_phone_book_type).click()

    # app日期插件元素
    # picker_type = (By.ID, 'android:id/pickers')
    # picker2_type = (By.CLASS_NAME, 'android.widget.NumberPicker')
    # picker3_type = (By.CLASS_NAME, 'android.widget.Button')
    # 日期插件的确认按钮
    device_date_affirm_type = (By.ID, 'android:id/button1')
    device_date_yes_type = (By.ID, 'android:id/date_picker_year')

    # 日期插件操作（年-月-日）
    # def long_press(self):
    #     self.find_element(*self.yes_type).click()  # 有时候可能用上
    #     sleep(1)
    #     # 滑动选择年
    #     for i in range(3):
    #         self.swipe_down3()
    #         self.swipe(501, 557, 501, 950, 1100)
    #     # 长按选择年（年-月-日）    ---最的版本的app换了插件，所以用不上这个方法
    #     action=TouchAction(self.driver)
    #     # 长按元元素，duration是按住的持续时间，默认1000，单位是毫秒      ---最的版本的app换了插件，所以用不上这个方法
    #     action.long_press(ele,duration=1500).wait(1000).perform()
    #     self.find_element(*self.button_type).click()

    device_date_year_header_type = (By.ID, 'android:id/date_picker_header_year')
    device_date_type = (By.ID, 'android:id/date_picker_header_date')
    device_date_year_type = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/'
                                       'android.widget.FrameLayout/android.widget.LinearLayout/'
                                       'android.widget.FrameLayout/android.widget.FrameLayout/'
                                       'android.widget.DatePicker/android.widget.LinearLayout/'
                                       'android.widget.ViewAnimator/android.widget.ListView/android.widget.TextView[1]')
    device_date_year1_type = (By.ID, 'android:id/text1')

    # 日期插件选择(目前只选择年)
    def click_device_date_action(self, n):
        self.find_element(*self.device_date_year_header_type).click()
        sleep(2)
        self.device_date_swipe('down', n)
        sleep(2)
        try:
            self.find_element(*self.device_date_year_type)
        except NoSuchElementException:
            self.find_element(*self.device_date_year1_type).click()
            self.find_element(*self.device_date_affirm_type).click()
        else:
            self.find_element(*self.device_date_year_type).click()
            self.find_element(*self.device_date_affirm_type).click()

    # ```````````````````````````````````web常用操作````````````````````````````````````
    # 浏览器窗口切换
    def switch_tab(self, num):
        driver = self.driver
        handles = driver.window_handles  # 获取当前窗口句柄集合（列表类型）
        driver.switch_to.window(handles[num - 1])  # 跳转到第num个窗口

    # ```````````````````````````````````通用方法封装````````````````````````````````````
    # 禁止结果打印
    def block_print(self):
        sys.stdout = open(os.devnull, 'w')

    # 继续结果打印
    def enable_print(self):
        sys.stdout = sys.__stdout__

    # 检查元素是否存在
    def check_element_exist(self, a):
        if self.find_elements(*a) == []:
            return False
        else:
            return True

    # ````````````````app`````````````````
    # 屏幕滑动,至某元素出现
    def device_screen_swipe_custom(self, way, element_a):
        if way == 'up':
            while self.find_elements(*element_a) == []:
                self.device_screen_swipe('up', 1)
                if self.find_elements(*element_a) != []:
                    break
        elif way == 'down':
            while self.find_elements(*element_a) == []:
                self.device_screen_swipe('down', 1)
                if self.find_elements(*element_a) != []:
                    break
        elif way == 'left':
            while self.find_elements(*element_a) == []:
                self.device_screen_swipe('left', 1)
                if self.find_elements(*element_a) != []:
                    break
        elif way == 'right':
            while self.find_elements(*element_a) == []:
                self.device_screen_swipe('right', 1)
                if self.find_elements(*element_a) != []:
                    break

    # 点击错误重试,该方法只会循环一次
    def click_error_retry(self, exist, element_a, element_b):
        # 如果a元素不存在,就再次点击b元素
        if exist == 'nonexistence':
            try:
                self.find_element(*element_a)
            except NoSuchElementException:
                self.find_element(*element_b).click()
            else:
                pass
        # 如果a元素存在,就再次点击b元素
        elif exist == 'existence':
            try:
                self.find_element(*element_a)
            except NoSuchElementException:
                pass
            else:
                self.find_element(*element_b).click()
        else:
            print('参数错误')

    # 点击错误重试,添加权限判断
    def click_error_retry_permissions(self, exist, element_a, element_b):
        # 如果a元素不存在,就再次点击b元素
        if exist == 'nonexistence':
            try:
                self.find_element(*element_a)
            except NoSuchElementException:
                self.find_element(*element_b).click()
                # 为预防有些点击会触发权限问题,进行检查处理
                device_btn = (By.ID, 'com.android.packageinstaller:id/permission_allow_button')
                self.click_error_retry('existence', device_btn, device_btn)
                self.click_error_retry('existence', device_btn, device_btn)
            else:
                pass
        # 如果a元素存在,就再次点击b元素
        elif exist == 'existence':
            try:
                self.find_element(*element_a)
            except NoSuchElementException:
                pass
            else:
                self.find_element(*element_b).click()
                # 为预防有些点击会触发权限问题,进行检查处理
                device_btn = (By.ID, 'com.android.packageinstaller:id/permission_allow_button')
                self.click_error_retry('existence', device_btn, device_btn)
                self.click_error_retry('existence', device_btn, device_btn)
        else:
            print('参数错误')

    # 点击错误重试,该方法会循环一直点击,直到出现指定元素终止循环
    def click_error_cycle_retry(self, exist, element_a, element_b, element_c):
        # 如果a元素不存在,就循环点击b元素,直至检查存在c元素终止循环
        if exist == 'nonexistence':
            while self.find_elements(*element_a) == []:
                self.find_element(*element_b).click()
                # 如果检查出现c元素,就终止循环
                if self.find_elements(*element_c) != []:
                    break
        # 如果a元素存在,就循环点击b元素,直至检查存在c元素终止循环
        elif exist == 'existence':
            while self.find_elements(*element_a) != []:
                self.find_element(*element_b).click()
                # 如果检查出现c元素,就终止循环
                if self.find_elements(*element_c) != []:
                    break
        else:
            print('参数错误')

    # ````````````````web`````````````````
    # 鼠标移动至指定位置
    def mouse_moves(self, element):
        ActionChains(self.driver).move_to_element(self.find_element(*element)).perform()

    # 模拟键盘操作
    def keyboard(self, key, n):
        ac = ActionChains(self.driver)
        if key == 'up':
            for i in range(n):
                ac.send_keys(Keys.ARROW_UP)
        elif key == 'down':
            for i in range(n):
                ac.send_keys(Keys.ARROW_DOWN)
        elif key == 'left':
            for i in range(n):
                ac.send_keys(Keys.ARROW_LEFT)
        elif key == 'right':
            for i in range(n):
                ac.send_keys(Keys.ARROW_RIGHT)
        elif key == 'enter':
            for i in range(n):
                ac.send_keys(Keys.ENTER)
        elif key == 'backspace':
            for i in range(n):
                ac.send_keys(Keys.BACKSPACE)
        elif key == 'tab':
            for i in range(n):
                ac.send_keys(Keys.TAB)
        elif key == 'space':
            for i in range(n):
                ac.send_keys(Keys.SPACE)
        elif key == 'f5':
            for i in range(n):
                ac.send_keys(Keys.F5)
        elif key == 'ctrl+t':
            for i in range(n):
                ac.send_keys(Keys.CONTROL + 'T')
        ac.perform()

    # 下拉框select表单
    def select(self, way, element, *param):
        select = Select(self.find_element(*element))
        value = param[0]
        if way == 'index':
            select.select_by_index(value)  # 索引,从0开始(1)
        elif way == 'value':
            select.select_by_value(value)  # option标签的一个属性值,并不是显示在下拉框的值("0")
        elif way == 'text':
            select.select_by_visible_text(value)  # option标签文本的值,是显示在下拉框的值(n"xxx")
