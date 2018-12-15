class construct:
    def __init__(self):
        self._mo = 0
        
    def add1(self):
        self._mo +=1
        
    def _take1(self):
        self._mo +=1        
        
    def R_V(self):
        return self._mo
        
mo_obj = construct()
mo_obj.add1()
mo_obj._take1()
mo_obj._mo = 30
print(mo_obj.R_V())
        