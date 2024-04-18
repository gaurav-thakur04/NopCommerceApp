#Code to read the common data 

import configparser    

config = configparser.RawConfigParser()                            #creating the config obj
config.read(r"D:\gaurav\Projects\nopcommerceApp\Configuration\config.ini")        #loading the file

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get( 'common info','baseURL')
        return url
    
    @staticmethod
    def getUseremail():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

read = ReadConfig()
print(read.getApplicationURL())
