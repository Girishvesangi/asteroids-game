import sys
from asteroid import Asteroid
from shot import Shot
from constants import * 
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
import pygame
def main():
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()



    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clk=pygame.time.Clock()
    dt=0
    screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    asteroids=pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    shots=pygame.sprite.Group()
    Shot.containers = (updatable, drawable, shots)

    while True:
        log_state()
        for event in pygame.event.get():
             if event.type==pygame.QUIT:
                 return
        screen.fill("black")
        for drawa in drawable:
            drawa.draw(screen)

        pygame.display.flip()
        ticked=clk.tick(60)
        dt=ticked/1000
        updatable.update(dt)
        for asteroid in asteroids:
           if  asteroid.collides_with(player):
               log_event("player_hit")
               print("Game Over!")
               sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()


if __name__ == "__main__":
    main()
