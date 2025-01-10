import random
import constants

def check_collision(ball_x, ball_y, paddle_x, paddle_y, paddle_width, paddle_height):
    # Cek apakah bola mengenai bagian bawah paddle
    if (paddle_x < ball_x < paddle_x + paddle_width) and (paddle_y < ball_y + constants.BALL_RADIUS <= paddle_y + paddle_height):
        return True
    return False

def update_ball_position(ball_x, ball_y, ball_speed_y, paddle_x, paddle_y, paddle_width, paddle_height):
    ball_y += ball_speed_y

    # Periksa tabrakan bola dengan paddle
    if check_collision(ball_x, ball_y, paddle_x, paddle_y, paddle_width, paddle_height):
        ball_y = paddle_y - constants.BALL_RADIUS  # Reset bola di atas paddle
        return ball_x, ball_y, True  # Tabrakan terjadi, kembalikan status tabrakan

    # Jika bola mencapai bawah layar tanpa tabrakan
    if ball_y > constants.SCREEN_HEIGHT:
        ball_x = random.randint(constants.BALL_RADIUS, constants.SCREEN_WIDTH - constants.BALL_RADIUS)
        ball_y = constants.BALL_RADIUS

    return ball_x, ball_y, False  # Tidak ada tabrakan
