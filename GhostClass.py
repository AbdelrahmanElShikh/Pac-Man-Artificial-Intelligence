import pygame
import collections
class Ghost(pygame.sprite.Sprite):
    def __init__(self,size,color):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ghost.png").convert()
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect()
        self.rect.x = 390
        self.rect.y = 390
        self.wall = "0"
        self.goal = "*"
        self.grid = ["0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
        "0 + - - - - + - - - - - + 0 0 + - - - - - + - - - - + 0",
        "0 | 0 0 0 0 | 0 0 0 0 0 | 0 0 | 0 0 0 0 0 | 0 0 0 0 | 0",
        "0 | 0 0 0 0 | 0 0 0 0 0 | 0 0 | 0 0 0 0 0 | 0 0 0 0 | 0",
        "0 | 0 0 0 0 | 0 0 0 0 0 | 0 0 | 0 0 0 0 0 | 0 0 0 0 | 0",
        "0 + - - - - + - - + - - + - - + - - + - - + - - - - + 0",
        "0 | 0 0 0 0 | 0 0 | 0 0 0 0 0 0 0 0 | 0 0 | 0 0 0 0 | 0",
        "0 | 0 0 0 0 | 0 0 | 0 0 0 0 0 0 0 0 | 0 0 | 0 0 0 0 | 0",
        "0 + - - - - + 0 0 + - - + 0 0 + - - + 0 0 + - - - - + 0",
        "0 0 0 0 0 0 | 0 0 0 0 0 | 0 0 | 0 0 0 0 0 | 0 0 0 0 0 0",
        "0 0 0 0 0 0 | 0 0 0 0 0 | 0 0 | 0 0 0 0 0 | 0 0 0 0 0 0",
        "0 0 0 0 0 0 | 0 0 + - - + - - + - - + 0 0 | 0 0 0 0 0 0",
        "0 0 0 0 0 0 | 0 0 | 0 0 0 0 0 0 0 0 | 0 0 | 0 0 0 0 0 0",
        "0 0 0 0 0 0 | 0 0 | 0 0 0 0 0 0 0 0 | 0 0 | 0 0 0 0 0 0",
        "+ - - - - - + - - + 0 0 0 0 0 0 0 0 + - - + - - - - - +",
        "0 0 0 0 0 0 | 0 0 | 0 0 0 0 0 0 0 0 | 0 0 | 0 0 0 0 0 0",
        "0 0 0 0 0 0 | 0 0 | 0 0 0 0 0 0 0 0 | 0 0 | 0 0 0 0 0 0",
        "0 0 0 0 0 0 | 0 0 + - - - - - - - - + 0 0 | 0 0 0 0 0 0",
        "0 0 0 0 0 0 | 0 0 |00000000000000000| 0 0 | 0 0 0 0 0 0",
        "0 0 0 0 0 0 | 0 0 |00000000000000000| 0 0 | 0 0 0 0 0 0",
        "0 +---------+-----+-----+-000-+-----+-----+---------+-0",
        "00|000000000|00000000000|00000|00000000000| 00000000|00",
        "00|000000000|00000000000|00000|00000000000| 00000000|00",
        "0-+---+0000-+-----+-----+-----+-----+-----+-000-+---+-0",
        "000000|00000|00000|00000000000000000|00000|00000|000000",
        "000000|00000|00000|00000000000000000|00000|00000|000000",
        "0-+---+-----+-0 0-+-----+-0 0-+-----+ 0 0 +-----+---+ 0",
        "00|000000000000000000000|00000|000000000000000000000|00",
        "00|000000000000000000000|00000|000000000000000000000|00",
        "0 + - - - - - - - - - - + - - + - - - - - - - - - - + 0",
        "0000000000000000000000000000000000000000000000000000000",
        "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0"
        ]
        self.w = 54
        self.h = 36
    
    
    
    def bfs(self,start,xPlayer,yPlayer):
        
        queue = collections.deque([[start]])
        seen = set([start])
        while queue:
            path = queue.popleft()
            x, y = path[-1] # to check the last element -1 means look at the end
#            if self.grid[y][x] == self.goal:
            if y == yPlayer and x == xPlayer:
                return path
            for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                if 0 <= x2 < self.w and 0 <= y2 < self.h and self.grid[y2][x2] != self.wall and (x2, y2) not in seen:
                    queue.append(path + [(x2, y2)])
                    seen.add((x2, y2))
                
    def bfs2(self,start):
         queue = collections.deque([[start]])
         seen = set([start])
         while queue:
             path = queue.popleft()
             x, y = path[-1] # to check the last element -1 means look at the end
             if self.grid[y][x] == self.goal:
                 return path
             for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
                  if 0 <= x2 < self.w and 0 <= y2 < self.h and self.grid[y2][x2] != self.wall and (x2, y2) not in seen:
                       queue.append(path + [(x2, y2)])
                       seen.add((x2, y2))
                

                    
            
    def movement (self,xPlayer,yPlayer):
        pathList = []
        count = 1
    
        width , height = (15,10)

        xPlayerr = int(xPlayer/height)
        yPlayerr = int(yPlayer/width)
        

        
        
        tmp_list = list(self.grid[yPlayerr])
        saveChar =  tmp_list[xPlayerr]
        tmp_list[xPlayerr] = '*' 
        new_str = ''.join(tmp_list)
        self.grid[yPlayerr] = new_str
        prevXPlayerr = xPlayerr
        prevYPlayerr = yPlayerr
        count = count+1
        
        print(new_str)
        
        xGhost = int(self.rect.x /height)
        yGhost = int(self.rect.y/width)

        path = self.bfs2((xGhost,yGhost))
        if count >1:
            tmp_list = list(self.grid[prevYPlayerr])
            tmp_list[prevXPlayerr] = saveChar
            new_str = ''.join(tmp_list)
            self.grid[prevYPlayerr] = new_str

        if path:
            for i in path:
                pathList.append(i)

            

        if len(pathList) > 1:
            x,y = pathList[1]
            self.rect.x = x*height
            self.rect.y = y*width


