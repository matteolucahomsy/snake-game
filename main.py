import pygame
import sys
import settings
from snake import Snake
from food import Food

pygame.init()
pygame.mixer.init()

screen= pygame.display.set_mode((settings.WIDTH,settings.HEIGHT))
pygame.display.set_caption("Snake Game")

clock= pygame.time.Clock()
font=pygame.font.SysFont(None,35)

eat_sound=pygame.mixer.Sound("assets/eat.wav")
gameover_sound=pygame.mixer.Sound("assets/gameover.wav")

snake= Snake()
food=Food()


score=0
high_score=0
speed=settings.SPEED + (score // 3)

state="MENU"
running=True

def draw_menu():
    screen.fill(settings.BLACK)
    title=font.render("SNAKE GAME",True,settings.WHITE)
    start=font.render("Press SPACE to start",True, settings.WHITE)

    screen.blit(title,(200,200))
    screen.blit(start,(150,260))
def draw_game_over():
    screen.fill(settings.BLACK)
    title=font.render("GAME OVER",True,settings.WHITE)
    start=font.render("Press R to restart",True, settings.WHITE)

    screen.blit(title,(220,200))
    screen.blit(start,(150,260))

# def load_high_score():
#     try:
#         with open("score.txt","r") as f:
#             return int(f.read())
#     except:
#         return 0
# def save_high_score(score):
#     with open("score.txt","w") as f:
#         f.write(str(score))
# high_score=load_high_score()


while running:
    screen.fill(settings.BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

        if event.type == pygame.KEYDOWN:
            if state == "MENU":
                if event.key == pygame.K_SPACE:
                    state="PLAYING"
            elif state == "GAME_OVER":
                snake.reset()
                food.respawn()
                score=0
                speed=settings.SPEED
                state = "PLAYING"
            elif state == "PLAYING":
                if event.key == pygame.K_LEFT:
                    snake.change_direction(-settings.BLOCK_SIZE,0)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(settings.BLOCK_SIZE,0)
                elif event.key == pygame.K_UP:
                    snake.change_direction(0,-settings.BLOCK_SIZE)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(0,settings.BLOCK_SIZE)
            
            
    if state == "PLAYING":
        snake.move()
        head=snake.get_head()

        if head[0] <0 or head[0]>= settings.WIDTH or head[1]<0 or head[1]>= settings.HEIGHT:
            state= "GAME_OVER"
            gameover_sound.play()
        if snake.check_self_collision():
            state="GAME_OVER"
            gameover_sound.play()
        if (head[0] < food.position[0] + settings.BLOCK_SIZE and head[0] + settings.BLOCK_SIZE > food.position[0] and head[1] < food.position[1] + settings.BLOCK_SIZE and head[1] + settings.BLOCK_SIZE > food.position[1]):
            food.respawn()
            snake.length +=1
            score+=1
            speed+=1
            eat_sound.play()
            if score>high_score:
                high_score=score
                

    

        pygame.draw.rect(
            screen,
            settings.RED,
            (food.position[0],food.position[1],settings.BLOCK_SIZE,settings.BLOCK_SIZE)
        )
        for part in snake.body:
            pygame.draw.rect(
                screen,
                settings.GREEN,
                (part[0],part[1], settings.BLOCK_SIZE, settings.BLOCK_SIZE)
            )
    
    
    score_text= font.render(
        f"Score: {score}",
        True,
        settings.WHITE
    )
    screen.blit(score_text, (10, 10))
    high_text=font.render(f"High Score: {high_score}",True,settings.WHITE)
    screen.blit(high_text,(10,40))
    
    if state == "MENU":
        draw_menu()
    elif state == "GAME_OVER":
        draw_game_over()
    pygame.display.update()
    clock.tick(speed)
pygame.quit()
sys.exit()
