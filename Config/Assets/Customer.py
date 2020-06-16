from Config.database import Connection

class Customer(Connection):


    def customer_info(self):
        d = Connection()
        data = d.run_query("SELECT * FROM `People` ORDER BY `People`.`Name` ASC")
        return  data

p = Customer()

