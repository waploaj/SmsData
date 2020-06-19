from lxml import html
from selenium import webdriver
import pymysql

class CityData:


    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='/home/waploaj/chromedriver_linux64/chromedriver')
        self.conn = pymysql.connect("127.0.0.1",'root','','nchizetu')

    def city_population(self):
        self.driver.get("https://www.citypopulation.de/en/tanzania/cities/")
        path = """//*[@id="tl"]/tbody"""
        table = self.driver.find_element_by_xpath(f"{path}")
        citys = {}

        for row in table.find_elements_by_tag_name("tr"):
            city = row.text
            ci = city.split()
            citys["name"] = ci[0]
            citys["population"] = ci[8]
            citys["pop_projection"] = ci[9]
        return citys

    def save_city_population(self):
        p = CityData()
        citys = p.city_population()
        name = citys["name"]
        po_12 = citys["population"]
        projection = citys["pop_projection"]
        with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
            query = f"INSERT INTO nchizetu.city(name,population,po_projection)VALUES('{name}','{po_12}','{projection}')"
            cursor.execute(query)
            self.conn.commit()

    def city_gender_info(self):
        for i in range(0, 30):
            if i < 10:
                url = f"https://www.citypopulation.de/en/tanzania/admin/0{i}__arusha/"
            else:
                url = f"https://www.citypopulation.de/en/tanzania/admin/{i}__arusha/"

            self.driver.get(url)
            gender = self.driver.find_element_by_xpath("""//*[@id="admtable"]/header/h1/span""")
            city = gender.text.lower()


            with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
                query = "SELECT * FROM nchizetu.city"
                cursor.execute(query)
                row = cursor.fetchall()
            for ro in row:
                if ro["name"].lower() == city:
                    # print(city)
                    table = self.driver.find_element_by_xpath("""//*[@id="chartgrid"]/section[1]/table/tbody""")
                    for row in table.find_elements_by_tag_name("tr"):
                        city = row.text
                        lis = (city.split())
                        for i in lis:
                            print(i)
                    ages = self.driver.find_element_by_xpath("""//*[@id="chartgrid"]/section[4]/table/tbody""")
                    for age in ages.find_elements_by_tag_name("tr"):
                        print(age.text)



p = CityData()
print(p.city_gender_info())














