import glob
import random
import time

import pymysql
import requests
from lxml import etree
from selenium import webdriver

base_url = 'https://www.9gexing.com/hongse/'
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


class A:
    def __init__(self):
        self.a1 = 1
        self.a2 = 2
        self.a3 = 3

    def fun(self):
        self.a4 = 4
        for i in range(1, 4):
            exec('print(self.a{})'.format(i))
            #eval()

    """if __name__ == '__main__':
        fun()"""


a = A()
a.fun()
print(a.a4)

"""a1 = 1
a2 = 2
a3 = 3
for i in range(1, 4):
    exec('print(a{})'.format(i))"""
"""x = 1
y ='yyy'
a = 'if x>0:' \
    'print(y)'
print(a)
exec(a)"""
"""b = "print(i-1)"
for i in range(1, 23):
    eval(a)
    exec(a)"""
# eval(a + b)
"""label = ''
if label == '':
    print('yyy')
print(label)"""
"""label = []
label.append('1')
label.append('2')
label.append('3')
label.append('4')
print(label)
print(label[1])
print(str(label))"""
"""db = pymysql.connect(host='localhost', user='root', password='123', db='recomm')
cursor = db.cursor()
sql = '''
update `{}` set `{}`='{}' where title='{}'
'''.format('ttt_t1', 'label', '你好', 'dsadas')
try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e)
finally:
    cursor.close()
    db.close()"""
"""db = pymysql.connect(host='localhost', user='root', password='123', db='recomm')
cursor = db.cursor()
sql = '''
select title from {}
'''.format('hotstory_test01')
cursor.execute(sql)
#print(str(cursor.fetchall()[0][0]))
print(cursor.fetchmany(3))
cursor.close()
db.close()"""

"""from PyQt5.Qt import *
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QListWidgetItem, QHBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("测试")
        self.resize(500, 750)
        self.move(500, 0)
        self.set()

    def set(self):
        list1 = ['python', 'java', 'c++']
        self.q1 = QLineEdit(self)
        self.q1.setPlaceholderText("试试看")
        self.q1.move(100, 100)

        self.cb = QComboBox(self)
        self.cb.addItems(list1)
        self.cb.move(300, 300)
        self.cb.currentIndexChanged.connect(self.cmb)

        list2 = ['1', '2', '3']
        self.qtb = QTableWidget(self)
        self.qtb.move(0, 300)
        self.qtb.setRowCount(5)
        self.qtb.setColumnCount(3)
        self.qtb.setHorizontalHeaderLabels(list2)
        self.qtb.setItem(0, 0, QTableWidgetItem('a'))

        self.cb2 = QCheckBox('看，飞机', self)
        self.cb2.move(400, 400)
        self.cb3 = QCheckBox('看，大炮', self)
        self.cb3.move(400, 450)

        btn1 = QPushButton(self)
        btn1.setText("点点看")
        btn1.move(200, 200)
        btn1.clicked.connect(self.btn)

        btn2 = QPushButton(self)
        btn2.setText('看啊')
        btn2.move(350, 350)
        btn2.clicked.connect(self.btn2)

    def btn2(self):
        a = self.cb3.isChecked()
        b = self.cb2.isChecked()
        print(a)
        if b == True and a == False:
            QMessageBox.information(self, '哪呢哪呢', self.cb2.text() + '在天上')
        if b == False and a == True:
            QMessageBox.information(self, '哪呢哪呢', self.cb3.text() + '在地上')
        if b == True and a == True:
            QMessageBox.information(self, '哪呢哪呢', '到底看哪啊')
        if b == False and a == False:
            QMessageBox.information(self, '哪呢哪呢', '看啥啊')

    def cmb(self):
        QMessageBox.information(self, 'cmb', '干tmd' + self.cb.currentText(), QMessageBox.Yes | QMessageBox.No)

    def btn(self):
        QMessageBox.information(self, '啊哈', self.q1.text(), QMessageBox.Yes | QMessageBox.No)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())"""

"""import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class QCheckBoxDemo(QWidget):
    def __init__(self):
        super(QCheckBoxDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('复选框控件演示')

        layout = QHBoxLayout()

        self.checkBox1 = QCheckBox('复选框控件1')
        self.checkBox1.setChecked(True)
        self.checkBox1.stateChanged.connect(lambda:self.checkboxState(self.checkBox1))
        layout.addWidget(self.checkBox1)

        self.checkBox2 = QCheckBox('复选框控件2')
        self.checkBox2.stateChanged.connect(lambda:self.checkboxState(self.checkBox2))
        layout.addWidget(self.checkBox2)

        self.checkBox3 = QCheckBox('半选中')
        self.checkBox3.stateChanged.connect(lambda:self.checkboxState(self.checkBox3))
        self.checkBox3.setTristate(True)
        self.checkBox3.setCheckState(Qt.PartiallyChecked)
        layout.addWidget(self.checkBox3)

        self.setLayout(layout)

    def checkboxState(self,cb):
        check1Status = self.checkBox1.text() + ', isChecked=' + str(self.checkBox1.isChecked()) + ',checkState=' + str(self.checkBox1.checkState()) + '\n'
        check2Status = self.checkBox2.text() + ', isChecked=' + str(self.checkBox2.isChecked()) + ',checkState=' + str(self.checkBox2.checkState()) + '\n'
        check3Status = self.checkBox3.text() + ', isChecked=' + str(self.checkBox3.isChecked()) + ',checkState=' + str(self.checkBox3.checkState()) + '\n'
        print(check1Status + check2Status + check3Status)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QCheckBoxDemo()
    main.show()
    sys.exit(app.exec_())"""
"""db = pymysql.connect(host='localhost', user='root', password='123', db='recomm')
cursor = db.cursor()
tablename = 'ttt_t1'
sql = '''
insert into {}(title,url,brief,detail) values('{}','{}','{}','{}')
'''.format(tablename, 'dsadas', 'dasdasda', 'dsadas', 'dwadsdsadasfwqeqweqw')
try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e)
finally:
    cursor.close()
    db.close()"""

"""db = pymysql.connect(host='localhost', user='root', password='123', db='recomm')
cursor = db.cursor()
tablename = 'ttt_t1'
sql = '''
   CREATE TABLE `{}`(
           `title` varchar(255) NOT NULL,
           `url` varchar(255) NOT NULL,
           `brief` varchar(255) NOT NULL,
           `detail` text(65530) DEFAULT NULL,
           `label` varchar(255) DEFAULT NULL,
           PRIMARY KEY  (`url`)
           )ENGINE=InnoDB DEFAULT CHARSET=utf8;
   '''.format(tablename)
try:
    cursor.execute(sql)
    db.commit()
    print('新建图书借阅数据表成功！')
    # self.lineEdit_4.setText('新建图书借阅数据表成功！')
except Exception as e:
    db.rollback()
    print('新建图书借阅数据表失败！{}'.format(e))
finally:
    cursor.close()
    db.close()"""

"""http = 'https://www.9gexing.com/hongse/13424.html'
response = requests.get(http, headers={
    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit'
                  '/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'})
content = response.content.decode("utf-8")
content = etree.HTML(content)
message = content.xpath("//div[1]/div[1]/div/p/text()")
message = "".join(message)
message = message.replace(" ", "").replace("\r\n", "").replace("\t", "").replace(
    "\xa0本站信息均来自网络，如果侵犯了您的权利，请及时联系我们，我们将会及时处理。上一篇：下一篇：", "")
print(message)"""

"""story_list = []
driver = webdriver.Chrome(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver")

print("Loading...................................")
driver.get('https://www.9gexing.com/hongse/')
for i in range(2):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(random.uniform(0.2, 1))
storyLists = driver.find_elements_by_css_selector('.lbox li')
for storyList in storyLists:
    story_dict = {}
    title = storyList.find_element_by_css_selector('.blogtitle a').text
    story_dict['title'] = title
    brief = storyList.find_element_by_css_selector('.blogtext').text
    story_dict['brief'] = brief
    url = storyList.find_element_by_css_selector('a').get_attribute("href")
    story_dict['url'] = url
    #print(story_dict)
    story_list.append(story_dict)
driver.quit()
for list in story_list:
    print(list)
    print(list['url'])"""
