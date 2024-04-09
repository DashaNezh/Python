import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Настройки окна
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Симулятор игры в кости')

# Настройки шрифта
font = pygame.font.SysFont(None, 36)

# Загрузка изображений костей
dice_images = [pygame.image.load(f'dice{i}.png') for i in range(1, 7)]

# Список для сохранения истории бросков
roll_history = []


# Функция для отображения текста
def draw_text(text, pos):
    text_surf = font.render(text, True, (255, 255, 255))
    screen.blit(text_surf, pos)


# Основной цикл игры
running = True
waiting_for_input = True
while running:
    screen.fill((0, 0, 128))  # Заливка экрана цветом

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if waiting_for_input:
                if event.key == pygame.K_SPACE:
                    # Генерация случайного числа и сохранение в историю
                    roll = random.randint(1, 6)
                    roll_history.append(roll)
                    waiting_for_input = False
                elif event.key == pygame.K_h:
                    # Показать историю бросков
                    print("История бросков:", roll_history)
            if event.key == pygame.K_r:
                # Бросить кости снова
                waiting_for_input = True

    # Если не ждем ввода, отображаем результат броска
    if not waiting_for_input:
        dice_img = dice_images[roll - 1]
        screen.blit(dice_img,
                    (screen_width // 2 - dice_img.get_width() // 2, screen_height // 2 - dice_img.get_height() // 2))
        draw_text(f'Выпало: {roll}', (10, 10))

    draw_text('Нажмите пробел, чтобы бросить кости', (50, screen_height - 100))
    draw_text('Нажмите H, чтобы посмотреть историю', (50, screen_height - 50))
    draw_text('Нажмите R, чтобы сбросить и начать снова', (50, screen_height - 150))

    pygame.display.flip()
    pygame.time.wait(100)

# Выход из игры
pygame.quit()
sys.exit()
