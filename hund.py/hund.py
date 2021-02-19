class Hund:
    def __init__(self, namn,ras,typ,alder,farg):
        self.__namn__ = namn
        self.__ras__ = ras
        self.__typ__ = typ if typ in ["brukshund", "kamphund", "jakthund", "familjehund", "tävlingshund"] else "okänd" 
        self.__alder__ = alder ##int   
        self.__farg__ = farg
        
    def get_namn(self):
        return self.__namn__    
    
    def set_namn(self,namn):
        self.__namn__ = namn
    
    def get_ras(self):
        return self.__ras__
    
    def set_ras(self,ras):
        self.__ras__ = ras
    
    def get_typ(self):
        return self.__typ__    
    def set_typ(self,typ):
        if typ in ["brukshund", "kamphund", "jakthund", "familjehund", "tävlingshund"]:
            self.__typ__ = typ
    
    def get_alder(self):
        return self.__alder__
    
    def set_alder(self,alder):
        self.__alder__ = alder
    
    def fodelsedag(self):
        self.__alder__ += 1
    
    def get_farg(self):
        return self.__farg__
    
    def set_farg(self,farg):
        self.__farg__ = farg

    def get_agare(self):
        return self.__agare__
    
    def set_agare(self,agare):
        self.__agare__ = agare   

    def __str__(self):
        return '%-15s %-10s %-15s %-4d %-15s' % (self.__namn__,self.__ras__,self.__typ__,self.__alder__,self.__farg__)

