import pygame
import random

WIDTH, HEIGHT = 800, 600

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Gesture Runner Game")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 40)

        self.reset()

    def reset(self):
        self.player = pygame.Rect(100, 450, 50, 50)
        self.velocity_y = 0
        self.gravity = 1
        self.is_jumping = False

        self.obstacles = []
        self.spawn_timer = 0

        self.score = 0
        self.speed = 5
        self.game_over = False

    def update(self, gesture):
        if self.game_over:
            return

        # Player movement
        if gesture == "LEFT":
            self.player.x -= 7
        elif gesture == "RIGHT":
            self.player.x += 7
        elif gesture == "JUMP" and not self.is_jumping:
            self.velocity_y = -15
            self.is_jumping = True

        # Gravity
        self.velocity_y += self.gravity
        self.player.y += self.velocity_y

        if self.player.y >= 450:
            self.player.y = 450
            self.is_jumping = False

        # Spawn obstacles
        self.spawn_timer += 1
        if self.spawn_timer > 40:
            self.obstacles.append(pygame.Rect(WIDTH, 450, 40, 40))
            self.spawn_timer = 0

        # Move obstacles
        for obs in self.obstacles:
            obs.x -= self.speed

        # Remove off-screen obstacles
        self.obstacles = [obs for obs in self.obstacles if obs.x > -50]

        # Collision detection
        for obs in self.obstacles:
            if self.player.colliderect(obs):
                self.game_over = True

        # Score
        self.score += 1

        # Increase difficulty
        if self.score % 500 == 0:
            self.speed += 1

    def draw(self):
        self.screen.fill((0, 0, 0))

        # Player
        pygame.draw.rect(self.screen, (0, 255, 0), self.player)

        # Obstacles
        for obs in self.obstacles:
            pygame.draw.rect(self.screen, (255, 0, 0), obs)

        # Score
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

        # Game Over
        if self.game_over:
            text = self.font.render("GAME OVER - Press R", True, (255, 0, 0))
            self.screen.blit(text, (200, 300))

        pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if self.game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.reset()
        return True

    def run(self, controller):
        running = True
        while running:
            gesture, _ = controller.get_gesture()
            running = self.handle_events()
            self.update(gesture)
            self.draw()
            self.clock.tick(30)

        pygame.quit()