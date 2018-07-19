class Player:
        image = None
        image_path = r"res\player.png"
        width = 64
        height = 90
        position_x = 0
        position_y = 0
        horizontal_speed = 1
        vertical_speed = 1
        moving_left = False
        moving_right = False
        moving_up = False
        moving_down = False

        def __init__(self, pygame, window):
                self.image = pygame.image.load(self.image_path)
                self.position_x = (window.width / 2) - (self.width / 2)
                self.position_y = (window.height - self.height)

                window.screen.blit(self.image, (self.position_x, self.position_y))

        def update(self, pygame, window, background):
                if (self.moving_left == True) or (self.moving_right == True) or (self.moving_up == True) or (self.moving_down == True):
                        self.updatePostion(pygame, window, background)

        def updatePostion(self, pygame, window, background):
                rect = pygame.Rect(self.position_x, self.position_y, self.width, self.height)
                window.screen.blit(background.image, rect, rect)

                if self.moving_left == True:
                        self.position_x -= self.horizontal_speed
                        self.position_x = max(self.position_x, 0)
                if self.moving_right == True:
                        self.position_x += self.horizontal_speed
                        self.position_x = min(self.position_x, window.width - self.width)
                if self.moving_up == True:
                        self.position_y -= self.vertical_speed
                        self.position_y = max(self.position_y, 0)
                if self.moving_down == True:
                        self.position_y += self.vertical_speed
                        self.position_y = min(self.position_y, window.height - self.height)

                window.screen.blit(self.image, (self.position_x, self.position_y))

class Window:
        width = 640
        height = 480
        title = ""
        color = (63, 122, 77)    
        screen = None
        caption = None
        logo = None
        logo_path = r"res\logo.jpg"
        
        def __init__(self, pygame):
                self.logo = pygame.display.set_icon(pygame.image.load(self.logo_path))   
                self.caption = pygame.display.set_caption(self.title)
                self.screen = pygame.display.set_mode((self.width, self.height))      
                self.screen.fill(self.color)

class Background:       
        image = None
        image_path = r"res\background.png"

        def __init__(self, pygame, window):
                self.image = pygame.image.load(self.image_path)

                window.screen.blit(self.image,(0, 0))

class FPSCounter:
        font = None
        image = None
        size = 20
        color = (0, 0, 0)
        position_x = 610
        position_y = 5

        def __init__(self, pygame, window):
                self.font = pygame.font.Font(None, self.size)

        def update(self, pygame, window, background, clock):
                
                fps = str(round(clock.get_fps(), 1))

                self.image = self.font.render(fps, True, self.color)
                self.position_x = window.width - self.image.get_width() - 20 
                rect = pygame.Rect(self.position_x, self.position_y, self.image.get_width(), self.image.get_height())
                window.screen.blit(background.image, rect, rect)       
                window.screen.blit(self.image, (self.position_x, self.position_y))