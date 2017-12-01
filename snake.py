 class Player:
    x = 10
    y = 10 
    speed = 1
    
    def  moveRight(self):
     self.x = self.x + self.speed
     
     def moveLeft(self):
      self.x = self.x - self.speed
      
      def moveUp(self):
       self.y = self.y - self.speed
       
       def moveDown(self):
        self.y = self.y + self.speed
       
       
     class App:
      
      windowWidth = 800
      windowHeight = 600
      player = 0
      
      def __init__(self):
       self.running = true
       self.display_surf = true
       self.image_surf = true
       self.play = Player()
