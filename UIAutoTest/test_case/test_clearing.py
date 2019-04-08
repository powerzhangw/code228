# #coding=utf-8
# from uitls import startend
# from selenium.webdriver.common.by import By
# from uitls.post_result import *
#
#
# class TestClearing(startend.PostlendTest):
# #     '''详细信息-基本信息'''
#     def test001(self):
#         self.po = get_code()
#         # 点击客户管理
#         self.browser.click((By.ID, 'tTopMenucustomer'))
#         # 点击在贷客户
#         self.browser.click((By.XPATH, '//*[@id="tSideMenuloanList"]/span'))
#         # 订单搜索
#         self.browser.input((By.XPATH, '//input[@name="tInputFilter"]'),'{0}'.format(self.po))
#         self.browser.click((By.XPATH, '//*[text()=\"筛选\"]'))
#         self.browser.wait(2)
#         #发起清贷
#         self.browser.click((By.XPATH,'//*[@class="ivu-icon ivu-icon-edit"]'))
#         self.browser.wait(1)
#         self.browser.click((By.XPATH,'//ul[@class="ivu-dropdown-menu"]/li[3]/a'))
#         self.browser.wait(1)
#
#         #输入清贷日期 当天时间
#         self.browser.click((By.XPATH,'//*[@placeholder="清贷时间"]'))
#         self.browser.kenter((By.XPATH,'//*[@placeholder="清贷时间"]'))
#         self.browser.click((By.XPATH,'//*[@name="tBtnLoanListClearingConfirm"]'))
#         self.browser.wait(1)
#         self.browser.scroll_top(5)
#         # 确定提交
#         self.browser.click((By.NAME, 'tBtnLoanListTrialModalConfirm'))
#         self.browser.wait(2)
#         # 点击清贷管理
#         self.browser.click((By.XPATH,'//*[@id="tTopMenurepaymentRemoveLoan"]/span'))
#         self.browser.click((By.ID,'tTopMenurepaymentRemoveLoan'))
#         # 点击议定清贷
#         self.browser.click((By.ID,'tSideMenuremoveLoan'))
#         # 点击清贷列表
#         self.browser.click((By.ID, 'tSideMenuremoveLoanremoveLoan-list'))
#         self.browser.wait(1)
#         # 搜索清贷客户
#         self.browser.input((By.XPATH,'//input[@name="tInputFilter"]'),'{0}'.format(self.po))
#         self.browser.click((By.XPATH, '//*[text()=\"筛选\"]'))
#         self.browser.wait(2)
#         # 提交审批
#         self.browser.click((By.XPATH,'//*[text()="提交审批"]'))
#         self.browser.wait(1)
#         # 点击清贷框
#         self.browser.click((By.XPATH,'//*[text()="请选择"]'))
#         # 点击下拉框
#         self.browser.click((By.XPATH,'/html/body/div[7]/div[2]/div/div/div[2]/div/form/div[3]/div/div/div[2]/ul[2]/li[2]'))
#         # 输入议定清贷总额
#         self.browser.input((By.XPATH,'/html/body/div[7]/div[2]/div/div/div[2]/div/form/div[7]/div/div[1]/input'),'244143')
#         self.browser.click((By.XPATH,'/html/body/div[7]/div[2]/div/div/div[2]/div/form/div[7]/label'))
#         self.browser.wait(2)
#         self.browser.click((By.XPATH,'/html/body/div[7]/div[2]/div/div/div[2]/div/form/div[8]/div/div/span'))
#         self.browser.input((By.CSS_SELECTOR, 'input[placeholder="查找"]'), '张巍巍')
#         self.browser.kenter((By.CSS_SELECTOR, 'input[placeholder="查找"]'))
#         self.browser.wait(2)
#         # 点击张巍巍，选中
#         self.browser.wait(1)
#         self.browser.click((By.CSS_SELECTOR, '.ej-rc-modal-item'))
#         self.browser.click((By.NAME, "tBtnRepaymentAddMemberConfirm"))
#         self.browser.click((By.NAME, "tBtnRepaymentAddMemberConfirm"))
#         self.browser.wait(1)
#         self.browser.click((By.XPATH, '//button[@name="tBtnRemoveLoanListModalConfirm"]'))
#         self.browser.wait(2)
#         # 点击经理审批
#         self.browser.click((By.XPATH, '//*[@id="tSideMenuremoveLoanremoveLoan-approval"]/span'))
#         self.browser.input((By.XPATH,'//input[@name="tInputFilter"]'),'{0}'.format(self.po))
#         self.browser.kenter((By.XPATH, '//input[@name="tInputFilter"]'))
#         self.browser.wait(2)
#         self.browser.click((By.XPATH, '// *[text() = "审批"]'))
#         # 点击通过
#         self.browser.wait(1)
#         self.browser.click((By.XPATH, '/html/body/div[7]/div[2]/div/div/div[2]/div[4]/form/div[1]/div/div/label[1]/span'))
#         self.browser.click((By.XPATH, '//*[@name="tBtnRemoveLoanApprovalModalConfirm"]'))
#         self.browser.wait(1)
#         self.browser.click((By.XPATH, '//*[@id="tSideMenuremoveLoanReal"]/div/span'))
#         # 清贷列表
#
#
#
#
#
#
#
#
#
#
#
#
#         # self.browser.kenter((By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/form/div[1]/div/div/input'))
#         # # 点击审批
#         # self.browser.click((By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]/div/div[2]/table/tbody/tr/td[14]/div/div/a'))
#         # # browser.input((By.NAME, "tInputFilter"))
#         # browser.click((By.NAME, "tBtnFilter"))
#         # print("断点断点断点断点断点断点")
#
#
#
#
#
#
