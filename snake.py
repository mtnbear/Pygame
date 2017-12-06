 from.pygamelocals import*
 import time
 
 class Apple:
    x = 0
    y = 0
    step = 44
 
    def __init__(self,x,y):
        self.x = x * self.step
        self.y = y * self.step
 
    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y))
 
 
 
 class Player:
    x = []
    y = []
    step = 44
    direction = 0
    length = 3
 
    updateCountMax = 2
    updateCount = 0
 
    def __init__(self, length):
       self.length = length
       for i in range(0,length):
           self.x.append(0)
           self.y.append(0)
 
    def update(self):
 
        self.updateCount = self.updateCount + 1
        if self.updateCount &gt; self.updateCountMax:
 
            # update previous positions
            for i in range(self.length-1,0,-1):
                print "self.x[" + str(i) + "] = self.x[" + str(i-1) + "]"
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]
 
            # update position of head of snake
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step
 
            self.updateCount = 0
 
 
    def moveRight(self):
        self.direction = 0
 
    def moveLeft(self):
        self.direction = 1
 
    def moveUp(self):
        self.direction = 2
 
    def moveDown(self):
        self.direction = 3 
 
    def draw(self, surface, image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i])) 
  
    class Game:
    
    def isCollision(self,x1,y1,x2,y2,bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False   
       
     class App:
      
      windowWidth = 800
      windowHeight = 600
      player = 0
      
      def __init__(self):
       self.running = true
       self.display_surf = true
       self.image_surf = true
       self.play = Player()
       
       def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        
        pygame.display.set_caption('Pygame snake game')
        self._running = false
        def on_loop(self):
         pass
        
        def on_render(self):
         self._display_surf.fill((0,0,0))
         self._display_surf.blit(self._image_surf,(self.player.x,self.player.y))
         pygame.display.flip()
         
         def on_cleanup(self):
          pygame.quit()
          
          def on_execute(self):
           if self.on_init() == false:
             self._running = false
             
             while( self._running ):
              pygame.event.pump()
              keys = pygame.key.get_pressed()
              
              if (key[K_RIGHT]):
               self.player.moveRight()
               
               if (key[K_LEFT]):
               self.player.moveLeft()
               
               if (key[K_UP]):
                self.player.MoveUp()
                
                if (key[K_DOWN]):
                 self.player.MoveDown()
                 
                 if (key[K_ECSCAPE]:
                     self._running = false 
                     self.on_loop()
                     self.on_render()
                     
                     time.sleep (50.0 / 1000.0);
                   self.on_cleanup()
if __name__ == "__main__" :
                     theApp = App()
                     theApp.on_execute()
                     

                     
                     
                     
                     
       
