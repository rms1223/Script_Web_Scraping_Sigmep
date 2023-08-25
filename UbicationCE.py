class UbicationCE:
    def __init__(self, province: str, canton: str, district :str ) -> None:
        self.__province = province
        self.__canton = canton
        self.__district = district
    
    def get_province(self) ->str:
        return self.__province.strip()
    def get_canton(self) ->str:
        return self.__canton.strip()
    def get_district(self) ->str:
        return self.__district.strip()
    