import time
from io import BytesIO

import cv2
import numpy as np
import requests
from PIL import Image
from selenium.webdriver import ActionChains
from Common.webkeys import WebKeys
from Common.common import path_file


class Common(WebKeys):
    def yzm(self):
        path = path_file()
        while 1:
            target = self.driver.find_element_by_class_name("yidun_bg-img")
            template = self.driver.find_element_by_class_name("yidun_jigsaw")
            target_link = target.get_attribute('src')
            template_link = template.get_attribute('src')
            target_img = Image.open(BytesIO(requests.get(target_link).content))
            template_img = Image.open(BytesIO(requests.get(template_link).content))
            target_img.save(path + '/Source/Image_yzm/target.jpg')  # 缺口图片
            template_img.save(path + '/Source/Image_yzm/template.png')  # 验证图片
            img_rgb = cv2.imread(path + '/Source/Image_yzm/target.jpg')
            img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
            template = cv2.imread(path + '/Source/Image_yzm/template.png', 0)
            run = 1
            res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
            # 使用二分法查找阈值的精确值
            L = 0
            R = 1
            while run < 20:
                run += 1
                threshold = (R + L) / 2
                if threshold < 0:
                    print('Error')
                    return None
                loc = np.where(res >= threshold)
                if len(loc[1]) > 1:
                    L += (R - L) / 2
                elif len(loc[1]) == 1:
                    result_value = loc[1][0]
                    break
                elif len(loc[1]) < 1:
                    R -= (R - L) / 2
            slider = self.driver.find_element_by_class_name("yidun_slider")
            action = ActionChains(self.driver)
            action.click_and_hold(slider).perform()
            action.move_by_offset(result_value + 10, 0).release().perform()
            time.sleep(1)
            try:
                self.driver.find_element_by_xpath('//*[contains(text(),"向右拖动滑块填充拼图")]').size == 0
            except:
                break
