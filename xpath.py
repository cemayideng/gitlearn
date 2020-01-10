'''xpath:
//*[@class='icon' and @id='add-new']
//div[@class='category-info']
//*[contains(text(),'医学类院系')]/../dl[2]//*[text()='更多>>']
//*[contains(text(),'医学类院系')]/..//*[text()='更多>>']
灵活，方式很多，最终目的让需要定位的元素 稳定，而且在页面是唯一的
'''
import  unittest
from selenium import webdriver
class Test(unittest.TestCase):
    def sub_setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://www.baidu.com')
        print('1')

    def sub_teardown(self):
        self.driver.quit()
        print(2)
    def test(self):
        with self.subTest():
            self.sub_setup()
            try:
                self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('111')
            except:
                raise ('111')
            print('3')
            self.sub_teardown()

if __name__=='__main__':
    unittest.main()
