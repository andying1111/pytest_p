from pywinauto import Application,Desktop
from time import sleep
import os

# appdress = C:\Program Files\PolyvDirector\PolyvDirector.exe
# 启动轻导播客户端
app = Application(backend='uia').start('C:\Program Files\PolyvDirector\PolyvDirector.exe')
sleep(10)
print("a:",app)

# 连接上轻导播窗口
dlg = Desktop(backend="uia").window(title="Polyv 轻导播")
# 打印登录界面
dlg.print_control_identifiers()
print('打印登录界面成功')

# 输入错误账号
channel = dlg.child_window(title="请输入频道号")
channel.set_text("3940621")
password = dlg.child_window(title="请输入频道密码")
password.set_text("111qqq")
username = dlg.child_window(title="请输入昵称")
username.set_text("二狗子")

# 点击登录控件
login_btn = dlg.child_window( title="同意并登录")
login_btn.click()
sleep(15)

# # 打印登录后的界面
# dlg.print_control_identifiers()
print('打印登录后的界面成功')


# 关闭程序
# app.kill()

