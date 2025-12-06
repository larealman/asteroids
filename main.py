import pygame
from logger import log_state, log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    # print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0
    running = True
    
    while running:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        for sprite in drawable:
            sprite.draw(screen)
        updatable.update(dt)
        for sprite in asteroids:
            if player.collides_with(sprite):
                log_event("player_hit")
                print("Game over!")
                running = False
        for sprite in shots:
            for asteroid in asteroids:
                if sprite.collides_with(asteroid):
                    log_event("asteroid_shot")
                    # print("Shot hit asteroid!")
                    # running = False
                    sprite.kill()
                    asteroid.split()
        pygame.display.flip()
        dt = clock.tick(60) / 1000.0

    pygame.quit()
    exit()
if __name__ == "__main__":
    main()
