from ast import With
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime
from time import sleep, time
import config
import random
import Information as CE
import UbicationCE as location
import SqlServerDatabase as sqlserverconn
sqlserverconn = sqlserverconn.SqlServerConnection()
import mongoScript as mongodb
conn_mongo = mongodb.Mongo_Database()


class InformationCE:
    
    def __init__(self) -> None:
        self.__errorScript = open(config.path_file_error,"a")
        conn_mongo.mongodb_information_centros_educativos().delete_many({})
        self.__errorScript.write(f"Init Script {datetime.datetime.now()} \n")

    def get_ubications(self,browser) -> None:
        try:
            data2 = browser.find_element(By.CSS_SELECTOR,"div.mainSection")
            dataP = data2.find_element(By.TAG_NAME,"p").get_attribute("outerHTML")
            dir = dataP.split("Dirección</strong>: ")
            dirfinal = dir[1].split("<br><strong>")
            locaciones = dirfinal[0].split(',')
            self.__ubication = location.UbicationCE(locaciones[0],locaciones[1],locaciones[2])
        except Exception as ex:
            self.__errorScript.write(f"Ubication Save Error: {ex} {datetime.datetime.now()}\n") 
             
    def get_code(self,data_excel) -> str:
        try:
            code_temp = str(data_excel[1]).split('.')
            code = code_temp[0]
            if len(code) < 4 :
                code = f"0{code}"
            return code
        except Exception as ex:
            self.__errorScript.write(f"Get Code Save Error: {ex} {datetime.datetime.now()}\n") 
    
    def get_lat(self, latitud) -> str:
        try:
            if len(latitud) == 6:
                lat = str(latitud[2].text).replace(',','.')
            else:
                lat = str(latitud[1].text).replace(',','.')
            return lat
        except Exception as ex:
            self.__errorScript.write(f"Latitud Save Error: {ex} {datetime.datetime.now()}\n") 
    
    def get_lng(self,longitud) -> str:
        try:
            if len(longitud) == 6:
                lng = str(longitud[3].text).replace(',','.')
            else:
                lng = str(longitud[2].text).replace(',','.')
            return lng
        except Exception as ex:
            self.__errorScript.write(f"Longitud Save Error: {ex} {datetime.datetime.now()}\n") 

    def get_information(self) -> None:
        try:
            global total_current
            chrome_options = webdriver.ChromeOptions()
            browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
            browser.get(config.path_get_driver)
            browser.maximize_window()
            browser.get(config.path_get_map)
            element_code_ce = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.CLASS_NAME,'searchInput')))
            print(datetime.datetime.now())
            for sheetname in config.sheetnames:
                try:
                    element_data_excel = pd.read_excel(config.filepath,sheet_name=sheetname).values.tolist()
                    for value_element in element_data_excel:
                        code_ce = self.get_code(value_element)
                        element_code_ce.click()
                        element_code_ce.send_keys(Keys.CONTROL + "a")
                        element_code_ce.send_keys(Keys.DELETE)
                        element_code_ce.send_keys(code_ce)
                        search_button = WebDriverWait(browser, 40).until(EC.element_to_be_clickable((By.CLASS_NAME,'searchSubmit')))
                        search_button.click()
                        element_data_values = WebDriverWait(browser, 40).until(EC.visibility_of_all_elements_located((By.CLASS_NAME,'esriNumericValue')))

                        self.get_ubications(browser)
                        lat = self.get_lat(element_data_values)
                        lng = self.get_lng(element_data_values)
                        
                        information = CE.Information(code_ce,str(value_element[0]),str(value_element[2]),float(lat),float(lng),str(value_element[3]),str(value_element[4]),str(config.systemDashboards[random.randint(1,3)]),str(config.providers[random.randint(1,3)]),random.randint(1,20))
                        
                        status_insert_ubication = sqlserverconn.insert_register_institution_ubication(information.get_code(),
                                                                                                    self.__ubication.get_province(),
                                                                                                    self.__ubication.get_canton(),
                                                                                                    self.__ubication.get_district())
                        status_insert_institution = sqlserverconn.insert_register_institution(information.get_code(),
                                                                                            information.get_name(),
                                                                                            )
                        status_insert_coordenadas = sqlserverconn.insert_register_coordenadas(information.get_code(),
                                                                                            information.get_lat(),
                                                                                            information.get_lng()
                                                                                            )
                        conn_mongo.mongodb_information_centros_educativos().insert_one(information.get_format_data())
                        sleep(2)
                except Exception as ex:
                    self.__errorScript.write(f"Main Error: {ex} {datetime.datetime.now()}\n")  
                    
            print(datetime.datetime.now())
            self.__errorScript.write(f"Finish Script {datetime.datetime.now()} \n")
        except Exception as ex:
            self.__errorScript.write(f"get_information Save Error: {ex} {datetime.datetime.now()}\n")
        finally:
            self.__errorScript.close()
            sqlserverconn.close_file()
            conn_mongo.close_file()

InformationCE().get_information()