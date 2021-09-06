# coding=utf-8
from selenium import webdriver
from Common.read_config import ReadConfig
from Common.common import path_file


class Browser(object):

    """
    docker_chrome_browser：docker启动chrome
    windows_chrome_browser：windows启动chrome
    """

    def docker_chrome_browser(self):
        chrome_capabilities = {
            "browserName": "chrome",
            "version": "",
            "platform": "ANY",
            "javascriptEnabled": True,
        }
        chrome_ip = 'http://' + ReadConfig().read_docker() + '/wd/hub'
        browser = webdriver.Remote(command_executor=chrome_ip, desired_capabilities=chrome_capabilities)
        return browser

    def windows_chrome_browser(self, version):
        path = path_file()
        chrome_path = path + '/Source/' + 'chromedriver-' + version + '.exe'
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        browser = webdriver.Chrome(chrome_path, options=options)
        return browser





