from pygame import*


okno = display.set_mode((1100,800))
clock = time.Clock()





class GameBB(sprite.Sprite):
    def __init__(self, img, x,y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(img), (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def ris(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))




class player(GameBB):
    def control(self):
        knopki = key.get_pressed()
        if knopki[K_d]:
            self.rect.x += 3
        if knopki[K_a]:
            self.rect.x -= 3
        if knopki[K_s]:
            self.rect.y += 3
        if knopki[K_w]:
            self.rect.y -= 3
            
class monster(GameBB):
    def patrol(self, m1, m2):
        if self.rect.x < m1:
            self.napr = "pravo"
        if self.rect.x > m2:
            self.napr = "levo"
        if self.napr == "pravo":
            self.rect.x += 5 
        else:
            self.rect.x -= 5

class wall(sprite.Sprite):
    def __init__(self, width, height, x, y):
        self.image = Surface((width, height))
        self.image.fill((32,10,120))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def ris(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))

steni = [
    wall(20,200,150,80), #над над играком
    wall(20,220,450,80), #спарава 
    wall(170,20,0,280), #над персонажем 
    wall(600,20,0,400), #под персонажем
    wall(10,130,0,280), #слева
    wall(150,20,450,300) #продолжение справа
]

cash = [
    GameBB("деньги.png",260,100),
    GameBB("деньги.png",310,140),
    GameBB("деньги.png",360,100),
]




hero = player("BOBR.png", 50,340)
vrag = monster("BOOM.png", 10,210)
game = True
finish = False
font.init()
writer = font.Font(None, 38)
t1 = writer.render("хаха,без мамный попуск", True, (199,21,133))


n = 0

mixer.init()
mixer.music.load("na fon.mp3")
mixer.music.set_volume(0.1)
mixer.music.play(loops=-1)

coff = 1
zvuki = mixer.Sound("manny.ogg")


while game:
    if coff == 1:
        mixer.music.unpause()
    else:
        mixer.music.pause()
    for i in event.get():
        if i.type == QUIT:
            game = False
        if i.type == KEYDOWN:
            if i.key == K_p:
                if coff == 1:
                    coff = 0 
                else:
                    coff = 1

    okno.fill((207,165,204))
    for i in cash:
        i.ris()
        if sprite.collide_rect(hero, i):
            n += 1
            zvuki.play()
            cash.remove(i)
    score = writer.render(str(n), True, (230,103,97))
    okno.blit(score, (50,50))
    for i in steni:
        i.ris()
        if sprite.collide_rect(hero, i):
            game = False 
            finish=True
    hero.ris()
    hero.control()
    vrag.ris()
    if sprite.collide_rect(hero, vrag):
            game = False 
            finish=True
    vrag.patrol(160, 420)
    clock.tick(60)
    display.update()

while finish:
    for i in event.get():
        if i.type == QUIT:
            finish = False
    okno.fill((231,84,192))
    okno.blit(t1, (180,250))
    display.update()