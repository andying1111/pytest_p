from pywinauto import Application, Desktop
from pywinauto.timings import WaitUntil
import pytest
from time import sleep
import os

filename = 'C:\wwj\python\study\PolyvDirectorSeleTest\test case\errorImage'

def capture_screenshot(window, filename):
    try:
        window.capture_as_image().save(filename)
    except Exception as e:
        print(f"Failed to capture screenshot: {e}")

@pytest.fixture(scope="module")
def app():
    # 启动轻导播客户端
    app = Application(backend='uia').start('C:\Program Files\PolyvDirector\PolyvDirector.exe')
    # 等待页面加载成功
    sleep(5)
    yield app
    # 关闭轻导播客户端
    app.kill()

def test_loginpass1(app):
    try:
        # 连接上轻导播窗口
        dlg = Desktop(backend="uia").window(title="Polyv 轻导播")
        # 输入频道和密码
        channel = dlg.child_window(title="请输入频道号")
        channel.set_text("3940621")
        password = dlg.child_window(title="请输入频道密码")
        password.set_text("111qqq")
        username = dlg.child_window(title="请输入昵称")
        username.set_text("二狗子")
        # 点击登录按钮
        login_btn = dlg.child_window(title="同意并登录")
        login_btn.click()
        # 等待加载页面成功
        # WaitUntil(30, 0.5, lambda: dlg['开始直播Button'].exists())
        sleep(20)
        # 检查登录是否成功
        assert dlg['开始直播Button'].exists()
    except Exception as e:
        # 在发生异常时截图
        filename = os.path.join(os.getcwd(), "test_loginpass1.png")
        capture_screenshot(app.window(), filename)
        raise
