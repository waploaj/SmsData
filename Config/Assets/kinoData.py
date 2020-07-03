from lxml import html
from selenium import webdriver
import pymysql


class CityData:

    def __init__(self):
        self.driver=webdriver.Chrome(executable_path='/home/waploaj/chromedriver_linux64/chromedriver')
        self.conn=pymysql.connect("127.0.0.1",'root','','nchizetu')

    @property
    def city_population(self):
        self.driver.get("https://www.citypopulation.de/en/tanzania/cities/")
        path="""//*[@id="tl"]/tbody"""
        table=self.driver.find_element_by_xpath(f"{path}")
        citys={}

        for row in table.find_elements_by_tag_name("tr"):
            city=row.text
            ci=city.split()
            citys["name"]=ci[0]
            citys["population"]=ci[8]
            citys["pop_projection"]=ci[9]
        return citys

    def save_city_population(self):
        citys=CityData.city_population
        name=citys["name"]
        po_12=citys["population"]
        projection=citys["pop_projection"]
        with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
            query=f"INSERT INTO nchizetu.city(name,population,po_projection)VALUES('{name}','{po_12}','{projection}')"
            cursor.execute(query)
            self.conn.commit()

    @staticmethod
    def city_info():
        p = CityData()
        with p.conn.cursor(pymysql.cursors.DictCursor) as cursor:
            query="SELECT * FROM nchizetu.city"
            cursor.execute(query)
            row=cursor.fetchall()
        return row

    @property
    def city_gender_info(self):

        wilaya = {}
        for i in range(0,30):
            if i<10:
                url=f"https://www.citypopulation.de/en/tanzania/admin/0{i}__arusha/"
            else:
                url=f"https://www.citypopulation.de/en/tanzania/admin/{i}__arusha/"

            self.driver.get(url)
            gender=self.driver.find_element_by_xpath("""//*[@id="tl"]/tbody[2]""")
            city = self.driver.find_element_by_xpath("""//*[@id="admtable"]/header/h1/span""")

        for row in gender.find_elements_by_tag_name("tr"):
            wards = row.text
            ward = wards.split()
            name =  wilaya["name"] = ward[0]
            po_02 = wilaya["2002"] = ward[3]
            po_12 = wilaya["2012"] = ward[4]

            database = CityData.city_info()
            for data in database:
                if data["name"] == city.text:
                    city_id = data["city_id"]

                    with self.conn.cursor(pymysql.cursors.DictCursor) as cursor:
                        query=f"INSERT INTO nchizetu.ward(name,city_id,po_02,po_12)VALUES('{name}','{city_id}','{po_02}','{po_12}')"
                        cursor.execute(query)
                        rows = cursor.rowcount
                        self.conn.commit()
        return f"{rows} are affected!!"

    def age_distribution(self):
        return None

    def gender(self):
        return None

    def urbanization(self):
        return None

p=CityData()
print(p.city_gender_info())
