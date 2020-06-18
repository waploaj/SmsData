from lxml import html
from selenium import webdriver
from Config.database import Connection

driver = webdriver.Chrome(executable_path='/home/waploaj/chromedriver_linux64/chromedriver')

if __name__ == "__main__":
    driver.get("https://www.citypopulation.de/en/tanzania/cities/")
    path = """//*[@id="tl"]/tbody"""
    table = driver.find_element_by_xpath(f"{path}")
    citys = {}

    for row in table.find_elements_by_tag_name("tr"):
        city = row.text
        ci = city.split()
        citys["name"] = ci[0]
        citys["population"] = ci[8]
        citys["pop_projection"] = ci[9]
        print(citys
              )
        p = Connection()
        name =citys["name"]
        po_12 =citys["population"]
        projection = citys["pop_projection"]
        query = f"insert into nchizetu.city({name},{po_12},{projection}"
        p.run_query(query)

        # for i in range(0,27):
        #     url = f"https://www.citypopulation.de/en/tanzania/admin/{i}__arusha/"
        #     driver.get(url)
        #     path = """//*[@id="tl"]/tbody[2]"""
        #     ward = driver.find_element_by_xpath(f"{path}")
        # print(citys["name"])








