from televisores.tv import TV
class Control:
    
    

    def turnOn(self):
        self.tv.turnOn()
        
    def turnOff(self):
        self.tv.turnOff()
        
    def volumenUp(self):
        self.tv.volumenUp()
        
    def volumenDown(self):
        self.tv.volumenDown()
    def canalUp(self):
        self.tv.canalUp()
        
    def canalDown(self):
        self.tv.canalDown()
        
    def setCanal(self, can):
        self.tv.setCanal(can)

    def enlazar(self, tv):
        self.tv = tv
        tv.setControl(self)

    def getTv(self):
        return self.tv