class Information :
    def __init__(self, code:str,name: str,cartel:str,latitud : float,longitud : float,type_site:str,modalidad:str,dashboard:str,provider:str,count:int) -> None:
        self.__code = code
        self.__name = name
        self.__cartel = cartel
        self.__lat = latitud
        self.__lng = longitud
        self.__site = type_site
        self.__modalidad = modalidad
        self.__dashboard = dashboard
        self.__provider = provider
        self.__count = count

    def get_code(self) -> str:
        return self.__code
    def get_name(self) -> str:
        return self.__name
    def get_cartel(self) -> str:
        return self.__cartel
    def get_lat(self) -> float:
        return self.__lat
    def get_lng(self) -> float:
        return self.__lng
    def get_type_site(self) -> str:
        return self.__site
    def get_modalidad(self) -> str:
        return self.__modalidad
    def get_dashoard(self) -> str:
        return self.__dashboard
    def get_provider(self) -> str:
        return self.__provider
    def get_count_device(self) -> str:
        return str(self.__count)
    def get_format_data(self):
        return {
                "Centro_educativo":self.get_name(),
                "codigo":self.get_code(),
                "cartel":self.get_cartel(),
                "latitud":self.get_lat(),
                "longitud":self.get_lng(),
                "tipositio":self.get_type_site(),
                "modalidad":self.get_modalidad(),
                "dashboard":self.get_dashoard(),
                "proveedor":self.get_provider(),
                "cantidad":self.get_count_device()
        }
