import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class AutoClick:
    global driver, check

    def __init__(self):
        print("시작합니다")

    @staticmethod
    def login():
        global driver
        # setup Driver|Chrome : 크롬드라이버를 사용하는 driver 생성
        driver = webdriver.Chrome('./chromedriver.exe')
        # 사이즈조절
        driver.set_window_size(1400, 1000)
        driver.get('https://www.saramin.co.kr/zf_user/auth?ut=c')

    @staticmethod
    def start_click(data, data2, data3):
        global driver, check
        try:
            driver.get( 'http://www.saramin.co.kr/zf_user/memcom/talent-pool/main')
            time.sleep(2)

            #진행중 선택한놈 클릭하기
            l = driver.find_element(By.XPATH, "//*[@id='app']/div/div[1]/ul[1]/li[1]/ul/li[" + str(data+1) + "]")
            l.click()

            time.sleep(2)

            #미열람 클릭
            miyulam = driver.find_element(By.XPATH, "//*[@id='inner_content_list']/div/div[1]/div[1]/div/span[2]/label")
            miyulam.click()

            check = True
            while check:
                time.sleep(2)
                #btn_check = driver.find_element(By.XPATH, "//*[@id='inner_content_list']/div[2]/div[2]/ul/li[1]/div[3]/button")

                btn_check = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@id='inner_content_list']/div[2]/div[2]/ul/li[1]/div[3]/button"))
                )
                driver.execute_script("arguments[0].click();", btn_check)

                road1 = WebDriverWait(driver, 30).until(
                    EC.presence_of_all_elements_located((By.ID, "load_pre_suggest"))
                )
                road1[0].click()

                time.sleep(1)

                select1 = Select(driver.find_element(By.ID, "sel_position_name"))
                select1.select_by_index(int(data2))

                time.sleep(1)

                select2 = Select(driver.find_element(By.ID, "sel_import_suggest"))
                select2.select_by_index(int(data3))

                time.sleep(1)

                load_btn = driver.find_element(By.ID, "load_btn")
                load_btn.click()

                time.sleep(1)

                kakaotalk = driver.find_element(By.XPATH, "//*[@id='frm']/dl[4]/dd/span[2]/label")
                driver.execute_script("arguments[0].click();", kakaotalk)

                submit_btn = driver.find_element(By.XPATH, "//*[@id='btn_send_submit']")
                submit_btn.click()

                alert = driver.switch_to_alert()
                alert.accept()

                time.sleep(1)
                alert2 = driver.switch_to_alert()
                alert2.accept()

        except Exception as e:  # 모든 예외의 에러 메시지를 출력할 때는 Exception을 사용
            print('예외가 발생했습니다.', e)

    @staticmethod
    def stop_click():
        global check
        check = False

    def load_list(self):
        global driver
        try:
            driver.get("http://www.saramin.co.kr/zf_user/memcom/talent-pool/main")
            time.sleep(5)

            if self.check_exists_by_element(By.XPATH, "//*[@id='app']/div[2]/div/div[2]/button"):
                x_btn = driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div[2]/button")
                driver.execute_script("arguments[0].click();", x_btn)

                days7 = driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div[2]/div/label[2]")
                driver.execute_script("arguments[0].click();", days7)

                close_day = driver.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div[2]/div/button")
                driver.execute_script("arguments[0].click();", close_day)

            list_ul = driver.find_elements(By.XPATH, "//*[@id='app']/div/div[1]/ul[1]/li[1]/ul/li")

        except Exception as e:
            print(e)
        return list_ul

    def load_send_job(self):
        global driver
        time.sleep(1)
        sendJob = driver.find_element(By.XPATH, "//*[@id='inner_content_list']/div[2]/div[1]/div[1]/div/span[1]/label")
        sendJob.click()
        time.sleep(5)

        tel_btn = driver.find_element(By.XPATH, "//*[@id='inner_content_list']/div[2]/div[2]/ul/li[1]/div[3]/button")
        driver.execute_script("arguments[0].click();", tel_btn)

        time.sleep(3)
        load_pre_suggest = driver.find_element(By.XPATH, "//*[@id='load_pre_suggest']")
        driver.execute_script("arguments[0].click();", load_pre_suggest)

        time.sleep(2)
        sel_position_name = driver.find_elements(By.XPATH, "//*[@id='sel_position_name']/option")

        return sel_position_name

    @staticmethod
    def check_exists_by_element(by, name):
        global driver
        try:
            print("노드가 있는지 체크를 해주세요 제발요")
            driver.find_element(by, name)
        except NoSuchElementException:
            print("노드가 없는 것이다.")
            return False
        return True

