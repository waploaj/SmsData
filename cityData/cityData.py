from lxml import html
from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/waploaj/chromedriver_linux64/chromedriver')

if __name__ == "__main__":
    driver.get("xxxxxxxxxxx")
    path = """//*[@id="tl"]/tbody[2]"""
    table = driver.find_element_by_xpath(f"{path}")
    gender = driver.find_element_by_xpath("""//*[@id="chartgrid"]/section/table/tbody""")
    name = {}
    for ro in gender.find_elements_by_tag_name('tr'):
        ge = ro.text
        g = ge.split()
        name['male'] = g[0]
        name['female'] = g[1]
    for row in table.find_elements_by_tag_name('tr'):
        ro = row.text
        t = ro.split()
        if len(t) > 5:
            name["ward"]=t[1] + " " + t[0]
            name["mun"] = t[2] + " "+ t[3]
            name["pop02"] = t[4]
            name['pop12'] = t[5]

        else:
            name["ward"] = t[0]
            name["mun"] = t[1] + " " + t[2]
            name["pop02"] = t[3]
            name['pop12'] = t[4]

    print(name)