#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                                             Variables Scripts                                                         #
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------- Archivos manejo de Errores -----------------------------------------------#
path_file_error = r"Logs//log_main_script.txt"
path_file_error_sqlserver = r"Logs//log_script_sqlserver.txt"
path_file_error_mongodb = r"Logs//log_script_mongo.txt"
#-------------------------------------------------------------------------------------------Path System---------------------------------------------------------#
path_get_driver = "D:/Carpetas del Sistema\Descargas/chromedriver_win32/chromedriver.exe"
path_get_map = "https://sigmep.maps.arcgis.com/apps/webappviewer/index.html?id=e5588a81e7744161a149608a773f23f2"
sheetnames = ['2019-12','2020-02','2020-06','2020-10-PROVEEDOR2','2020-10-PROVEEDOR1','2021-02-PROVEEDOR1','2021-03-PROVEEDOR2','2021-04-PROVEEDOR1','2020-01-PROVEEDOR1']
filepath = "FILENAME.xlsx"    
mongo_string_connection =""
mongo_database = ""
mongo_collection = ""
sqlserver_driver = "{ODBC Driver 18 for SQL Server}"
sqlserver_database =""
sqlserver_servername =""
systemDashboards = {
            1 : "MERAKI",
            2 : "ARUBA",
            3 : "HUAWEI"
        }  
providers = {
            1 : "Proveedor1",
            2 : "Proveedor2",
            3 : "Proveedor3"
        } 
