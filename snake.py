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
                   self.on_cleanup()
if __name__ == "__main__" :
                     theApp = App()
                     theApp.on_execute()
                     
                     
                 
      class Player:
            x = 10
            y = 10         
                  
                  
                     
         
                
           
                                                      
                                                      
                                               
