import pygame
import sys
from settings import *

pygame.init()
sc = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption("Window")

main_menu_bg_img = pygame.image.load('assets/img/main_menu_bg.png').convert()
main_menu_bg_img = pygame.transform.scale(main_menu_bg_img, SIZE)
credits_bg_img = pygame.image.load('assets/img/credits_bg_img.png').convert()
credits_bg_img = pygame.transform.scale(credits_bg_img, SIZE)

menu_font = pygame.font.Font("assets/fonts/main_menu_font.ttf", 65)


def show_credits():
    while True:
        sc.blit(credits_bg_img, (0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
 
        pygame.display.flip()
        clock.tick(FPS)


def new_game():
    sc.fill(GREEN)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(FPS)

def main():
    while True:
        # sc.blit(main_menu_bg_img, (0, 0))
        
        new_game_button = menu_font.render("New Game", False, WHITE)
        continue_button = menu_font.render("Continue", False, GRAY)
        settings_button = menu_font.render("Settings", False, WHITE)
        credits_button = menu_font.render("Credits", False, WHITE)
        exit_button = menu_font.render("Exit", False, WHITE)

        new_game_rect = new_game_button.get_rect(center=(SIZE[0] // 2, SIZE[1] // 2 - 150))
        continue_rect = continue_button.get_rect(center=(SIZE[0] // 2, SIZE[1] // 2 - 75))
        settings_rect = settings_button.get_rect(center=(SIZE[0] // 2, SIZE[1] // 2))
        credits_rect = credits_button.get_rect(center=(SIZE[0] // 2, SIZE[1] // 2 + 75))
        exit_rect = exit_button.get_rect(center=(SIZE[0] // 2, SIZE[1] // 2 + 150))

        sc.blit(new_game_button, new_game_rect)
        sc.blit(continue_button, continue_rect)
        sc.blit(settings_button, settings_rect)
        sc.blit(credits_button, credits_rect)
        sc.blit(exit_button, exit_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if new_game_rect.collidepoint(event.pos):
                    new_game()
                if continue_rect.collidepoint(event.pos):
                    continue
                if settings_rect.collidepoint(event.pos):
                    continue
                if credits_rect.collidepoint(event.pos):
                    show_credits()
                if exit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()

