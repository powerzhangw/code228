#-*- coding: utf-8 -*-
from uitls import startend
from selenium.webdriver.common.by import By
from uitls.post_result import *
import os
import uitls.close_title


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
        self.browser.wait(2)
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
        log.info('发起受让成功')
        # 还款管理
        self.browser.wait(1)
        self.browser.click((By.ID,"tTopMenurepayment"))
        # 受让管理
        self.browser.click((By.ID,"tSideMenutransfer"))
        # 受让列表
        self.browser.click((By.ID,"tSideMenutransfertransfer-index"))
        # 订单搜索
        self.browser.input((By.NAME, "tInputFilter"), '{0}'.format(self.po))
        self.browser.kenter((By.NAME,"tInputFilter"))
        # 提交审批
        time.sleep(1)
        self.browser.click((By.XPATH,'//*[text()="提交审批"]'))
        # 点击清贷框
        self.browser.click((By.XPATH,'//*[text()="请选择"]'))
        time.sleep(1)
        self.browser.click((By.XPATH,'//li[text()="查封"]'))
        self.browser.input((By.XPATH,'//textarea[@placeholder="请输入审批意见"]'),"审批意见")
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
        self.browser.click((By.CSS_SELECTOR, ' tr:nth-child(1) > td:nth-child(14) > div'))
        self.browser.wait(2)
        # self.browser.click((By.CSS_SELECTOR, '.ivu-radio.ivu-radio-checked>span'))
        # self.browser.click((By.CSS_SELECTOR, ".ivu-radio.ivu-radio-checked"))
        self.browser.click((By.XPATH, "/html/body/div[7]/div[2]/div/div/div[2]/div[4]/form/div[1]/div/div/label[1]/span"))
        self.browser.click((By.NAME, 'tBtnTransferApprovalModalConfirm'))
        # 副总审批列表
        self.browser.wait(1)
        self.browser.click((By.ID, "tSideMenutransfertransfer-approval1"))
        # 订单搜索
        self.browser.input((By.NAME, "tInputFilter"), '{0}'.format(self.po))
        self.browser.kenter((By.NAME, "tInputFilter"))
        time.sleep(1)
        self.browser.click((By.CSS_SELECTOR, ' tr:nth-child(1) > td:nth-child(14) > div'))
        self.browser.wait(2)
        self.browser.click((By.XPATH, "/html/body/div[7]/div[2]/div/div/div[2]/div[5]/form/div[1]/div/div/label[1]/span"))
        self.browser.click((By.NAME, 'tBtnTransferApprovalModalConfirm'))
        # 总经理审批列表
        self.browser.wait(1)
        self.browser.click((By.ID, "tSideMenutransfertransfer-approval2"))
        # 订单搜索
        self.browser.input((By.NAME, "tInputFilter"), '{0}'.format(self.po))
        self.browser.kenter((By.NAME, "tInputFilter"))
        time.sleep(1)
        self.browser.click((By.CSS_SELECTOR, ' tr:nth-child(1) > td:nth-child(14) > div'))
        self.browser.wait(3)
        self.browser.click((By.XPATH, "/html/body/div[7]/div[2]/div/div/div[2]/div[5]/form/div[1]/div/div/label[1]/span"))
        self.browser.click((By.NAME, 'tBtnTransferApprovalModalConfirm'))
        # 受让确认列表
        self.browser.wait(1)
        self.browser.click((By.ID, "tSideMenutransfertransfer-ensure"))
        # 订单搜索
        self.browser.input((By.NAME, "tInputFilter"), '{0}'.format(self.po))
        self.browser.kenter((By.NAME, "tInputFilter"))
        time.sleep(1)
        self.browser.click((By.XPATH, '//a[text()="确认"]'))
        self.browser.wait(1)
        self.browser.click((By.NAME, 'tBtnTransferEnsureModalConfirm'))
        #历史受让列表
        self.browser.wait(1)
        self.browser.click((By.ID,'tSideMenutransfertransfer-history'))
        self.browser.input((By.NAME, "tInputFilter"), '{0}'.format(self.po))
        self.browser.kenter((By.NAME, "tInputFilter"))
        self.browser.wait(1)
        self.browser.click((By.XPATH, "//*[text()= '{0}']".format(self.po)))
        self.browser.wait(2)
        self.srstatus = self.browser.get_text((By.CSS_SELECTOR,'div.ivu-collapse-header > span'))
        log.info(self.srstatus)
        self.srstatusss = "完成受让"
        self.assertEqual(self.srstatus, self.srstatus)
        self.browser.wait(1)
        # 点击资方还款计划表
        self.browser.click((By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[3]/div/div[1]/div/div/div/div/div[3]'))
        self.browser.click((By.XPATH,'//div[text()="资方表"]'))
        self.a = self.browser.get_text((By.XPATH,'//span[text()="已回购"]'))
        log.info(self.a)
        self.b = "已回购"
        self.assertEqual(self.a, self.b)























