import pygame
class Player (pygame.sprite.Sprite):
    #Sprite for the Player Object
    isCol = False
    direction = 0

    
 
    def __init__(self,size,ghosts):
        pygame.sprite.Sprite.__init__(self)
        # Variables

        self.size = size
        self.ghosts = ghosts
        self.image = pygame.image.load("pac.png").convert()
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.center = (275,265)


    def update(self,walls,changeDirectionPositions):
     
        self.movingScale = 8
 
                
        if self.direction == 1:
            self.rect.y-= self.movingScale
            if pygame.sprite.spritecollide(self,walls,False):
                self.rect.y+= self.movingScale
                  
        elif self.direction == 2:
               
            self.rect.y += self.movingScale
            if pygame.sprite.spritecollide(self,walls,False):
                self.rect.y-= self.movingScale
            
        elif self.direction == 3:
            
            self.rect.x += self.movingScale
            if pygame.sprite.spritecollide(self,walls,False):
                self.rect.x-= self.movingScale
            
        elif self.direction == 4:
                
            self.rect.x -= self.movingScale
            if pygame.sprite.spritecollide(self,walls,False):
                self.rect.x+= self.movingScale
                
        if pygame.sprite.spritecollide(self,self.ghosts,True):
            print("NO GHoSTS ANY MORE")

                    


            
            
        
            
        
        