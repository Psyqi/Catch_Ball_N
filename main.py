import pygame
import random
import cv2
import game_logic
import detection
import constants

# Inisialisasi PyGame
pygame.init()
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("Tangkap Bola dengan Telunjuk")

# Memuat aset visual
ball_image = pygame.image.load("assets/images/ball2.png")
paddle_image = pygame.image.load("assets/images/paddle3.png")
background_image = pygame.image.load("assets/images/background2.jpg")

# Inisialisasi kamera
cap = cv2.VideoCapture(0)

# Game loop
def main():
    ball_x = random.randint(constants.BALL_RADIUS, constants.SCREEN_WIDTH - constants.BALL_RADIUS)
    ball_y = constants.BALL_RADIUS
    ball_speed_y = 5
    score = 0
    paddle_x = (constants.SCREEN_WIDTH - constants.PADDLE_WIDTH) // 2

    # Mulai deteksi tangan
    with detection.HandTracking() as hand_tracker:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Baca frame dari kamera
            ret, frame = cap.read()
            if not ret:
                break

            # Deteksi tangan dan dapatkan posisi telunjuk
            finger_x = hand_tracker.detect_hand(frame)

            # Update posisi paddle
            paddle_x = hand_tracker.update_paddle_position(finger_x, paddle_x)

            # Update posisi bola
            # Pastikan untuk mengimpor dan menggunakan game_logic.update_ball_position dengan benar
            ball_x, ball_y, collided = game_logic.update_ball_position(ball_x, ball_y, ball_speed_y, paddle_x, 
            constants.SCREEN_HEIGHT - constants.PADDLE_HEIGHT - 10,
            constants.PADDLE_WIDTH, constants.PADDLE_HEIGHT)


            # Jika bola bertabrakan dengan paddle, tambah skor
            if collided:
                score += 1
                ball_speed_y += 0.5
                ball_x = random.randint(constants.BALL_RADIUS, constants.SCREEN_WIDTH - constants.BALL_RADIUS)
                ball_y = constants.BALL_RADIUS

            # Gambar background, bola, dan paddle
            screen.fill(constants.WHITE)
            screen.blit(background_image, (0, 0))
            screen.blit(paddle_image, (paddle_x, constants.SCREEN_HEIGHT - constants.PADDLE_HEIGHT - 10))
            screen.blit(ball_image, (ball_x - constants.BALL_RADIUS, ball_y - constants.BALL_RADIUS))

            # Tampilkan score
            font = pygame.font.Font(None, 36)
            score_text = font.render(f"Score: {score}", True, constants.BLACK)
            screen.blit(score_text, (10, 10))

            # Update tampilan
            pygame.display.flip()

            # Tampilkan frame untuk debugging
            cv2.imshow('Kamera', frame)

            # Keluar jika 'q' ditekan
            if cv2.waitKey(1) & 0xFF == ord('q'):
                running = False

    # Bersihkan sumber daya
    cap.release()
    cv2.destroyAllWindows()
    pygame.quit()

if __name__ == "__main__":
    main()
