import allure
class Test_1:
    def test_add_png(self):
        with open("./hh.png","rb") as f:
            allure.attach("截图",f.read(),allure.attach_type.PNG)