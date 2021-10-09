import pygame, random
pygame.init()
pygame.font.init()
class Spaceship:
    def __init__(self, image, coord:tuple, direction:str, boundaries:tuple) -> None:
        self.image, self.surface = image,  pygame.image.load(image)
        self.x, self.y = coord
        self.width, self.height = 40, 55
        self.vel, self.direction = 5, direction
        self.bullets, self.bullet_vel = [], 10
        self.health = 10
        self.__initial_rotation__(direction)
        self.scale(self.width, self.height)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.boundaries = self.blx, self.brx, self.buy, self.bdy = boundaries
        self.bullet_width, self.bullet_height = 15, 10 

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

    def fireRight(self):
        bullet = pygame.Rect(self.getX() + self.width, self.getY() + self.height/2, self.bullet_width, self.bullet_height)
        self.bullets.append(bullet)

    def fireLeft(self):
        bullet = pygame.Rect(self.getX(), self.getY() + self.height/2, self.bullet_width, self.bullet_height)
        self.bullets.append(bullet)

    def changeHealth(self, int):
        self.health += int

    def moveLeft(self): 
        coord = self.rect.x - self.vel
        if coord > self.blx:
            self.rect.x = coord

    def moveRight(self): 
        coord = self.rect.x + self.vel
        if coord < self.brx - self.width:
            self.rect.x = coord

    def moveUp(self): 
        coord = self.rect.y - self.vel
        if coord > self.buy:
            self.rect.y = coord

    def moveDown(self): 
        coord = self.rect.y + self.vel
        if coord <= self.bdy - self.height:
            self.rect.y = coord

    def getHealth(self):
        return self.health

    def getX(self):
        self.x = self.rect.x
        return self.x

    def getY(self): 
        self.y = self.rect.y
        return self.y

    def getWidth(self): return self.width

    def getCoord(self): return (self.getX(), self.getY())

    def __initial_rotation__(self, direction):
        direction = direction.lower()
        if direction[0] == 'r': self.rotate(90)
        elif direction[0] == 'l': self.rotate(270)
        elif direction[0] == 'u': self.rotate(180)
        elif direction[0] == 'd': pass

class EnemySpaceship(Spaceship):
    def __init__(self, image, coord: tuple, direction: str, boundaries: tuple) -> None:
        super().__init__(image, coord, direction, boundaries)
        self.decision_count = 0
        self.decision = 'd'

    def getRandomMovement(self):
        movements = ['l', 'r', 'u', 'd']
        num = random.randrange(0,4)
        return movements[num]
    
    def moveRandomly(self, prob):
        if prob >= random.random():
            self.decision_count += 1
            if self.decision_count < 25:
                decision = self.decision
            else:
                decision = self.decision = self.getRandomMovement()
                self.decision_count = 0
            if decision == 'l':
                self.moveLeft()
            elif decision == 'd':
                self.moveDown()
            elif decision == 'r':
                self.moveRight()
            elif decision == 'u':
                self.moveUp()
        

    def fireRandomly(self, prob):
        if prob >= random.random():
            self.fireLeft()
        
class MiddleBar:
    def __init__(self, width, height) -> None:
        half_width = width/2
        self.rec = pygame.Rect(640-half_width, 0, width, height)
        self.leftX, self.rightX = 640-half_width, 640+width

    def draw(self, win, color):
        pygame.draw.rect(win, color, self.rec)

def updateWindow(win, Yspaceship, Rspaceship, Bar):
    health_font = pygame.font.SysFont('comicsans', 40)
    
    WHITE, BLACK, BLUE = (255,255,255), (0,0,0), (0,0,255)
    win.fill(WHITE)
    Bar.draw(win, BLACK)
    win.blit(Yspaceship.surface, Yspaceship.getCoord()), win.blit(
            Rspaceship.surface, Rspaceship.getCoord())
    red_health_text = health_font.render('Health: ' + str(Rspaceship.getHealth()), 1, BLACK)
    yellow_health_text = health_font.render('Health: '+str(Yspaceship.getHealth()),1, BLACK)
    win.blit(red_health_text, (1000, 10))
    win.blit(yellow_health_text, (280, 10))
    #Handle Yellow bullets
    for bullet in Yspaceship.bullets:
        bullet.x += Yspaceship.bullet_vel
        pygame.draw.rect(win, (255,0,0), bullet)
        if bullet.x > 1280: Yspaceship.bullets.remove(bullet)
        if bullet.x >= Rspaceship.getX()-Yspaceship.bullet_width and bullet.x <= Rspaceship.getX() and bullet.y >= Rspaceship.getY(
        ) and bullet.y <= Rspaceship.getY() + Rspaceship.height and Rspaceship.getHealth() > 0:
            Yspaceship.bullets.remove(bullet)
            Rspaceship.changeHealth(-1)
    #Handle Red bullets
    for bullet in Rspaceship.bullets:
        bullet.x -= Rspaceship.bullet_vel
        pygame.draw.rect(win, (255,0,0), bullet)
        if bullet.x < 0: Rspaceship.bullets.remove(bullet)
        if bullet.x >= Yspaceship.getX() and bullet.x <= Yspaceship.getX()+Yspaceship.width and bullet.y >= Yspaceship.getY(
        ) and bullet.y <= Yspaceship.getY() + Yspaceship.height and Yspaceship.getHealth() > 0:
            Rspaceship.bullets.remove(bullet)
            Yspaceship.changeHealth(-1)
    Rspaceship.moveRandomly(.25)
    Rspaceship.fireRandomly(.05)
    pygame.display.update()

def main():
    #Variables
    BLUE = (0,0,255)
    winsize = width, height = 1280, 720
    gameOn = True
    FPS = 60
    y_spaceship_boundaries, r_spaceship_boundaries = (0,620,0,720), (660,1280,0,720)
    y_spaceship_coord, r_spaceship_coord = (300, 390), (800, 390)
    winner_font = pygame.font.SysFont('comiscans', 100)
    #Defining objects
    win = pygame.display.set_mode(winsize)
    #pygame.display.toggle_fullscreen()
    clock = pygame.time.Clock()
    dividingBar = MiddleBar(40, 720)
    #Yellow Spaceship & Red Spaceship
    Yspaceship = Spaceship("Chapter-12/Assets/spaceship_yellow.png", y_spaceship_coord, 'right', y_spaceship_boundaries)
    Rspaceship = EnemySpaceship("Chapter-12/Assets/spaceship_red.png", r_spaceship_coord, 'left', r_spaceship_boundaries)
    
    while gameOn:
        clock.tick(FPS)  
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                gameOn = False
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_f: Yspaceship.fireRight()
        keys_pressed = pygame.key.get_pressed()
        Yspaceship.react(keys_pressed)
        if Rspaceship.getHealth() <= 0: 
            winner_text = 'Yellow Wins!'
            winner_text_surf = winner_font.render(winner_text, 1, BLUE)
            win.blit(winner_text_surf, (500, 300))
            pygame.display.update()
            pygame.time.delay(5000)
            break
        elif Yspaceship.getHealth() <= 0:
            winner_text = 'Red Wins'
            winner_text_surf = winner_font.render(winner_text, 1, BLUE)
            win.blit(winner_text_surf, (500, 300))
            pygame.display.update()
            pygame.time.delay(5000)
            break
        updateWindow(win, Yspaceship, Rspaceship, dividingBar)
    main()
        
        

if __name__ == '__main__': main()