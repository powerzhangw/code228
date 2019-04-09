# -*- coding: utf-8 -*-
# import uitls.browser
from selenium.webdriver.common.by import By
import uitls.startend
u = uitls.startend
class Title (u.PostlendTest):
    def closetitle(self):
        self.browser.click((By.CSS_SELECTOR,'.ivu-btn.ivu-btn-primary.ivu-btn-small'))
        self.browser.click((By.CSS_SELECTOR,'//button[text()="关闭所有"]'))
