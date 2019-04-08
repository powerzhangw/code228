# -*- coding: utf-8 -*-
import win32gui

import win32con

def upload_ chrome (fi lepath) :

      #一级窗口#
        # dialog = win32gui. FindWindow(' #32770",”打开")#二级窗口

      ComboBoxEx32 = win32gui. FindWindowEx (dialog, 0, "ComboBoxEx32", None)
        #三级窗口

      comboBox = win32gui. FindWindowEx (ComboBoxEx32, 0, "ComboBox", None)#四级窗口一文件路径输入框

      edit = win32gui. FindWindowEx (comboBox, 0,’Edit', None)#二级窗口一打开按钮

      button = win32gui. FindW indowEx (dialog, 0, "Button",”打开(&O) "”)#操作一#发送文件路径

      win32gui. SendMessage (edit, win32con. WM_ SETTEXT, None, filepath)#点击打开按钮

      win32gui. SendMessage (dialog, win32con. WM COMMAND, 1，but ton)

#指定要上传的文件路径

file_ path = "D:\\111. txt"upload_ chrome(file_ path)
