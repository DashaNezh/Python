import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Настройки окна
screen_width = 640
screen_height = 525
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Симулятор игры в кости')

# Настройки шрифта
font = pygame.font.SysFont('Arial', 24, bold=True)

# Загрузка изображений костей
dice_images = [pygame.image.load(f'dice{i}.png') for i in range(1, 7)]

# Список для сохранения истории бросков
roll_history = []

# Переменные для состояния игры
showing_history = False
waiting_for_roll = True
roll = 0
message_show_time = 3000  # Время отображения сообщения в миллисекундах (3000 мс = 3 секунды)
message_start_time = 0  # Время начала отображения сообщения
show_message = False  # Показываем сообщение или нет


# Функция для отображения текста
def draw_text(text, pos, color=(255, 255, 255)):
    text_surf = font.render(text, True, color)
    text_rect = text_surf.get_rect(center=(pos[0], pos[1]))
    screen.blit(text_surf, text_rect)

# Функция для отображения истории бросков в виде таблицы
def draw_history(history, background_color):
    max_history = 10  # Устанавливаем максимальное количество отображаемых бросков
    start_index = max(0, len(history) - max_history)  # Стартовый индекс для отображения

    # Закрашиваем фон для таблицы
    background_rect = pygame.Rect(50, 50, screen_width - 100, screen_height - 100)
    pygame.draw.rect(screen, background_color, background_rect)

    # Столбцы и ширина столбцов
    columns = ['№', 'Бросок']
    column_widths = [50, 100]

    # Рисуем заголовки столбцов
    for col_num, title in enumerate(columns):
        draw_text(title, (50 + sum(column_widths[:col_num]) + column_widths[col_num] // 2, 70), color=(0, 0, 0))

    # Выводим строки бросков
    for i in range(start_index, len(history)):
        # Рисуем номер броска
        draw_text(f'{i + 1}', (50 + column_widths[0] // 2, 90 + (i - start_index) * 40), color=(0, 0, 0))
        # Рисуем значение броска
        draw_text(f'{history[i]}', (50 + sum(column_widths[:1]) + column_widths[1] // 2, 90 + (i - start_index) * 40), color=(0, 0, 0))

# Изменения в основном цикле игры
max_rolls = 10  # Максимальное количество бросков
roll_limit_reached = False  # Переменная для отслеживания достижения лимита


# Функция для отображения кнопки
def draw_button(text, pos, size, color, text_color):
    button_rect = pygame.Rect(pos, size)
    pygame.draw.rect(screen, color, button_rect)
    draw_text(text, (pos[0] + size[0] * 0.5, pos[1] + size[1] * 0.5), color=text_color)
    return button_rect


# Основной цикл игры
running = True
while running:
    current_time = pygame.time.get_ticks()
    screen.fill((3, 52, 122))  # Основной фон окна

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = event.pos
            if 'back_button' in locals() and back_button.collidepoint(mouse_pos):
                showing_history = False
            if 'exit_button' in locals() and exit_button.collidepoint(mouse_pos):
                running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not showing_history:
                roll = random.randint(1, 6)
                roll_history.append(roll)
                waiting_for_roll = False
            elif event.key == pygame.K_h:
                showing_history = True
            elif event.key == pygame.K_r:
                waiting_for_roll = True
                showing_history = False

    if showing_history:
        draw_history(roll_history, background_color=(216, 216, 216))
        back_button = draw_button('Назад', (screen_width - 200, screen_height - 50), (150, 40), color=(123, 164, 40),
                                  text_color=(255, 255, 255))
    else:
        if not waiting_for_roll:
            dice_img = dice_images[roll - 1]
            screen.blit(dice_img, (
            screen_width // 2 - dice_img.get_width() // 2, screen_height // 2 - dice_img.get_height() // 2))
            draw_text(f'Выпало: {roll}', (screen_width // 2, 15), color=(255, 213, 0))

        draw_text('Нажмите пробел, чтобы бросить кости', (screen_width // 2, screen_height - 100))
        draw_text('Нажмите H, чтобы посмотреть историю', (screen_width // 2, screen_height - 50))
        draw_text('Нажмите R, чтобы сбросить и начать снова', (screen_width // 2, screen_height - 150))

    # Проверка, достигнут ли лимит бросков
    if len(roll_history) >= max_rolls and not roll_limit_reached:
        roll_limit_reached = True
        show_message = True
        message_start_time = current_time  # Установка таймера для сообщения

    # Проверка таймера для автоматического скрытия сообщения
    if show_message and current_time - message_start_time > message_show_time:
        show_message = False
        roll_limit_reached = False  # Сброс флага достижения лимита для новых бросков

    # Отображение сообщения, если требуется
    if show_message:
        draw_text('Лимит бросков достигнут!', (screen_width // 2, screen_height - 180),
                    color=(230, 55, 55))
        roll_history.clear()
        roll_limit_reached = False

    # Добавляем кнопку выхода из игры
    exit_button = draw_button('Выход', (screen_width - 150, screen_height - 515), (100, 40), color=(200, 0, 0),
                              text_color=(255, 255, 255))

    pygame.display.flip()
    pygame.time.wait(100)

# Выход из игры
pygame.quit()
sys.exit()