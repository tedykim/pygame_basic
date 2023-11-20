#########################################################
import pygame

pygame.init() # 초기화 (반드시 필요)

# 1.화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 2.제목 설정
pygame.display.set_caption("팡팡 Game") # 게임 이름

# 3. 클럭,fps
clock = pygame.time.Clock()

# 4. 배경 이미지 불러오기
background = pygame.image.load("C:\mac_dev_C\pygame_basic/background.png")

# 5. 스프라이트_character 불러오기
character = pygame.image.load("C:\mac_dev_C\pygame_basic/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴

# 5.1 이동할 좌표
to_x = 0
to_y = 0

# 5.2 이동 속도
character_speed = 0.6 # 5에서 변경함

# 5.3 스프라이트_enemy
enemy = pygame.image.load("C:\mac_dev_C\pygame_basic/enemy.png")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0] # 캐릭터의 가로 크기
enemy_height = enemy_size[1] # 캐릭터의 세로 크기
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
enemy_y_pos = (screen_height / 2) - (enemy_height / 2) # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)


# 6. 폰트 정의
game_font = pygame.font.Font(None, 40) # 폰트 객체 생성 (폰트, 크기)
# 7. 총 시간
total_time = 10
# 7.1 시작 시간
start_ticks = pygame.time.get_ticks() # 현재 tick 을 받아옴

# 8. 이벤트 루프
running = True # 8.1 게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정
    
    for event in pygame.event.get(): # 8.2 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 8.3 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: # 8.4 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed # to_x = to_x - 5(5가아니라 0.6 일꺼야)

        if event.type == pygame.KEYUP: # 8.5 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x * dt   # 8.6 캐릭터 이동 속도유지(fps무관하게 동일속도) 
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False
    
    screen.blit(background, (0, 0)) # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # 적 그리기

    # 타이머 집어 넣기
    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    # 경과 시간(ms)을 1000으로 나누어서 초(s) 단위로 표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))
    # 출력할 글자, True, 글자 색상
    screen.blit(timer, (10, 10))

    # 만약 시간이 0 이하이면 게임 종료
    if total_time - elapsed_time <= 0:
        print("타임아웃")
        running = False

    pygame.display.update() # 게임화면을 다시 그리기!

# 잠시 대기
pygame.time.delay(2000) # 2초 정도 대기 (ms)

# pygame 종료
pygame.quit()