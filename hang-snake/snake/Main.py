import time
from pynput import keyboard
from random import randint

import threading

fieldWidth = 20
fieldHeight = 20
fps = 1
isRunning = True

class Xy: # класс чтобы можно было обращаться к x,y координатам
    x = 1
    y = 1

    def __init__(self,x,y): # конструктор
        self.x = x
        self.y = y


class Field:

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.apples = []

    def addApple(self):
        self.apples.append(
            (
                randint(0, self.height),  # генерируем х координату яблока
                randint(0, self.width)  # генерируем у координату яблока
            )
        )

    def render(self):
        for i in range(0,self.height):
            print('.' * self.width + '\n')


class Snake:

    directions = ['up', 'right', 'down', 'left']

    body = [Xy(fieldWidth,fieldHeight-1), Xy(fieldWidth,fieldHeight)] # 1 - голова, 2 - хвост

    length = len(body)

    moveDir = directions[0]

    def keyProcesser(self,key):
        if key == keyboard.Key.left and self.moveDir != self.directions[1]:
            self.moveDir = self.directions[3]
        elif key == keyboard.Key.up and self.moveDir != self.directions[2]:
            self.moveDir = self.directions[0]
        elif key == keyboard.Key.right and self.moveDir != self.directions[3]:
            self.moveDir = self.directions[1]
        elif key == keyboard.Key.down and self.moveDir != self.directions[0]:
            self.moveDir = self.directions[2]

    def crawl(self):
        self.body.pop(-1)
        if self.moveDir == 'up':
            self.body.insert(0,self.body[0].y-1)
        elif self.moveDir == 'right':
            self.body.insert(0,self.body[0].x+1)
        elif self.moveDir == 'down':
            self.body.insert(0,self.body[0].y+1)
        elif self.moveDir == 'left':
            self.body.insert(0,self.body[0].x-1)

    def isCollision(self):
        if self.body.count(self.body[0]) > 1:
            return True
        elif self.body[0].x >= fieldWidth or self.body[0].y >= fieldHeight:
            return True
        elif self.body[0].x <= 0 or self.body[0].y <= 0:
            return True
        else:
            return False



field = Field(fieldHeight,fieldWidth)
snake = Snake()

with keyboard.Listener(on_press=snake.keyProcesser) as listener:
    while isRunning:
        field.render()
        if snake.isCollision() == True:
            isRunning = False
        else:
            snake.crawl()
            print(snake.body)
            time.sleep(fps)



