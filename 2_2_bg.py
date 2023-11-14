import pygame
pygame.init()

w = 480
h = 640
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("팡팡게임")
# fps
clock = pygame.time.Clock()

background = pygame.image.load("C:\mac_dev_C\pygame_basic/background.png")

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

running = True
while running:
    dt = clock.tick(30)
    
    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

    # 3. 게임 캐릭터 위치 정의
    
    # 4. 충돌 처리

    # 5. 화면에 그리기

# pygame 종료
pygame.quit()
