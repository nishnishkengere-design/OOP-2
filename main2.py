from turtle import

class Face:

    def_init(self, xpos, ypos)
       self.size = 90
       self.coord =  (xpos, ypos)
       self.noseSize = 'small'

    def setSize(self, radius):
        self.size = radius

    def draw(self):
        self.goHome
        pensize(3)
        speed(0)
        self.drawOutline()
        self.drawEye(135)
        