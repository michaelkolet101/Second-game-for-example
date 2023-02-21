import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 500))


#שם תמונת רקע 
back_grund_img = pygame.image.load(r"C:\Users\micha\Desktop\seconde_game\IMAGS\bg_img.jpg").convert()
back_grund_img = pygame.transform.scale(back_grund_img, (500, 500))


# טיפול בגיבור

hero  = pygame.image.load(r"C:\Users\micha\Desktop\seconde_game\IMAGS\zord1.PNG").convert()
x_hero = 20
y_hero = 260
hero = pygame.transform.scale(hero, (200, 200))
hero.set_colorkey((255,255,255))

hero2  = pygame.image.load(r"C:\Users\micha\Desktop\seconde_game\IMAGS\zord2.PNG").convert()
x_hero2 = 20
y_hero2 = 260
hero2 = pygame.transform.scale(hero2, (200, 200))
hero2.set_colorkey((255,255,255))

hero3  = pygame.image.load(r"C:\Users\micha\Desktop\seconde_game\IMAGS\zord3.PNG").convert()
x_hero3 = 20
y_hero3 = 260
hero3 = pygame.transform.scale(hero3, (200, 200))
hero3.set_colorkey((255,255,255))



# טיפןל במפלצת
manster  = pygame.image.load(r"C:\Users\micha\Desktop\seconde_game\IMAGS\monster.jpg").convert()
x_manster = 200
y_manster = 260
manster = pygame.transform.scale(manster, (200, 200))
manster.set_colorkey((255,255,255))


heart1 = pygame.image.load(r"C:\Users\micha\Desktop\seconde_game\IMAGS\heart.png").convert()
heart1.set_colorkey("black")
heart1 = pygame.transform.scale(heart1, (50, 30))

flag = 0

finish = False

while finish != True:

    screen.blit(back_grund_img, (0, 0))
    screen.blit(manster, (x_manster, y_manster))

    x_manster -= 5
    if x_manster < -100:
        x_manster = 300

    if flag == 1: 
        screen.blit(hero2, (x_hero, y_hero))
        flag += 1
        pygame.time.delay(300)

    elif flag == 2: 
        screen.blit(hero3, (x_hero, y_hero))
        flag += 1
        pygame.time.delay(500)
        
    elif flag == 3:
    
        flag = 0
        pygame.time.delay(600)
    else:
        screen.blit(hero, (x_hero, y_hero))

         
    for i in range(0,71, 35):
        screen.blit(heart1, [i,0])
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    pygame.key.set_repeat(30)
                    y_hero += 10

                if event.key == pygame.K_UP:
                    pygame.key.set_repeat(30)
                    y_hero -= 10
                
                if event.key == pygame.K_LEFT:
                     pygame.key.set_repeat(30)
                     x_hero -= 10 

                if event.key == pygame.K_RIGHT:
                     pygame.key.set_repeat(30)
                     x_hero += 10 
                
                if event.key == pygame.K_SPACE:
                    flag = 1
                    


    pygame.display.update()
    clock.tick(10)