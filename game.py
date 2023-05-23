import pygame
import random
import time

# Fenstergröße
WIDTH = 800
HEIGHT = 600

# Farben
BLUE = (0, 0, 255)

# Spieler Eigenschaften
PLAYER_WIDTH = 128
PLAYER_HEIGHT = 128
PLAYER_VELOCITY = 8
JUMP_VELOCITY = 10
GRAVITY = 0.5

# Plattform Eigenschaften
PLATFORM_WIDTH = 200
PLATFORM_HEIGHT = 50
PLATFORM_VELOCITY = 5
PLATFORM_GAP = 300  # Horizontaler Abstand zwischen den Plattformen

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jump and Run Spiel")

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/c1_run.png")
        self.image = pygame.transform.scale(self.image, (PLAYER_WIDTH, PLAYER_WIDTH))
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2
        self.rect.y = HEIGHT - PLAYER_HEIGHT
        self.velocity_y = 0
        self.on_ground = False

    def update(self):
        self.velocity_y += GRAVITY

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rect.x -= PLAYER_VELOCITY
        if keys[pygame.K_d]:
            self.rect.x += PLAYER_VELOCITY

        self.rect.y += self.velocity_y

        if self.rect.y >= HEIGHT - PLAYER_HEIGHT:
            self.rect.y = HEIGHT - PLAYER_HEIGHT
            self.velocity_y = 0
            self.on_ground = True

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (PLATFORM_WIDTH, random.randint(30,120)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.x -= PLATFORM_VELOCITY
        if self.rect.right < 0:
            self.rect.x = WIDTH + 200
            self.rect.y = random.randint(500, 590)

font = pygame.font.Font(None, 36)

def draw_score(score):
    text = font.render("Score: " + str(score), True, (1,1,1))
    screen.blit(text, (10, 10))
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

# Plattformen erstellen
platform_images = ["images/table.png"]  # Liste der Plattform-Bilder

for i in range(5):
    platform_image = random.choice(platform_images)
    platform = Platform(WIDTH + i * random.randint(PLATFORM_GAP, PLATFORM_GAP + 100),
                        random.randint(530, 550), platform_image)
    platforms.add(platform)
    all_sprites.add(platform)

S_TIME = time.time()  # Startzeit des Spiels
score = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and player.on_ground:
            player.image = pygame.image.load("images/c1_jump.png")
            player.image = pygame.transform.scale(player.image, (PLAYER_WIDTH, PLAYER_WIDTH))
            player.velocity_y -= JUMP_VELOCITY
            player.on_ground = False

    all_sprites.update()

    collision = pygame.sprite.spritecollide(player, platforms, False)
    if collision:
        # Korrigiere die Position des Spielers auf der Plattform
        player.image = pygame.image.load("images/c1_run.png")
        player.image = pygame.transform.scale(player.image, (PLAYER_WIDTH, PLAYER_WIDTH))
        player.rect.y = collision[0].rect.y - PLAYER_HEIGHT
        player.velocity_y = 0
        player.on_ground = True
        score += 10

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    draw_score(score)

    pygame.display.flip()
    clock.tick(60)
    print(score)

    TIMER = time.time() - S_TIME  # Verstrichene Zeit seit Spielbeginn
    if TIMER >= 3 and player.rect.y >= HEIGHT - PLAYER_HEIGHT:
        running = False

pygame.quit()
