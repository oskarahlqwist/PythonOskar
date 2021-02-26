class Hundagare:
    def __init__(self, namn, adress, adressnr, titel):
        self.__namn__ = namn
        self.__adress__ = adress
        self.__adressnr__ = adressnr
        self.__titel__ = titel
    
    def get_namn(self):
        return self.__namn__    
    def set_namn(self,namn):
        self.__namn__ = namn

    def get_adress(self):
        return self.__adress__    
    def set_adress(self,adress):
        self.__adress__ = adress

    def get_adressnr(self):
        return self.__adressnr__    
    def set_adressnr(self,adressnr):
        self.__adressnr__ = adressnr

    def get_titel(self):
        return self.__titel__    
    def set_titel(self,titel):
        self.__titel__ = titel
    
    def __str__(self):
        return '%-15s %-15s %-15s %-15s' %    \
            (self.__namn__,self.__adress__,self.__adressnr__,self.__titel__)