import pygame
import random

pygame.init()
dis = pygame.display.set_mode((900,600))
pygame.display.set_caption("Expand your aria")

clock = pygame.time.Clock()
notover = True
 

font_style = pygame.font.SysFont("Arial", 30)


def message(msg, color, w, h):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [w/3, h/3])

class player:
     def __init__(self,x,y,w,h,color,speed):
          self.x = x
          self.y = y
          self.w = w
          self.h = h
          self.speed = speed
          self.color = color
          self.score = 0
     def draw(self):
          self.p1 = pygame.Rect(self.x,self.y,self.w,self.h)
          pygame.draw.rect(dis,self.color,self.p1)
          return self.p1
     
     def move(self):
          key = pygame.key.get_pressed()
          if key[pygame.K_RIGHT]:
               self.x += self.speed
          if key[pygame.K_LEFT]:
               self.x -= self.speed
          if key[pygame.K_UP]:
               self.y -= self.speed
          if key[pygame.K_DOWN]:
               self.y += self.speed
          
     def big(self):
          self.w += 10
          self.h +=10
     def smal(self):
          self.w -= 15
          self.h -= 15
     
     # def bordarcollid(self):
     #      if self.x >= 800 or self.x <= 0:
     #           print("border")
               
     # def show(self):
     #      pygame.Rect(dis,self.color,self.draw)

     def iswin(self):
          if self.w >= 800 or self.h >=600:
               return True
          return False


class Food:
     def __init__(self,w,h,color):
          self.x = random.randrange(700)
          self.y = random.randrange(500)
          self.w = w
          self.h = h
          self.color = color
          self.name = "good"

     def draw(self):
          self.f1 =pygame.Rect(self.x,self.y,self.w,self.h)
          pygame.draw.rect(dis,self.color,self.f1)
          return self.f1

class Foodb:
     def __init__(self,w,h,color):
          self.x = random.randrange(700)
          self.y = random.randrange(500)
          self.w = w
          self.h = h
          self.color = color
          self.name = "bad"

     def draw(self):
          self.f1 =pygame.Rect(self.x,self.y,self.w,self.h)
          pygame.draw.rect(dis,self.color,self.f1)
          return self.f1
    
          

def iscollid(rect1 ,rect2):
     rect1.colliderect(rect2)


def deletfood(foods,food):
     foods.remove(food)

def makefood(foods):
     food1 = Food(20,20,(250,200,2))
     food2 = Foodb(20,20,(254,74,25))
     foods.append(food2)
     foods.append(food1)



def main():
     p = player(10,10,50,50,(255,255,255),5)
     food1 = Food(20,20,(250,200,2))
     
     foods = []
     foods.append(food1)
      
     
     
     while notover :

          for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    pygame.quit()

                    quit()
          p.move()
          r1=p.draw()
          message("score", (255,255,255),800*3-200,10)
          message(str(p.score), (255,255,255),800*3+100,10)
          print(p.h,p.w)
          for i in foods:
               # i.food_position()
               r2 = i.draw()
               if i.x > 800 :
                    print("going out")
                    deletfood(foods,i)

               if r1.colliderect(r2):
                    # print("collition")
                    if i.name == "good":
                         p.big()
                         p.score += 10
                         # print(p.score)
                         
                    elif i.name == "bad":
                         p.score -=5
                         p.smal()

            
                    
                    deletfood(foods,i)
                    makefood(foods)
                    
          if p.iswin():
               print("p1 win")

          if p.score < 0  or p.h < 0:
               message("Game Over ",(255,255,255),800,800)
          
          
          


         


          # if iscollid(r1,r2):
          #      print("collition")

         
          pygame.display.update()
          dis.fill(0)
          clock.tick(30)
main()
