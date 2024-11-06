import pygame,random


pygame.init()

screen = pygame.display.set_mode((1080,720),vsync=True)
pygame.display.set_caption('labirint')

#Инициализируем звуковой модуль
pygame.mixer.init()

#Загружаем музыку
menu_music = pygame.mixer.Sound("music/menu.mp3")
cristals_counds = [pygame.mixer.Sound("music/cristal_1.mp3"),pygame.mixer.Sound("music/cristal_2.mp3"),pygame.mixer.Sound("music/cristal_3.mp3"),pygame.mixer.Sound("music/cristal_4.mp3")]



gameplay = True
finish = False
#frames
clock = pygame.time.Clock()

#классы
class Boy:
    def __init__(self,image,x,y):
        self.image = image
        self.y = y
        self.x = x
class Girl:
    def __init__(self,image,x,y):
        self.image = image
        self.y = y
        self.x = x  
"""изображения"""
fireboy = Boy(pygame.transform.scale(pygame.image.load('images/Fireboy.png').convert_alpha(), (50, 75)),10,200)
watergirl = Girl(pygame.transform.scale(pygame.image.load('images/Watergirl.png').convert_alpha(), (55, 75)),1080-fireboy.x-50,200)

wasd = pygame.transform.scale(pygame.image.load('images/wasd.png').convert_alpha(), (170, 160))
qwer = pygame.transform.scale(pygame.image.load('images/keys.png').convert_alpha(), (170, 160))
finish_image = pygame.transform.scale(pygame.image.load('images/finish.png').convert_alpha(), (1080, 500))
pause_image = pygame.transform.scale(pygame.image.load('images/pause.png').convert_alpha(), (1080, 500))
finish_image_ = pygame.transform.scale(pygame.image.load('images/finish_.png').convert_alpha(), (1080, 500))
levels_image = pygame.transform.scale(pygame.image.load('images/levels.png').convert_alpha(), (1080, 500))
finish_image__ = pygame.transform.scale(pygame.image.load('images/finish__.png').convert_alpha(), (1080, 500))
menu_image = pygame.transform.scale(pygame.image.load('images/menu.png').convert_alpha(), (1080, 720))
#colors
red_color = (255,0,0)
blue_color = (0,0,255)
gold_color = (255,215,0)

#third_labirint
black_walls3 = [(0,0,0),[65,0,10,199],[65,280,10,240],[1080-65,0,10,199],[1080-65,280,10,240],[0,0,1080,10],[0,510,1080,10],[155,520-95-80,780,10],[245,520-5-80,690,100],[1080-75-80,10,10,520-180],[1080-75-90-200,220,220,10],[1080-75-560,100,400,10],[1080-75-560,100,10,165],[65,10,290,165],[1080-75-560-295,345,10,165],[1080-75-50-90-30,100,10,130],[340,255,110,10]]
bottoms_power3 = [0,0]
bottoms3 = [red_color,[1080-75-70-90-90-15,125,80,81],blue_color,[1080-75-70,10,80,80]]
labirint_homes3 = [red_color,[1080-75-70-90,139,80,81],blue_color,[162,430,82,80]]
walls3 = []





#secpnd labirint
black_walls2 = [(0,0,0),[65,0,10,99],[65,89,600,10],[655,89,10,100],[65,180,10,139],[65,180,600,10],[65,309,600,10],[655,309,10,100],[65,400,10,110],[65,400,600,10],[0,0,1080,10],[0,510,1080,10]]
bottoms_power2 = []
bottoms2 = []
labirint_homes2 = [red_color,[575,99,80,81],blue_color,[575,319,80,81]]
walls2 = []


#первый лаюиринт
labirint1 = [(0,0,0),[65,0,10,199],[65,280,10,240],[1080-65,0,10,199],[1080-65,280,10,240],[0,0,1080,10],[0,510,1080,10],[75,90,80,10],[155,520-95,1080-155-75-70,10],[1080-75-80,90,10,520-180],[1080-75-80-90,90,90,10],[1080-75-80-90,90,10,80],[1080-75-80-90-90,0,10,80],[1080-75-80-90-90,250,100,10],[1080-75-80-90-90,170,10,80],[155,335,1080-390,10],[1080-75-80-90-90-90,10,10,250],[1080-75-80-90-90-90-90,10,10,170],[155+10+90,10,10,90],[155+10+90,90,220,10],[1080-75-80-90-90-90-90-90,90,10,170],[155,250,230,10],[385,250,10,90]]

#b
#нажата кнопка или нет
labirint1_bottoms_power = [0,]
#расположение кнопок
labirint1_bottoms = [red_color,[310,260,75,75]]


#homes
labirint1_homes = [red_color,[845,100,80,80],blue_color,[75,10,80,80]]
labirint_homes_powers = [0,0]
#walls colored
walls1 = [red_color,[320,435,4,75],red_color,[751,80,4,90], blue_color,[845,250,80,4]]
class Labirintus():
    def __init__(self,labirint_black_walls,labirint_colored_walls,labirint_bottoms_power,labirint_bottoms,labirint_homes,x1=10,y1=200,x2=1020,y2=200,cristals = []):
        self.black_walls = labirint_black_walls
        self.bottoms_power=labirint_bottoms_power
        self.bottoms=labirint_bottoms
        self.homes=labirint_homes
        self.colored_walls = labirint_colored_walls
        self._copy = self.black_walls.copy()
        self.x1= x1
        self.y1= y1
        self.x2= x2
        self.y2= y2
        self.cristals = cristals
labirint_2= Labirintus(labirint1,walls1,labirint1_bottoms_power.copy(),labirint1_bottoms,labirint1_homes, cristals=[red_color,[304,43],blue_color,[359,471]])
labirint_3 = Labirintus(black_walls3,walls3,bottoms_power3.copy(),bottoms3,labirint_homes3, cristals=[red_color,[566,293],blue_color,[970,140]])


labirint_1 = Labirintus(black_walls2,walls2,bottoms_power2.copy(),bottoms2,labirint_homes2,10,100,10,320,[red_color,[222,138],blue_color,[222,365]])
#all the labirints
all_the_labirints = [labirint_1,labirint_3,labirint_2,]
all_the_labirints_info = [[],[0]]

#количество уровней
levels_exist = 3
#пройденные уровни
passed_levels = 0
#current
current_level = 1

def change_level(what_level):
    global all_the_labirints,all_the_labirints_info,fireboy,watergirl,current_level,labirint_2,labirint1,walls1,labirint1_bottoms_power,labirint1_bottoms,labirint1_homes
    if what_level<=passed_levels+1:
        
        

        current_level = what_level
        if all_the_labirints[current_level-1].bottoms_power:
            for i in range(len(all_the_labirints[current_level-1].bottoms_power)):
                all_the_labirints[current_level-1].bottoms_power[i] = 0
        fireboy.x =all_the_labirints[current_level-1].x1
        fireboy.y =all_the_labirints[current_level-1].y1
        watergirl.x =all_the_labirints[current_level-1].x2
        watergirl.y =all_the_labirints[current_level-1].y2
change_level(1)



#made
def is_home(person,labirint):
    global fireboy,watergirl,labirint_homes_powers
    
    for i in range(1,len(labirint.homes),2):
        if person == fireboy and labirint.homes[i-1] == red_color or person == watergirl and labirint.homes[i-1] == blue_color:
            if labirint.homes[i][0] <(person.x +25) < labirint.homes[i][0]  + labirint.homes[i][2] and labirint.homes[i][1] <(person.y +40) < labirint.homes[i][1]  + labirint.homes[i][3]:
                labirint_homes_powers[int((i-1)/2)] = 1
                
                return None
        labirint_homes_powers[int((i-1)/2)] = 0
#made
def are_home():
    global fireboy,watergirl, labirint_homes_powers,passed_levels,lcurrent_level,gameplay,finish
    if labirint_homes_powers[0] and labirint_homes_powers[1]:
        passed_levels=current_level
        gameplay = False
        finish = True
#made
def labirintum_homes(labirint):
    global screen
    for i in range(1,len(labirint.homes),2):
        pygame.draw.rect(screen,gold_color,labirint.homes[i]) 
        pygame.draw.rect(screen,labirint.homes[i-1],[labirint.homes[i][0]+20,labirint.homes[i][1]+20,40,40]) 


#made
def show_colored_walls(labirint):
    global screen
    for i in range(1,len(labirint.colored_walls),2):
        pygame.draw.rect(screen,labirint.colored_walls[i-1],labirint.colored_walls[i])
#made
def if_colored_wall(persona,labirint,way):
    global screen,watergirl,fireboy,red_color,blue_color
    size = 0; h = 0;color = red_color
    if persona == watergirl: size += 3; h+= 5;color=blue_color
    if way == 'right':
        for i in range(1,len(labirint.colored_walls),2):
            if persona.x + 50 + size-8+int(size/3*2) == labirint.colored_walls[i][0] and color!= labirint.colored_walls[i-1]:
                for z in range(persona.y+h+4,persona.y + 75-h):
                    if z in [y for y in range(labirint.colored_walls[i][1]+1,labirint.colored_walls[i][1] + labirint.colored_walls[i][3])] :
            
                        return False
            
    elif way=='left':
        for i in range(1,len(labirint.colored_walls),2):
            if persona.x+8+size == labirint.colored_walls[i][0] + labirint.colored_walls[i][2]and color!= labirint.colored_walls[i-1]:
                for z in range(persona.y+4+h,persona.y + 75-h):
                    if z in [y for y in range(labirint.colored_walls[i][1]+1,labirint.colored_walls[i][1] + labirint.colored_walls[i][3])] :
                        return False
            
    elif way=='up':

        for i in range(1,len(labirint.colored_walls),2):
            
            if persona.y+4+h == labirint.colored_walls[i][1] + labirint.colored_walls[i][3]and color!= labirint.colored_walls[i-1]:
                for z in range(persona.x+8+size,persona.x + 50 + size-8+int(size/3*2)):
                    if z in [x for x in range(labirint.colored_walls[i][0]+1,labirint.colored_walls[i][0] + labirint.colored_walls[i][2])] :
                        return False
            
            
    elif way=='down':
        for i in range(1,len(labirint.colored_walls)):
            
            if persona.y + 75-h == labirint.colored_walls[i][1]and color!= labirint.colored_walls[i-1]:
                for z in range(persona.x+8+size,persona.x + 50 + size-8+int(size/3*2)):
                    if z in [x for x in range(labirint.colored_walls[i][0]+1,labirint.colored_walls[i][0] + labirint.colored_walls[i][2])] :
                        return False
            
    return True


points = 0 
def labirintum_cristals(labirint):
    global screen
    
    for i in range(1,len(labirint.cristals),2):
        x = labirint.cristals[i][0]
        y = labirint.cristals[i][1]

        pygame.draw.polygon(screen,labirint.cristals[i-1],[(x-10,y),(x,y+15),(x+10,y),(x,y-15)])

def is_cristal(person,labirint):
    global fireboy,watergirl,points
    
    for i in range(1,len(labirint.cristals),2):
        if person == fireboy and labirint.cristals[i-1] == red_color or person == watergirl and labirint.cristals[i-1] == blue_color:
            if labirint.cristals[i][0]-5 <(person.x +25) < labirint.cristals[i][0]  + 5 and labirint.cristals[i][1]-10 <(person.y +40) < labirint.cristals[i][1]  + 30:
                points += 1
                labirint.cristals.pop(i-1)
                labirint.cristals.pop(i-1)
                cristals_counds[random.randint(0,3)].play()
                break
    else:
        return None
    is_cristal(person,labirint)
    

    


#made
def labirintum_bottoms(labirint):
    global screen
    for i in range(1,len(labirint.bottoms),2):
        pygame.draw.rect(screen,labirint.bottoms[i-1],labirint.bottoms[i])
#made
def is_bottom(person,labirint):
    global fireboy,watergirl
    
    for i in range(1,len(labirint.bottoms),2):
        if person == fireboy and labirint.bottoms[i-1] == red_color or person == watergirl and labirint.bottoms[i-1] == blue_color:
            if labirint.bottoms[i][0] <(person.x +25) < labirint.bottoms[i][0]  + labirint.bottoms[i][2] and labirint.bottoms[i][1] <(person.y +40) < labirint.bottoms[i][1]  + labirint.bottoms[i][3]:
                
                labirint.bottoms_power[int((i-1)/2)] = 1
    is_cristal(person,labirint)
                
                

                

def what_bottoms_do3():
    global screen,labirint_1,all_the_labirints_info,current_level




    
    
    labirint_2.black_walls = labirint_2._copy.copy()

    
    if labirint_2.bottoms_power[0]==0:
        pygame.draw.rect(screen,(61,237,151),[300,435,4,75])
        
        labirint_2.black_walls.append([300,435,4,75])
        pygame.draw.rect(screen,(61,237,151),[745,80,4,90])
        
        labirint_2.black_walls.append([745,80,4,90])
        pygame.draw.rect(screen,(61,237,151),[835,170,4,80])
        
        labirint_2.black_walls.append([835,170,4,80])
def what_bottoms_do2():
    global screen,labirint_3,all_the_labirints_info,current_level 
    labirint_3.black_walls = labirint_3._copy.copy()

    
    if labirint_3.bottoms_power[1]==0:
        pygame.draw.rect(screen,(61,237,151),[342,175,4,80])
        
        labirint_3.black_walls.append([342,175,4,80])
    if labirint_3.bottoms_power[0]==0:
        pygame.draw.rect(screen,(61,237,151),[930,355,4,80])
        
        labirint_3.black_walls.append([930,355,4,80])
        




#строит лабиринт(стены)
def labirintum(labirint):
    global screen,fireboy,watergirl
    for i in range(1,len(labirint.black_walls)):
        pygame.draw.rect(screen,labirint.black_walls[0],labirint.black_walls[i])
    labirintum_bottoms(labirint)
    labirintum_cristals(labirint)
    show_colored_walls(labirint)
    labirintum_homes(labirint)
    screen.blit(fireboy.image,(fireboy.x,fireboy.y))
    screen.blit(watergirl.image,(watergirl.x,watergirl.y))
#made
def check_wall(persona,labirint,way):
    global screen,watergirl,fireboy
    
    size = 0; h = 0
    if persona == watergirl: size += 3; h+= 5
    if way == 'right':
        for i in range(1,len(labirint.black_walls)):
            if persona.x + 50 + size-8+int(size/3*2) == labirint.black_walls[i][0]:
                for z in range(persona.y+h+4,persona.y + 75-h):
                    if z in [y for y in range(labirint.black_walls[i][1]+1,labirint.black_walls[i][1] + labirint.black_walls[i][3])] :
            
                        return False
    elif way=='left':
        for i in range(1,len(labirint.black_walls)):
            if persona.x+8+size == labirint.black_walls[i][0] + labirint.black_walls[i][2]:
                for z in range(persona.y+4+h,persona.y + 75-h):
                    if z in [y for y in range(labirint.black_walls[i][1]+1,labirint.black_walls[i][1] + labirint.black_walls[i][3])] :
                        return False
    elif way=='up':
        for i in range(1,len(labirint.black_walls)):
            
            if persona.y+4+h == labirint.black_walls[i][1] + labirint.black_walls[i][3]:
                for z in range(persona.x+8+size,persona.x + 50 + size-8+int(size/3*2)):
                    if z in [x for x in range(labirint.black_walls[i][0]+1,labirint.black_walls[i][0] + labirint.black_walls[i][2])] :
                        return False
            
    elif way=='down':
        for i in range(1,len(labirint.black_walls)):
            
            if persona.y + 74-h == labirint.black_walls[i][1]:
                for z in range(persona.x+8+size,persona.x + 50 + size-8+int(size/3*2)):
                    if z in [x for x in range(labirint.black_walls[i][0]+1,labirint.black_walls[i][0] + labirint.black_walls[i][2])] :
                        return False
    return True and if_colored_wall(persona,labirint,way)

#нижнее меню
def bottom_menu():
    global  screen,wasd,qwer,points,current_level,passed_levels
    pygame.draw.rect(screen,(179, 107, 0),[0,520,1080,200])
    pygame.draw.rect(screen, (255, 204, 153),[20,540,1040,160])
    
    screen.blit(wasd,(25,540))
    screen.blit(qwer,(890,540))
    text_result = pygame.font.SysFont('sand', 65).render(f'Очки: {points + passed_levels*5}', 0,(30,100,75))
    screen.blit(text_result,(640,655) )
    text_result = pygame.font.SysFont('sand', 65).render(f'Пройдено: {passed_levels}', 0,(30,100,75))
    screen.blit(text_result,(220,655) )
    text_result = pygame.font.SysFont('sand', 65).render(f'Уровень: {current_level}', 0,(30,100,75))
    screen.blit(text_result,(430,550) )
    
the_bottom = 0
pause = False
running = True
menu = True
gameplay = False
level_menu = False
has_been_played = False
while running:

    
    pygame.display.update()
    #backgroundcolor rgb
    screen.fill((240,240,240))
    mouse = pygame.mouse.get_pos()
    if level_menu:
        
        if not has_been_played:
            menu_music.play(loops=-1)
            has_been_played = True
    
        
        screen.fill((0,0,0))
        screen.blit(levels_image,(0,0))
        for i in range(levels_exist):
            stars = 0
            if i < passed_levels:
                stars += 2
                if all_the_labirints[i].cristals == []:
                    stars += 1
            elif i == passed_levels:
                stars += 1
            
            if stars == 0: 
                color = (99,0,15)
            elif stars == 1: 
                color = (100,100,100)
            elif stars == 2: 
                color = (200,50,20)
            else: color = (0,210,0)
            text_result = pygame.font.SysFont('sand', 110).render(str(i), 0, (255,255,255))
            
            if i <= 6:
                pygame.draw.rect(screen, color,[20 + 80 * 2*i,150,80,80])
                screen.blit(text_result, (38+80 * 2*i,157))
            elif i <= 13:
                pygame.draw.rect(screen, color,[20 + 80 * 2*i,150+160,80,80])
                screen.blit(text_result, (38+80 * 2*i,157+160))
    elif not(menu or level_menu):
        try:
            menu_music.stop()
        except:
            None

    if menu:
        screen.blit(menu_image,(0,0))
        if not has_been_played:
            menu_music.play(loops=-1)
            has_been_played = True
    elif not(menu or level_menu):
        try:
            menu_music.stop()
        except:
            None

    if finish:
         
        screen.fill((240,240,240))
        bottom_menu()
        
        
        
                
            
        if 1<current_level<levels_exist:
            screen.blit(finish_image,(0,10))
            if the_bottom == 1:
                change_level(current_level+1)
                finish = False
                gameplay = True
            if the_bottom == 2:
                change_level(current_level-1)
                finish = False
                gameplay = True
        elif current_level == 1:
            screen.blit(finish_image__,(0,10))
            if the_bottom == 1:
                change_level(current_level+1)
                finish = False
                gameplay = True
                
        else: 
            if the_bottom == 2:
                change_level(current_level-1)
                finish = False
                gameplay = True
            screen.blit(finish_image_,(0,10))
        the_bottom = 0



        
        for i in range(len([[0,0,10,520],[1070,0,10,520],[0,0,10,1080],[0,510,10,1080]])):
            pygame.draw.rect(screen,(0,0,0),[[0,0,10,520],[1070,0,10,520],[0,0,1080,10],[0,510,1080,10]][i])
    if gameplay:
        labirintum(all_the_labirints[current_level-1])
        
        
        bottom_menu()
        #update the screen
        
        is_bottom(fireboy,all_the_labirints[current_level-1])
        is_bottom(watergirl,all_the_labirints[current_level-1])
        is_home(watergirl,all_the_labirints[current_level-1])
        is_home(fireboy,all_the_labirints[current_level-1])
        are_home()
        if current_level == 2:
            
            what_bottoms_do2()
        elif current_level == 3:
            what_bottoms_do3()




        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if fireboy.y >= 5:
                for i in range(1,6):
                    if check_wall(fireboy,all_the_labirints[current_level-1],'up'):fireboy.y -= 1
        if keys[pygame.K_s]:
            if fireboy.y <= 440:
                for i in range(1,6):
                    if check_wall(fireboy,all_the_labirints[current_level-1],'down'):fireboy.y += 1
            
        if keys[pygame.K_d]:
            if fireboy.x <= 1025:
                for i in range(1,6):
                    if check_wall(fireboy,all_the_labirints[current_level-1],'right'):fireboy.x += 1
        if keys[pygame.K_a]:
            if fireboy.x >= 5:
                for i in range(1,6):
                    if check_wall(fireboy,all_the_labirints[current_level-1],'left'):fireboy.x -= 1


        if keys[pygame.K_UP]:
            if watergirl.y >= 5:
                for i in range(1,6):
                    if check_wall(watergirl,all_the_labirints[current_level-1],'up'):watergirl.y -= 1
        if keys[pygame.K_DOWN]:
            if watergirl.y <= 445:
                for i in range(1,6):
                    if check_wall(watergirl,all_the_labirints[current_level-1],'down'):watergirl.y += 1
            
        if keys[pygame.K_RIGHT]:
            if watergirl.x <= 1025:
                for i in range(1,6):
                    if check_wall(watergirl,all_the_labirints[current_level-1],'right'):watergirl.x += 1
        if keys[pygame.K_LEFT]:
            if watergirl.x >= 5:
                for i in range(1,6):
                    if check_wall(watergirl,all_the_labirints[current_level-1],'left'):watergirl.x -= 1
        if keys[pygame.K_1]:
            change_level(1)
        if keys[pygame.K_2]:
            change_level(2)
        if keys[pygame.K_3]:
            change_level(3)
    if pause:
        screen.fill((240,240,240))
        bottom_menu()
        screen.blit(pause_image,(0,10))
        for i in range(len([[0,0,10,520],[1070,0,10,520],[0,0,10,1080],[0,510,10,1080]])):
            pygame.draw.rect(screen,(0,0,0),[[0,0,10,520],[1070,0,10,520],[0,0,1080,10],[0,510,1080,10]][i])
        
        
        
                
            
        
        
    clock.tick(30)

    for event in pygame.event.get():
        #if event is quit
        if event.type == pygame.QUIT:
            running=False 
            pygame.mixer.music.unload()
            pygame.quit() 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and not finish:
                if pause:
                    pause = False
                    gameplay = True
                else:
                    pause = True
                    gameplay = False
        elif event.type == pygame.MOUSEBUTTONDOWN: 
                print(mouse[0],mouse[1])
                #if the mouse is clicked on the 
                # button the game is terminated 
                if 438 <= mouse[0] <= 668 and 154 <= mouse[1] <= 211 and finish and current_level<levels_exist: 
                    
                    the_bottom = 1
                elif 438 <= mouse[0] <= 668 and 230 <= mouse[1] <= 280 and finish and current_level>1: 
                    
                    the_bottom = 2
                elif 438 <= mouse[0] <= 668 and 164 <= mouse[1] <= 201 and pause:
                    pause = False
                    gameplay = True
                elif 438 <= mouse[0] <= 668 and 230 <= mouse[1] <= 280 and pause:
                    change_level(current_level)
                    pause = False
                    gameplay = True
                elif 365 <= mouse[0] <= 533 and 314 <= mouse[1] <= 368 and (pause or finish):
                    pause = False
                    finish = False
                    has_been_played = False
                    menu = True
                elif 396 <= mouse[0] <= 682 and 24 <= mouse[1] <= 92 and level_menu:
                    pause = False
                    finish = False
                    level_menu = False
                    
                    menu = True
                elif 556 <= mouse[0] <= 730 and 314 <= mouse[1] <= 368 and (pause or finish):
                    pause = False
                    finish = False
                    level_menu = True
                    has_been_played = False
                    gameplay = False
                    menu = False
                elif 376 <= mouse[0] <= 660 and 373 <= mouse[1] <= 438 and menu:
                    menu = False
                    level_menu = True
                elif 376 <= mouse[0] <= 660 and 278 <= mouse[1] <= 340 and menu:
                    
                    change_level(current_level)
                    menu = False
                    gameplay = True
                elif 376 <= mouse[0] <= 660 and 455 <= mouse[1] <= 530 and menu:
                    running=False
                    pygame.mixer.music.unload() 
                    pygame.quit() 
                    
                elif level_menu:
                    for i in range(levels_exist):
                        if i <= passed_levels:
                            if i <= 6:
                                if 20 + 80 * 2*i <= mouse[0] <= 100 + 80 * 2*i and 150 <= mouse[1] <= 230:
                                    change_level(i+1)
                                    gameplay = True
                                    level_menu = False
                                    has_been_played = False
                            elif i <= 13:
                                if 20 + 80 * 2*i <= mouse[0] <= 100 + 80 * 2*i and 310 <= mouse[1] <= 390:
                                    change_level(i+1)
                                    gameplay = True
                                    level_menu = False
                                    has_been_played = False
                
                        
                            
