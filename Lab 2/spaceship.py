import math
from PIL import Image, ImageDraw, ImageFont

# collision
def collide(a, b, ra, rb):
    dx = a.x - b.x
    dy = a.y - b.y
    d = math.sqrt(dx*dx + dy*dy)
    if d < (ra+rb):
        return True
    else:
        return False

def collideEnemies(enemies, spaceship, bullets, explode_img, img):
    time = 0
    for e in enemies.es:
        if collide(spaceship, e, 10, 15):
            return True, time
        for b in bullets.bs:
            if collide(e, b, 15, 2):
                time += 1
                enemies.removeEnemy(e)
                bullets.removeBullet(b)
                e.explode(explode_img, img)
    return False, time


# our space ship

class spaceship:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
        self.velocity = 0.01

    def draw(self, img):
        offset = (self.x-10, self.y-10, self.x+10, self.y+10)
        image = Image.open(self.image).convert("RGBA")
        img.paste(image, offset, image)

    def move(self, dx, dy):
        if -5 < dx < 5:
            dx = 0
        if -5 < dy < 5:
            dy = 0
        self.x += int(dx * self.velocity)
        self.y += int(dy * self.velocity)
        if self.x > 232:
            self.x = 232
        elif self.x < 7:
            self.x = 7
        if self.y > 127:
            self.y = 127
        elif self.y < 7:
            self.y = 7

class bullet:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.velocity = 4

    def draw(self, draw):
        offset = (self.x-2, self.y-2, self.x+2, self.y+2)
        draw.rectangle(offset, outline="red", fill="red")

    def move(self):
        self.x += self.vx * self.velocity
        self.y += self.vy * self.velocity



class bullets:
    bs = []
    def __int__(self):
        self.bs = []

    def addBullet(self, x, y, vx, vy):
        self.bs.append(bullet(x,y,vx,vy))

    def moveBullets(self):
        for b in self.bs:
            b.move()

    def removeBullets(self):
        for b in self.bs:
            if b.x > 250 or b.x < -10 or b.y > 145 or b.y < -10:
                self.bs.remove(b)

    def removeBullet(self, b):
        self.bs.remove(b)

    def removeAll(self):
        for b in self.bs:
            self.bs.remove(b)

    def drawBullets(self, draw):
        for b in self.bs:
            b.draw(draw)

    def updateBullets(self, draw):
        self.moveBullets()
        self.removeBullets()
        self.drawBullets(draw)

class enemy:
    def __init__(self, x, y, vx, vy, image):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.image = image
        self.velocity = 1

    def draw(self, img):
        offset = (self.x-15, self.y-15, self.x+15, self.y+15)
        image = Image.open(self.image).convert("RGBA")
        img.paste(image, offset, image)

    def explode(self, explode_img, img):
        offset = (self.x-20, self.y-20, self.x+20, self.y+20)
        image = Image.open(explode_img).convert("RGBA")
        img.paste(image, offset, image)

    def move(self):
        self.x += int(self.vx * self.velocity)
        self.y += int(self.vy * self.velocity)
        if self.x > 230 or self.x < 10:
            self.vx = -self.vx

class enemies:
    es = []
    def __int__(self):
        self.es = []

    def addEnemy(self, x, y, vx, vy, img):
        self.es.append(enemy(x,y,vx,vy,img))

    def moveEnemies(self):
        for e in self.es:
            e.move()

    def removeEnemies(self):
        for e in self.es:
            if e.x > 250 or e.x < -10 or e.y > 145 or e.y < -10:
                self.es.remove(e)

    def removeAll(self):
        for e in self.es:
            self.es.remove(e)

    def removeEnemy(self, e):
        self.es.remove(e)

    def drawEnemies(self, img):
        for e in self.es:
            e.draw(img)

    def updateEnemies(self, img):
        self.moveEnemies()
        self.removeEnemies()
        self.drawEnemies(img)