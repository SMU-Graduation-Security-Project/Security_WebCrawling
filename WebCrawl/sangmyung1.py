from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()
url = 'https://www.smu.ac.kr/lounge/notice/notice.do'
driver.implicitly_wait(5)
driver.get(url)
글제목_list=[]  
글내용_list=[]
첫번째게시글=driver.find_element(By.XPATH,'//*[@id="ko"]/div[4]/ul/li[1]/dl/dt/table/tbody/tr/td[3]/a')
첫번째게시글.click()
time.sleep(2)
for i in range(1,20):
    글제목='//*[@id="jwxe_main_content"]/div[1]/div/div/div[1]/div/div[1]'
    글제목_el=driver.find_element(By.XPATH,글제목)
    글제목_list.append(글제목_el.text)

    글내용='//*[@id="jwxe_main_content"]/div[1]/div/div/div[1]/div/div[2]'
    글내용_el=driver.find_element(By.XPATH,글내용)
    글내용_list.append(글내용_el.text)

    이전게시글 = driver.find_element(By.XPATH,'//*[@id="jwxe_main_content"]/div[1]/div/div/div[2]/div[2]/p/a')
    이전게시글.click()
    time.sleep(1)

df = pd.DataFrame(
    {
        "글제목":글제목_list,
        "글내용":글내용_list,
    }

)
df.to_csv(r'./상명대공지사항.csv')
driver.close()