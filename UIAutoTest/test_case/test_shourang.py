#-*- coding: utf-8 -*-
from uitls import startend
from selenium.webdriver.common.by import By
from uitls.post_result import *
import os


class TestShourang(startend.PostlendTest):
#     '''详细信息-基本信息'''
    def test002(self):
        self.po = get_code()
        self.browser.click((By.ID, 'tTopMenucustomer'))
        # 点击在贷客户
        self.browser.click((By.ID, "tSideMenuloanList"))
        # 订单搜索
        self.browser.input((By.NAME, "tInputFilter"),'{0}'.format(self.po))
        self.browser.click((By.XPATH, '//*[text()=\"筛选\"]'))
        self.browser.wait(1)
        # 发起受让
        self.browser.click((By.XPATH, '//*[@class="ivu-icon ivu-icon-edit"]'))
        self.browser.wait(1)
        self.browser.click((By.XPATH, '//ul[@class="ivu-dropdown-menu"]/li[2]/a'))
        self.browser.input((By.XPATH,'/html/body/div[8]/div[2]/div/div/div[2]/div/form/div[3]/div/div[1]/input'),'100000')
        self.browser.wait(1)
        self.browser.click((By.XPATH,'//input[ @placeholder="年-月-日"]'))
        self.browser.kenter((By.XPATH,'//input[ @placeholder="年-月-日"]'))
        self.browser.wait(1)
        self.browser.Ktab((By.XPATH,'//input[ @placeholder="年-月-日"]'))
        self.browser.kenter((By.XPATH, '//input[ @placeholder="时：分"]'))
        self.browser.click((By.CSS_SELECTOR,'button[name="tBtnLoanListTransferModalConfirm"]>span'))
        self.browser.click((By.CSS_SELECTOR,'button[name="tBtnLoanListTransferModalConfirm"]>span'))
        self.browser.wait(1)
        # 还款管理
        self.browser.wait(1)
        self.browser.click((By.ID,"tTopMenurepayment"))
        # 受让管理
        self.browser.click((By.ID,"tSideMenutransfer"))
        # 受让列表
        self.browser.click((By.ID,"tSideMenutransfertransfer-index"))
        # 订单搜索
        self.browser.input((By.NAME, "tInputFilter"), '{0}'.format(self.po))
        # 提交审批
        self.browser.click((By.XPATH,'//*[text()="提交审批"]'))
        # 点击清贷框
        self.browser.click((By.XPATH,'//*[text()="请选择"]'))
        time.sleep(1)
        self.browser.click((By.XPATH,'//li[text()="查封"]'))
        self.browser.input((By.XPATH,'//textarea[@placeholder="请输入审批意见"]'),"审批意见")
        # C:\Users\Administrator\Desktop\测试图\企鹅01
        # self.browser.input((By.XPATH,'/html/body),'100000')
        self.browser.click((By.CSS_SELECTOR,'.ivu-icon.ivu-icon-camera'))
        os.system(r"F:\upfile.exe")
        self.browser.wait(1)
        self.browser.click((By.XPATH,'//span[text()="选择总监审批人"]'))
        self.browser.wait(1)
        self.browser.input((By.CSS_SELECTOR, 'input[placeholder="查找"]'), '张巍巍')
        self.browser.kenter((By.CSS_SELECTOR,'input[placeholder="查找"]'))
        self.browser.wait(2)
        # 点击张巍巍选中
        # self.browser.wait(1)
        self.browser.click((By.CSS_SELECTOR, '.ej-rc-modal-item'))
        self.browser.click((By.NAME,"tBtnRepaymentAddMemberConfirm"))
        self.browser.click((By.NAME,"tBtnRepaymentAddMemberConfirm"))
        # 选择副总审批人
        self.browser.wait(2)
        self.browser.click((By.XPATH,'//span[text()="选择副总审批人"]'))
        self.browser.wait(1)
        self.browser.input((By.CSS_SELECTOR, 'input[placeholder="查找"]'), '张巍巍')
        self.browser.kenter((By.CSS_SELECTOR,'input[placeholder="查找"]'))
        self.browser.wait(2)
        self.browser.click((By.CSS_SELECTOR, '.ej-rc-modal-item'))
        self.browser.click((By.NAME,"tBtnRepaymentAddMemberConfirm"))
        self.browser.click((By.NAME,"tBtnRepaymentAddMemberConfirm"))
        # 选择总经理审批人
        self.browser.wait(2)
        self.browser.click((By.XPATH,'//span[text()="选择总经理审批人"]'))
        self.browser.wait(1)
        self.browser.input((By.CSS_SELECTOR, 'input[placeholder="查找"]'), '张巍巍')
        self.browser.kenter((By.CSS_SELECTOR,'input[placeholder="查找"]'))
        self.browser.wait(2)
        self.browser.click((By.CSS_SELECTOR, '.ej-rc-modal-item'))
        self.browser.click((By.NAME,"tBtnRepaymentAddMemberConfirm"))
        self.browser.click((By.NAME,"tBtnRepaymentAddMemberConfirm"))
        # tBtnTransferListConfirm
        self.browser.wait(1)
        # self.browser.click((By.NAME, "tBtnTransferListConfirm"))
        self.browser.click((By.NAME, "tBtnTransferListConfirm"))
        # 总监审批列表
        self.browser.wait(1)
        self.browser.click((By.ID, "tSideMenutransfertransfer-approval"))
        # 订单搜索
        self.browser.input((By.NAME, "tInputFilter"), '{0}'.format(self.po))
        self.browser.click((By.XPATH, '//a[text()="审批"]'))
        self.browser.wait(2)
        # self.browser.click((By.CSS_SELECTOR, '.ivu-radio.ivu-radio-checked>span'))
        # self.browser.click((By.CSS_SELECTOR, ".ivu-radio.ivu-radio-checked"))
        self.browser.click((By.XPATH, "/html/body/div[7]/div[2]/div/div/div[2]/div[4]/form/div[1]/div/div/label[1]/span"))
        self.browser.click((By.NAME, 'tBtnTransferApprovalModalConfirm'))















