from   selenium import webdriver
from   selenium.webdriver.common.keys import Keys
import time
import calendar
import random

driver = webdriver.Chrome()

#Login
ID_number = str(input('請輸入帳號：'))
password  = str(input("請輸入密碼："))
job       = "'" + str(input('請輸入登入身分 (兼任助理為3)：')) + "'"

projtype = "'" + str(input('請輸入計畫代碼 ex:105-01837：')) + "'"
workhour=str(input('請輸入工作時數：')) #input workhour
workroutine = []
print('請輸入五個工作項目')
for i in range(4):
    print ('第',i+1,'項')
    workroutine.append(str(input("請輸入工作項目："))) #input workroutine

year = str(input('請輸入年份：'))
month = str(input('請輸入月份：'))


driver.get('https://miswww1.ccu.edu.tw/pt_proj/index.php')
driver.set_page_load_timeout(50)
driver.maximize_window()
driver.implicitly_wait(30)
user = driver.find_element_by_name("staff_cd").send_keys(ID_number)
passwd = driver.find_element_by_name("passwd").send_keys(password)
driver.find_element_by_xpath(("//select[@name='proj_type']/option[@value=%s]")%job).click()
driver.find_element_by_xpath("/html/body/center/form/input[1]").click()
print ("已進入工作日誌系統")
time.sleep(1) #delay seconds

#Enter Workroutine Space & write in

date = calendar.monthcalendar((int(year)+1911),int(month))
workday = set()
for everyweek in date:
        del everyweek[-1]
        del everyweek[-1]
        for day in everyweek:
            workday.add(day)
workday.remove(0)
workday = list(workday)
print(workday)

for eachday in workday:
    driver.get("https://miswww1.ccu.edu.tw/pt_proj/main2.php")
    driver.find_element_by_xpath(("//select[@name='type']/option[@value=%s]")%(projtype)).click()

    y = driver.find_element_by_name('yy')
    y.send_keys(Keys.BACK_SPACE*10)
    y.send_keys(year)

    m = driver.find_element_by_name('mm')
    m.send_keys(Keys.BACK_SPACE*10)
    m.send_keys(month)

    d = driver.find_element_by_name('dd')
    d.send_keys(Keys.BACK_SPACE*10)
    d.send_keys(str(eachday))

    driver.find_element_by_name('hrs').send_keys(workhour)
    driver.find_element_by_name('workin').send_keys(random.choice(workroutine))
    driver.find_element_by_xpath("/html/body/form/center/input[1]").click()

    print ('以輸入',year,' 年 ',month, ' 月 ', eachday, '日  工作',workhour,' 小時' )

print (year,' 年 ',month, ' 月 的工作日誌已全數填寫完畢 並 儲存於資料庫')

#Finish & Save
driver.get("https://miswww1.ccu.edu.tw/pt_proj/main2.php")
time.sleep(5)
driver.find_element_by_xpath("/html/body/form/center/input[2]").click()
driver.find_element_by_xpath("/html/body/center[2]/input").click()

print ('請自行產生批號')