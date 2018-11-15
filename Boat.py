
class boat:
    width = 40
    height = 100
    def __init__(self, x, y, pos,image1,image2,gameDisplay):
        self.x = x
        self.y = y
        self.pos = pos  #position of boat i.e. 2,3,4,5
        self.image1 = image1
        self.image2 = image2
        self.gameDisplay = gameDisplay

    def highlight(self,a,b,c):
        if self.pos==2 or self.pos==3:
            if c=='M':
                self.gameDisplay.blit(self.image1,(a+20,b-50))
            elif c == 'C':
                self.gameDisplay.blit(self.image2,(a+20,b-50))

        elif self.pos==4 or self.pos==5:
            if c=='M':
                self.gameDisplay.blit(self.image1, (a+180,b-50))
            elif c == 'C':
                self.gameDisplay.blit(self.image2, (a + 180, b - 50))
