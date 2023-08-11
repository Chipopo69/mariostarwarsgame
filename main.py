import pygame
import random

# Initialize Pygame
pygame.init()

# Define screen dimensions
screen_width = 800
screen_height = 600

# Load music and character images
bg_music = pygame.mixer.Sound("music.wav")
mario_img = pygame.image.load("mario.png")
luigi_img = pygame.image.load("luigi.png")
goomba_img = pygame.image.load("goomba.png")
koopatroopa_img = pygame.image.load("koopatroopa.png")

# Sets the character's starting position
mario_x = 200
mario_y = 300
luigi_x = 300
luigi_y = 300

# Create Pygame window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Super Mario Game")

clock = pygame.time.Clock()

class Mario:
    def __init__(self, x, y):
        self.image = mario_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.power = 0

    def draw(self):
        screen.blit(self.image, self.rect)

class Luigi:
    def __init__(self, x, y):
        self.image = luigi_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.power = 0

    def draw(self):
        screen.blit(self.image, self.rect)

class Enemy:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.power = 0

class Goomba(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = goomba_img

    def draw(self):
        screen.blit(self.image, self.rect)

class KoopaTroopa(Enemy):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = koopatroopa_img

    def draw(self):
        screen.blit(self.image, self.rect)

# Levels and Power-ups
levels = {
    "Level 1": {
        "power_ups": ["Fire Flower", "Mushroom"],
        "enemies": [Goomba(400, 300), Goomba(500, 300), Goomba(600, 300)]
    },
    "Level 2": {
        "power_ups": ["Mushroom"],
        "enemies": [Goomba(400, 300), Goomba(500, 300), KoopaTroopa(600, 300)]
    },
    "Level 3": {
        "power_ups": ["Star"],
        "enemies": [KoopaTroopa(400, 300), KoopaTroopa(500, 300)]
    },
    # Define remaining levels similarly
}

def choose_character():
    print("Choose your character:")
    print("1. Mario")
    print("2. Luigi")
    choice = input("Enter your choice (1/2): ")
    if choice == '1':
        return Mario(mario_x, mario_y)
    elif choice == '2':
        return Luigi(luigi_x, luigi_y)
    else:
        return None

def play_level(level):
    current_power_ups = levels[level]["power_ups"]
    current_enemies = levels[level]["enemies"]

    print(f"Level: {level}")
    print("Power ups:", current_power_ups)
    print("Enemies:", len(current_enemies))
    print()

    running = True
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for power_up in current_power_ups:
            pygame.draw.rect(screen, (255, 0, 0), (random.randint(0, screen_width), random.randint(0, screen_height), 20, 20))

        for enemy in current_enemies:
            enemy.draw()

        character.draw()

        pygame.display.update()
        clock.tick(60)

# Start background music
bg_music.play()

character = choose_character()
if character:
    for level in levels:
        play_level(level)
else:
    print("Invalid character choice.")

# Quit Pygame
pygame.quit()
