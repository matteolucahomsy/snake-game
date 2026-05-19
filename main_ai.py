import pygame
import sys
import settings
from snake import Snake
from food import Food

pygame.init()
pygame.mixer.init()

screen= pygame.display.set_mode((settings.WIDTH,settings.HEIGHT))
pygame.display.set_caption("Snake AI")
clock= pygame.time.Clock()
font=pygame.font.SysFont(None,35)
snake=Snake()
food=Food()
score=0
high_score=0
state="PLAYING"
try:
    eat_sound=pygame.mixer.Sound("assets/eat.wav")
    gameover_sound=pygame.mixer.Sound("assets/gameover.wav")
except:
    eat_sound=None
    gameover_sound=None

def get_ai_direction(snake,food):
    head=snake.get_head()
    dx=food.position[0]-head[0]
    dy=food.position[1]-head[1]

    if abs(dx) > abs(dy):
        if dx>0:
            return [settings.BLOCK_SIZE, 0]
        else:
            return [-settings.BLOCK_SIZE,0]
    else:
        if dy>0:
            return [0, settings.BLOCK_SIZE]
        else:
            return [0,-settings.BLOCK_SIZE]
def draw_text(text,x,y):
    img=font.render(text,True, settings.WHITE)
    screen.blit(img,(x,y))
running=True
while running:
    screen.fill(settings.BLACK)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    if state=="PLAYING":
        snake.change_direction(*get_ai_direction(snake,food))
        snake.move()
        head=snake.get_head()

        if head[0] < 0 or head[0] >= settings.WIDTH or head[1] < 0 or head[1] >= settings.HEIGHT:
            state = "GAME_OVER"
            if gameover_sound:
                gameover_sound.play()

        
        if snake.check_self_collision():
            state = "GAME_OVER"
            if gameover_sound:
                gameover_sound.play()

        
        if head == food.position:
            food.respawn()
            snake.length += 1
            score += 1

            if score > high_score:
                high_score = score

            if eat_sound:
                eat_sound.play()

        
        pygame.draw.rect(
            screen,
            settings.RED,
            (food.position[0], food.position[1],
             settings.BLOCK_SIZE, settings.BLOCK_SIZE)
        )

        
        for part in snake.body:
            pygame.draw.rect(
                screen,
                settings.GREEN,
                (part[0], part[1],
                 settings.BLOCK_SIZE, settings.BLOCK_SIZE)
            )

        
        draw_text(f"Score: {score}", 10, 10)
        draw_text(f"High Score: {high_score}", 10, 40)

    elif state == "GAME_OVER":
        draw_text("GAME OVER", 200, 250)
        draw_text("Close window to exit", 170, 300)

    pygame.display.update()
    clock.tick(settings.SPEED)

pygame.quit()
sys.exit()


