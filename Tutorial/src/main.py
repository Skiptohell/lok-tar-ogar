import constants
import pygame

def main():

        pygame.init()

        window = constants.Window(pygame)
        background = constants.Background(pygame, window)
        player = constants.Player(pygame, window)
        fps = constants.FPSCounter(pygame, window)     
        
        clock = pygame.time.Clock()

        pygame.display.update()

        running = True 

        #clock.tick()

        while running:
                print(clock.get_time())
                for event in pygame.event.get():

                        processInput(event, player)

                        if event.type == pygame.QUIT:
                                 running = False

                player.update(pygame, window, background)

                pygame.display.update()
                fps.update(pygame, window, background, clock)
                clock.tick_busy_loop(60)
        pygame.quit()
        quit()

def processInput(event, player):
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                        player.moving_left = True
                if event.key == pygame.K_RIGHT:
                        player.moving_right = True
                if event.key == pygame.K_UP:
                        player.moving_up = True
                if event.key == pygame.K_DOWN:
                        player.moving_down = True
        elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                        player.moving_left = False
                if event.key == pygame.K_RIGHT:
                        player.moving_right = False
                if event.key == pygame.K_UP:
                        player.moving_up = False
                if event.key == pygame.K_DOWN:
                        player.moving_down = False


if __name__=="__main__":
        main()


