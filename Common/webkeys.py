# coding=utf-8
from Common.open_browser import Browser
from Common.read_config import ReadConfig
import time


class WebKeys(object):

    """
    open_browser：初始化打开浏览器
    get_url：打开被测地址url
    element_location：元素定位方法封装
    elements_location：多元素定位方法封装
    click_element：点击操作
    input_element：输入操作
    text_element：获取元素文本内容
    text_elements：获取多个元素文本内容
    """

    def open_browser(self, mode, version):
        if mode == 'windows':
            self.driver = Browser().windows_chrome_browser(version)
        if mode == 'docker':
            self.driver = Browser().docker_chrome_browser()
        self.driver.maximize_window()

    def get_url(self):
        url = ReadConfig().read_url()
        self.driver.get(url)
        self.driver.implicitly_wait(20)

    def element_location(self, location_type, location_value):
        el = None
        if location_type == 'id':
            el = self.driver.find_element_by_id(location_value)
        elif location_type == 'name':
            el = self.driver.find_element_by_name(location_value)
        elif location_type == 'class_name':
            el = self.driver.find_element_by_class_name(location_value)
        elif location_type == 'xpath':
            el = self.driver.find_element_by_xpath(location_value)
        elif location_type == 'css_selector':
            el = self.driver.find_element_by_css_selector(location_value)
        elif location_type == 'link_text':
            el = self.driver.find_element_by_link_text(location_value)
        elif location_type == 'tag_name':
            el = self.driver.find_element_by_tag_name(location_value)
        elif location_type == 'partial_link_text':
            el = self.driver.find_element_by_partial_link_text(location_value)
        if el is None:
            print("元素定位失败")
        else:
            return el

    def elements_location(self, location_type, location_value):
        els = None
        if location_type == 'xpath':
            els = self.driver.find_elements_by_xpath(location_value)
        elif location_type == 'css_selector':
            els = self.driver.find_elements_by_css_selector(location_value)
        if els is None:
            print("元素定位失败")
        else:
            return els

    def click_element(self,location_type,location_value):
        el = self.element_location(location_type,location_value)
        el.click()

    def input_element(self,location_type,location_value,input_value):
        el = self.element_location(location_type,location_value)
        el.send_keys(input_value)

    def text_element(self,location_type,location_value):
        el = self.element_location(location_type, location_value)
        return el.text

    def text_elements(self,location_type,location_value):
        els = []
        el = self.elements_location(location_type, location_value)
        for i in el:
            els.append(i.text)
        els = [str(i) for i in els]
        els = '\n'.join(els)
        return els
























