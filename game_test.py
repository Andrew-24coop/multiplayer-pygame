import pygame
import sys
import os
import json

from settings import *

pygame.init()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class Game:
    def __init__(self):
        self.fullscreen = False
        self.fullscreen_status = "OFF"
        self.screen = pygame.display.set_mode(SIZE)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Echoes of Mercy")
        
        self.px, self.py = SIZE[0] // 2, SIZE[1] // 2
        self.player_speed = 5
        self.player_rect = pygame.Rect(self.px, self.py, 196, 240)

        self.main_menu_bg_img = pygame.transform.scale(pygame.image.load(resource_path('assets/img/main_menu_bg.png')).convert(), SIZE)
        self.credits_bg_img = pygame.transform.scale(pygame.image.load(resource_path('assets/img/credits_bg_img.png')).convert(), SIZE)
        self.sprite = pygame.transform.scale(pygame.image.load(resource_path('assets/img/image.png')).convert_alpha(), (196, 240))

        self.title_font = pygame.font.Font(resource_path("assets/fonts/main_menu_font.ttf"), 100)
        self.menu_font = pygame.font.Font(resource_path("assets/fonts/main_menu_font.ttf"), 65)

    def set_fullscreen(self, state):
        self.fullscreen = state
        self.fullscreen_status = "ON" if self.fullscreen else "OFF"
        if self.fullscreen:
            self.screen = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(SIZE)

    def show_credits(self):
        while True:
            self.screen.blit(self.credits_bg_img, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()
            self.clock.tick(FPS)

    def show_settings(self):
        while True:
            self.screen.fill(BLACK)

            title_text = self.title_font.render("Settings", False, WHITE)
            fullscreen_label = self.menu_font.render("Fullscreen:", False, WHITE)
            change_status = self.menu_font.render(self.fullscreen_status, False, WHITE)
            reset_progress = self.menu_font.render("Reset progress", False, WHITE)
            back_button = self.menu_font.render("Back", False, WHITE)

            title_rect = title_text.get_rect(center=(SIZE[0] // 2, SIZE[1] // 2 - 350))
            label_rect = fullscreen_label.get_rect(center=(SIZE[0] // 2 - 90, SIZE[1] // 2 - 150))
            status_rect = change_status.get_rect(center=(SIZE[0] // 2 + 250, SIZE[1] // 2 - 150))
            reset_rect = reset_progress.get_rect(center=(SIZE[0] // 2, SIZE[1] // 2 - 75))
            back_rect = back_button.get_rect(center=(SIZE[0] // 2, SIZE[1] // 2 + 300))

            self.screen.blit(title_text, title_rect)
            self.screen.blit(fullscreen_label, label_rect)
            self.screen.blit(change_status, status_rect)
            self.screen.blit(reset_progress, reset_rect)
            self.screen.blit(back_button, back_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if back_rect.collidepoint(event.pos):
                        return
                    if label_rect.collidepoint(event.pos) or status_rect.collidepoint(event.pos):
                        self.set_fullscreen(not self.fullscreen)

            pygame.display.flip()
            self.clock.tick(FPS)

    def new_game(self):
        while True:
            self.screen.fill(WHITE)
            
            current_fps = str(round(self.clock.get_fps()))
            fps_text = self.menu_font.render(current_fps, False, WHITE)
            self.screen.blit(fps_text, (5, 5))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.player_rect.y -= self.player_speed
            if keys[pygame.K_s]:
                self.player_rect.y += self.player_speed
            if keys[pygame.K_a]:
                self.player_rect.x -= self.player_speed
            if keys[pygame.K_d]:
                self.player_rect.x += self.player_speed

            self.player_rect.clamp_ip(self.screen.get_rect())

            self.screen.blit(self.sprite, self.player_rect.topleft)

            pygame.display.flip()
            self.clock.tick(FPS)

    def main_menu(self):
        while True:
            self.screen.fill(BLACK)

            title = self.title_font.render("Echoes of Mercy", False, WHITE)
            new_game_button = self.menu_font.render("New Game", False, WHITE)
            continue_button = self.menu_font.render("Continue", False, GRAY)
            settings_button = self.menu_font.render("Settings", False, WHITE)
            credits_button = self.menu_font.render("Credits", False, WHITE)
            exit_button = self.menu_font.render("Exit", False, WHITE)

            title_rect = title.get_rect(center=(SIZE[0] // 2, SIZE[1] // 2 - 350))
            new_game_rect = new_game_button.get_rect(center=(SIZE[0] // 2, SIZE[1] // 2 - 150))
            continue_rect = continue_button.get_rect(center=(SIZE[0] // 2, SIZE[1] // 2 - 75))
            settings_rect = settings_button.get_rect(center=(SIZE[0] // 2, SIZE[1] // 2))
            credits_rect = credits_button.get_rect(center=(SIZE[0] // 2, SIZE[1] // 2 + 75))
            exit_rect = exit_button.get_rect(center=(SIZE[0] // 2, SIZE[1] // 2 + 300))

            self.screen.blit(title, title_rect)
            self.screen.blit(new_game_button, new_game_rect)
            self.screen.blit(continue_button, continue_rect)
            self.screen.blit(settings_button, settings_rect)
            self.screen.blit(credits_button, credits_rect)
            self.screen.blit(exit_button, exit_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if new_game_rect.collidepoint(event.pos):
                        self.new_game()
                    if continue_rect.collidepoint(event.pos):
                        pass
                    if settings_rect.collidepoint(event.pos):
                        self.show_settings()
                    if credits_rect.collidepoint(event.pos):
                        self.show_credits()
                    if exit_rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

            pygame.display.flip()
            self.clock.tick(FPS)

    def run(self):
        self.main_menu()


if __name__ == "__main__":
    game = Game()
    game.run()

