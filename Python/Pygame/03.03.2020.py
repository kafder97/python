from random import randint
import pygame
pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 2000)# раз в 2 сек
W = 400
H = 400
WHITE = (255, 255, 255)
 
sc = pygame.display.set_mode((W, H))
CARS=('ded.png', 'ded.png')#список изображений
CARS_SURF=[]
 
pygame.mixer.music.load('Nooo.mp3')
pygame.mixer.music.play()
 
sound1 = pygame.mixer.music.load('1.mp3')
 
for i in range(len(CARS)):
    CARS_SURF.append(pygame.image.load(CARS[i]).convert())#добавление изображения
 
class Car(pygame.sprite.Sprite):#класс машин 
    def __init__(self, x, surf,group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, W))
        self.add(group)
        self.speed=(randint(1,5))
        self.image.set_colorkey((255,255,255))#добавил 
    def update(self):#обновление /изменяем св-ва класса за его пределами 
        if self.rect.y > -100:
            self.rect.y -= self.speed
        else:
            self.kill
 
cars = pygame.sprite.Group()#
Car(randint(25,W-25), CARS_SURF[0],cars)#создание первой машины - спрайта
 
class Car_up(pygame.sprite.Sprite):#класс машин едущих навстречу
    def __init__(self,x,surf):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(center=(x, 50))
        self.image.set_colorkey((255,255,255))
 
car_up=Car_up(200, CARS_SURF[1])#создание спрайта-машины едущей навстречу
sc.blit(car_up.image, car_up.rect)#
 
while 1:
    a=pygame.event.get()
    for i in a:
        if i.type== pygame.USEREVENT:#        
            Car(randint(25,W-25), CARS_SURF[0],cars)#создание новой машины
 
    keys = pygame.key.get_pressed()#отслеживает была ли зажата и какая кнопка
    if keys[pygame.K_RIGHT]:#вправо движение
        car_up.rect.x+=2
    elif keys[pygame.K_LEFT]:#влево движение
        car_up.rect.x-=2
 
    if pygame.sprite.spritecollide(car_up,cars,False):#если было соприкосновение одного с кем-то из группы то
        pygame.mixer.music.load('1.mp3')
        pygame.mixer.music.play()
        pygame.time.delay(4000)#задаем время после которого следует закрыть окно
        #умножать на 1000 нужно т.к. длина возвращается в секундах а не миллисекундах
        pygame.quit()#      то выход
 
    sc.fill(WHITE)#
    cars.draw(sc)#отрисовать поверх-ть
    sc.blit(car_up.image, car_up.rect)#отрисовать поверх-ть
    pygame.display.update()#обновить
    pygame.time.delay(20)
    cars.update()#обновить класс машин
