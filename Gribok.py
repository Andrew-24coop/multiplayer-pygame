import pygame
import sys

GAME_RES = 768, 384
FPS = 60

pygame.init()
sc = pygame.display.set_mode(GAME_RES)
clock = pygame.time.Clock()

b_img = pygame.image.load('img/background.png').convert()
b_img = pygame.transform.scale(b_img, GAME_RES)
l_img = pygame.image.load('img/loading_screen.jpg').convert()
l_img = pygame.transform.scale(l_img, GAME_RES)
c_img = pygame.image.load('img/credits.jpeg').convert()
c_img = pygame.transform.scale(c_img, GAME_RES)
grib_img = pygame.image.load('img/grib.png').convert_alpha()
grib_img = pygame.transform.scale(grib_img, (45, 45))
mario_img = pygame.image.load('img/mario.png').convert_alpha()
mario_img = pygame.transform.scale(mario_img, (36, 48))
block_img = pygame.image.load('img/block.png').convert_alpha()
block_img = pygame.transform.scale(block_img, (40, 40))
lucky_img = pygame.image.load('img/lucky_block.png').convert_alpha()
lucky_img = pygame.transform.scale(lucky_img, (40, 40))
coin_img = pygame.image.load("img/coin.png").convert_alpha()
coin_img = pygame.transform.scale(coin_img, (25, 25))

x, y = 50, 282
fall_speed = 0
gravity = 0.5
ground_y = 282
is_jumping = False
jump_count = 9

box_x, box_y = 650, 277
box_width, box_height = 36, 48
box_rect = pygame.Rect(box_x, box_y, box_width, box_height)

coin_count = 0
coins = []

lucky_block_positions = [
    pygame.Rect(175, 190, 40, 40),
    pygame.Rect(415, 190, 40, 40),
    pygame.Rect(495, 190, 40, 40)
]


def create_coins_on_block_collision(lucky_positions):
    for pos in lucky_positions:
        coins.append(pygame.Rect(pos.x + 7, pos.y - 27, 25, 25))


def show_credits():
    while True:
        sc.blit(c_img, (0, 0))
        font = pygame.font.Font("font/font.ttf", 25)
        return_text = font.render("Return", False, (255, 255, 255))
        font = pygame.font.Font("font/font.ttf", 50)
        credits_text = font.render("Credits", False, (255, 255, 255))
        developer_text = font.render("Developed by Jimbo83", False, (255, 255, 255))
        developer2_text = font.render("Assets by Mariia", False, (255, 255, 255))
        developer4_text = font.render("Idea by Oximoron", False, (255, 255, 255))

        credits_rect = credits_text.get_rect(center=(GAME_RES[0] // 2, GAME_RES[1] // 4 - 50))
        developer_rect = developer_text.get_rect(center=(GAME_RES[0] // 2, GAME_RES[1] // 2 - 50))
        developer2_rect = developer_text.get_rect(center=(GAME_RES[0] // 2, GAME_RES[1] // 2))
        developer4_rect = developer_text.get_rect(center=(GAME_RES[0] // 2, GAME_RES[1] // 2 + 60))
        return_rect = return_text.get_rect(topleft=(10, 10))

        sc.blit(credits_text, credits_rect)
        sc.blit(developer_text, developer_rect)
        sc.blit(developer2_text, developer2_rect)
        sc.blit(developer4_text, developer4_rect)
        sc.blit(return_text, return_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_rect.collidepoint(event.pos):
                    return

        pygame.display.flip()
        clock.tick(FPS)


def main_menu():
    while True:
        sc.fill((0, 0, 0))
        font = pygame.font.Font("font/font.ttf", 65)
        title = font.render("Gribok Oximoron", False, (255, 255, 255))
        start_button = font.render("Start", False, (255, 255, 255))
        exit_button = font.render("Exit", False, (255, 255, 255))
        credits_button = font.render("Credits", False, (255, 255, 255))

        title_rect = title.get_rect(center=(GAME_RES[0] // 2, GAME_RES[1] // 4 - 20))
        start_rect = start_button.get_rect(center=(GAME_RES[0] // 2, GAME_RES[1] // 2 - 10))
        exit_rect = exit_button.get_rect(center=(GAME_RES[0] // 2, GAME_RES[1] // 2 + 115))
        credits_rect = credits_button.get_rect(center=(GAME_RES[0] // 2, GAME_RES[1] // 2 + 55))

        sc.blit(l_img, (0, 0))
        sc.blit(title, title_rect)
        sc.blit(start_button, start_rect)
        sc.blit(exit_button, exit_rect)
        sc.blit(credits_button, credits_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos):
                    game_loop()
                if exit_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                if credits_rect.collidepoint(event.pos):
                    show_credits()

        pygame.display.flip()
        clock.tick(FPS)


def game_loop():
    global x, y, is_jumping, jump_count, fall_speed, coin_count, coins
    boxes = [
        pygame.Rect(375, 190, 40, 40),  # Block 1
        pygame.Rect(455, 190, 40, 40),  # Block 2
        pygame.Rect(535, 190, 40, 40),  # Block 3
        pygame.Rect(455, 70, 40, 40)  # Lucky block above
    ]

    while True:
        pygame.time.delay(20)
        sc.blit(b_img, (0, 0))
        # Draw lucky blocks
        for block_rect in lucky_block_positions:
            sc.blit(lucky_img, block_rect.topleft)

        # Draw the added coin at (592, 8)
        sc.blit(coin_img, (592, 8))

        # Draw coins after they are created
        for coin_rect in coins:
            sc.blit(coin_img, coin_rect.topleft)

        sc.blit(mario_img, (box_x, box_y))
        sc.blit(grib_img, (x, y))

        return_font = pygame.font.Font("font/font.ttf", 25)
        return_text = return_font.render("Return", False, (0, 0, 0))
        return_rect = return_text.get_rect(topleft=(10, 10))
        sc.blit(return_text, return_rect)

        # Draw the coin counter in the top-right corner
        coin_text = return_font.render(f'Coins: {coin_count}', True, (0, 0, 0))
        sc.blit(coin_text, (GAME_RES[0] - 150, 10))  # Adjust x to fit

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            x -= 5
        if key[pygame.K_RIGHT]:
            x += 5
        if key[pygame.K_UP] and not is_jumping:
            is_jumping = True

        if is_jumping:
            if jump_count >= -9:
                neg = 1
                if jump_count < 0:
                    neg = -1
                y -= (jump_count ** 2) * 0.5 * neg
                jump_count -= 1
            else:
                is_jumping = False
                jump_count = 9
        else:
            y += fall_speed
            fall_speed += gravity

        grib_rect = pygame.Rect(x, y, grib_img.get_width(), grib_img.get_height())

        # Check for collisions with lucky blocks
        for box_rect in lucky_block_positions:
            if grib_rect.colliderect(box_rect):
                if fall_speed < 0 and grib_rect.top <= box_rect.bottom:
                    y = box_rect.top - grib_img.get_height()
                    fall_speed = 0

                    # Call to create coins after hitting the lucky block
                    create_coins_on_block_collision([box_rect])  # Create coins above the block
                elif grib_rect.right > box_rect.left > grib_rect.left:
                    x = box_rect.left - grib_img.get_width()
                elif grib_rect.left < box_rect.right < grib_rect.right:
                    x = box_rect.right
                if grib_rect.bottom > box_rect.top > grib_rect.top:
                    if fall_speed <= 0:
                        y = box_rect.top - grib_img.get_height()

        # Check for collisions with boxes
        for box_rect in boxes:
            if grib_rect.colliderect(box_rect):
                if fall_speed > 0 and grib_rect.bottom <= box_rect.bottom:
                    y = box_rect.top - grib_img.get_height()
                    fall_speed = 0
                elif grib_rect.right > box_rect.left > grib_rect.left:
                    x = box_rect.left - grib_img.get_width()
                elif grib_rect.left < box_rect.right < grib_rect.right:
                    x = box_rect.right
                if grib_rect.bottom > box_rect.top > grib_rect.top:
                    if fall_speed <= 0:
                        y = box_rect.top - grib_img.get_height()

        # Check for collisions with coins
        for coin_rect in coins[:]:  # Copy of coins list for safe removal
            if grib_rect.colliderect(coin_rect):
                coins.remove(coin_rect)  # Remove coin upon collection
                coin_count += 1  # Increment coin count

        # Reset player position if hits the ground
        if y >= ground_y:
            y = ground_y
            fall_speed = 0

        # Boundary checks for player
        if x < 0:
            x = 0
        elif x > GAME_RES[0] - grib_img.get_width():
            x = GAME_RES[0] - grib_img.get_width()

        # Check for return button
        if return_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            main_menu()

        pygame.display.flip()
        clock.tick(FPS)


main_menu()
