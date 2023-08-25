import pyodbc
import config
import datetime

class SqlServerConnection :
    global conn
    def __init__(self) -> None:
        self.__errorSqlServer = open(config.path_file_error_sqlserver,"a")
        self.__errorSqlServer.write(f"Init SqlServer Connection {datetime.datetime.now()} \n")
        self.GetConnection()
    def close_file(self):
        self.__errorSqlServer.write(f"Finish SqlServer Connection {datetime.datetime.now()} \n")
        self.__errorSqlServer.close()

    def GetConnection(self) :
        try:
            cnxn_str = (f"Driver={config.sqlserver_driver};"
                f"Server={config.sqlserver_servername};"
                f"Database={config.sqlserver_database};"
                "TrustServerCertificate=yes;"
                "Trusted_Connection=yes;")
            self.conn = pyodbc.connect(cnxn_str)
        except Exception as ex:
            self.__errorSqlServer.write(f"SQLSERVER ERROR Error: {ex} {datetime.datetime.now()} \n") 


    def isExistCoordenadas(self, code):
        try:
            status = True
            cursor = self.conn.cursor()
            cursor.execute("SELECT codigo FROM CoordenadasIntitucion WHERE codigo = ?",code)
            row = cursor.fetchone()
            if row == None : 
                status = False
            return status
        except Exception as ex:
            self.__errorSqlServer.write(f"SQLSERVER ERROR Error: {ex} {datetime.datetime.now()}\n")
    def isExistCE(self, code):
        try:
            status = True
            cursor = self.conn.cursor()
            cursor.execute("SELECT codigo FROM Instituciones WHERE codigo = ?",code)
            row = cursor.fetchone()
            if row == None : 
                status = False
            return status
        except Exception as ex:
            self.__errorSqlServer.write(f"SQLSERVER ERROR Error: {ex} {datetime.datetime.now()}\n")
    def isExistUbication(self, code):
        try:
            status = True
            cursor = self.conn.cursor()
            cursor.execute("SELECT codigo FROM UbicacionInstitucion WHERE codigo = ?",code)
            row = cursor.fetchone()
            if row == None : 
                status =  False
            return status
        except Exception as ex:
            self.__errorSqlServer.write(f"SQLSERVER ERROR Error: {ex} {datetime.datetime.now()}\n")
    def insert_register_coordenadas(self,code: str,lat: float, lng:float) -> bool:
        try:
            status = False
            if (self.isExistCoordenadas(code) == False):
                cursor = self.conn.cursor()
                count = cursor.execute("INSERT INTO CoordenadasIntitucion (codigo,lat,lng) VALUES(?,?,?)",code,lat,lng).rowcount
                self.conn.commit()
                return True
            return status
        except Exception as ex:
            self.__errorSqlServer.write(f"SQLSERVER ERROR Error: {ex} {datetime.datetime.now()}\n")

    def insert_register_institution(self,code: str, name: str) -> bool: 
        try:
            status = False
            if (self.isExistCE(code)==False) :
                cursor = self.conn.cursor()
                count = cursor.execute("INSERT INTO Instituciones (codigo,centro_educativo) VALUES(?,?)",code,name).rowcount
                self.conn.commit()
                status = True
            return status
        except Exception as ex:
            self.__errorSqlServer.write(f"SQLSERVER ERROR Error: {ex} {datetime.datetime.now()}\n")
        
    def insert_register_institution_ubication(self, code: str, province: str, canton: str, district: str) -> bool:
        try:
            status = False
            if (self.isExistUbication(code)==False) :
                cursor = self.conn.cursor()
                count = cursor.execute("INSERT INTO UbicacionInstitucion (codigo,provincia,canton,distrito) VALUES(?,?,?,?)",code,province,canton,district).rowcount
                self.conn.commit()
                status = True
            return status
        except Exception as ex:
            self.__errorSqlServer.write(f"SQLSERVER ERROR Error: {ex} {datetime.datetime.now()}\n")
        

