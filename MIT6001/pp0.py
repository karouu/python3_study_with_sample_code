class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    def getY(self):
        return self.y
        
    def __str__(self):
        return '<'+str(self.getX())+','+str(self.getY())+'>'
        
    def __eq__(self,other1):
        assert type(other1) == type(self)
        return self.getX() == other1.getX() and self.getY() == other1.getY()
            
    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'
        