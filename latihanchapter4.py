import pygame
pygame.init()

# Mengatur tampilan
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Game")

# Memuat gambar
image = pygame.image.load('contoh.jpg')

# Loop utama permainan
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Menggambar gambar
    screen.blit(image, (100, 100))

    # Memperbarui tampilan
    pygame.display.flip()

pygame.quit()
