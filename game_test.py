import pygame
from settings import *

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)
pygame.display.set_caption("Window")

font = pygame.font.SysFont(None, 60)

current_width, current_height = WIDTH, HEIGHT
is_fullscreen = True


def draw_text(text, color, rect, center=True):
    text_surf = font.render(text, True, color)
    if center:
        screen.blit(text_surf, text_surf.get_rect(center=rect.center))
    else:
        screen.blit(text_surf, rect)


def draw_button(rect, text, selected=False):
    color = RED if selected else BLACK
    pygame.draw.rect(screen, WHITE, rect)
    pygame.draw.rect(screen, color, rect, 3)
    draw_text(text, color, rect)


def main_menu():
    menu_options = ["New Game", "Settings"]
    selected_index = 0
    in_menu = True

    while in_menu:
        screen.fill(WHITE)
        rects = []

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_index = (selected_index + 1) % len(menu_options)
                elif event.key == pygame.K_UP:
                    selected_index = (selected_index - 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if selected_index == 0:
                        in_menu = False
                    elif selected_index == 1:
                        settings_menu()
            elif event.type == pygame.MOUSEMOTION:
                mx, my = pygame.mouse.get_pos()
                for i, opt in enumerate(menu_options):
                    rect = pygame.Rect(current_width // 2 - 150, current_height // 2 - 40 + i * 80, 300, 60)
                    if rect.collidepoint(mx, my):
                        selected_index = i
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for i, opt in enumerate(menu_options):
                    rect = pygame.Rect(current_width // 2 - 150, current_height // 2 - 40 + i * 80, 300, 60)
                    if rect.collidepoint(mx, my):
                        if i == 0:
                            in_menu = False
                        elif i == 1:
                            settings_menu()

        for i, opt in enumerate(menu_options):
            rect = pygame.Rect(current_width // 2 - 150, current_height // 2 - 40 + i * 80, 300, 60)
            draw_button(rect, opt, selected=i == selected_index)
            rects.append(rect)

        pygame.display.flip()
        clock.tick(FPS)


def settings_menu():
    global is_fullscreen, screen
    
    setting_x = 200
    option_x = current_width - 300
    row_y = current_height // 2 - 60
    spacing = 100

    in_settings = True

    while in_settings:
        screen.fill(WHITE)

        fullscreen_rect = pygame.Rect(option_x, row_y, 120, 50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    in_settings = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if fullscreen_rect.collidepoint(mx, my):
                    toggle_fullscreen()

        draw_text("Fullscreen", BLACK, pygame.Rect(setting_x, row_y, 200, 50), center=False)

        pygame.draw.rect(screen, BLACK, fullscreen_rect, 3)
        pygame.draw.rect(screen, GREEN if is_fullscreen else RED, fullscreen_rect.inflate(-10, -10))
        toggle_text = "On" if is_fullscreen else "Off"
        draw_text(toggle_text, BLACK, fullscreen_rect)

        pygame.display.flip()
        clock.tick(FPS)


def toggle_fullscreen():
    global is_fullscreen, screen
    is_fullscreen = not is_fullscreen
    screen = pygame.display.set_mode((current_width, current_height), pygame.FULLSCREEN if is_fullscreen else 0)


def main():
    main_menu()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(BLUE)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
