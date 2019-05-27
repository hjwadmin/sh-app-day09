import allure
class Test_1:
    def test_add_png(self):
        with open("E:/rz_Web_Code/sh-app-day08/scripts/hh.png","rb") as f:
            allure.attach("截图",f.read(),allure.attach_type.PNG)