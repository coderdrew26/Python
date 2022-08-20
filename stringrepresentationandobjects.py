from turtle import speed
import unittest


class Car:
    def __init__(self, speed,unit):
        self.speed=speed
        self.unit=unit
    def __str__(self):
        str1="Car with the maximum speed of {} {}"
        return str1.format(self.speed, self.unit)
    
class Boat:
    def __init__(self, speed):
        self.speed=speed
    def __str__(self):
        str1="Car with the maximum speed of {} knots"
        return str1.format(self.speed)