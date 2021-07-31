import pygame
pygame.init()

class EnemySpaceship:
    pass

class Spaceship:
    def __init__(self, image, coord:tuple, direction:str, size:tuple) -> None:
        self.image = image
        self.x, self.y = coord
        self.width, self.height = size
        self.vel = 5
        self.surface = pygame.image.load(image)
        self.__initial_rotation__(direction)
        self.scale(self.width, self.height)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def scale(self, width, height):
        self.surface = pygame.transform.scale(
            self.surface, (width, height))
        self.width, self.height = width, height
        return self

    def rotate(self, degrees):
        self.surface = pygame.transform.rotate(self.surface, degrees)
        return self

    def react(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT]: self.moveLeft()
        if keys_pressed[pygame.K_RIGHT]: self.moveRight()
        if keys_pressed[pygame.K_UP]: self.moveUp()
        if keys_pressed[pygame.K_DOWN]: self.moveDown()

    def moveRight(self): 
        coord = self.rect.x + self.vel
        if coord < 1280:
            self.rect.x = coord

    def moveLeft(self): 
        coord = self.rect.x - self.vel
        if coord > 0:
            self.rect.x = coord

    def moveUp(self): 
        coord = self.rect.y - self.vel
        if coord > 0:
            self.rect.y = coord

    def moveDown(self): 
        coord = self.rect.y + self.vel
        if coord < 720:
            self.rect.y = coord

    def getX(self):
        self.x = self.rect.x
        return self.x

    def getY(self): 
        self.y = self.rect.y
        return self.y

    def getCoord(self): return (self.getX(), self.getY())

    def __initial_rotation__(self, direction):
        direction = direction.lower()
        if direction[0] == 'r': self.rotate(90)
        elif direction[0] == 'l': self.rotate(270)
        elif direction[0] == 'u': self.rotate(180)
        elif direction[0] == 'd': pass

class MiddleBar:
    def __init__(self, width, height) -> None:
        half_width = width/2
        self.rec = pygame.Rect(640-half_width, 0, width, height)
        self.leftX, self.rightX = 640-half_width, 640+width

    def draw(self, win, color):
        pygame.draw.rect(win, color, self.rec)

def updateWindow(win, Yspaceship, Rspaceship, Bar):
    WHITE, BLACK = (255,255,255), (0,0,0)
    win.fill(WHITE)
    Bar.draw(win, BLACK)
    win.blit(Yspaceship.surface, Yspaceship.getCoord()), win.blit(
            Rspaceship.surface, Rspaceship.getCoord())
    pygame.display.update()

def main():
    #Variables
    winsize = width, height = 1280, 720
    gameOn = True
    FPS = 60
    spaceship_size = spaceship_width, spaceship_height = 40, 55
    y_spaceship_coord, r_spaceship_coord = (300, 390), (800, 390)
    spaceship_velocity = 5
    #Defining objects
    win = pygame.display.set_mode(winsize)
    pygame.display.toggle_fullscreen()
    clock = pygame.time.Clock()
    dividingBar = MiddleBar(40, 720)
    #Yellow Spaceship & Red Spaceship
    Yspaceship = Spaceship("Chapter-12/Assets/spaceship_yellow.png", y_spaceship_coord, 'right', spaceship_size)
    Rspaceship = Spaceship("Chapter-12/Assets/spaceship_red.png", r_spaceship_coord, 'left', spaceship_size)
    while gameOn:
        clock.tick(FPS)  
        for event in pygame.event.get():
            if event.type == pygame.QUIT: gameOn = False
        keys_pressed = pygame.key.get_pressed()
        Yspaceship.react(keys_pressed)
        updateWindow(win, Yspaceship, Rspaceship, dividingBar)
        
        

if __name__ == '__main__': main()