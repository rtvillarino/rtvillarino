import pyglet

class cd():
    def __init__(self):
        self.start = '3'
        self.display = pyglet.text.Label(self.start,font_size=65,x=1180//2, y=590//2, 
                                        anchor_x = 'center', anchor_y = 'center')
        self.running = False
        self.time = 5
        self.display.color = (255, 255, 255, 255)

    def update(self,dt):
        if self.running == True:
            self.time-=dt
            m = int(self.time//1)
            self.display.text = '%s'% m
            if m < 1:
                self.running = False
                self.display.text = 'SIMULAN!'
    def reset(self):
        self.display.text = self.start
        self.time = 5

time_alloted = 1
class game_timer():
    def __init__(self):
        self.start = '%s:00' % time_alloted
        self.display = pyglet.text.Label(self.start,font_size=40,x=1049, y=539, 
                                            anchor_x = 'center', anchor_y = 'center')
        self.running = False
        self.time = 62
        self.display.color = (255, 255, 255, 255)
        
    def update(self,dt):
        if self.running == True:
            self.time-=dt
            mins, sec = divmod(self.time,60)
            self.display.text = '%02d:%02d'% (mins,sec)
            if sec < 1 and mins==0:
                self.running = False
                self.display.text = 'TIGIL!'

    def reset(self):
        self.display.text = self.start
        self.time = 62