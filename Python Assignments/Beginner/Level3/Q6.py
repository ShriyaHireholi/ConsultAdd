# Single Inheritance
class Animal:
    def sound(self):
        return "sound"

class Dog(Animal):
    def bark(self):
        return "Woof!"

# Multiple Inheritance
class Father:
    def skills(self):
        return ["gardening"]

class Mother:
    def skills(self):
        return ["art"]

class Child(Father, Mother):
    def skills(self):
        return super().skills() + Mother.skills(self)

# Multilevel Inheritance
class A:
    def method(self):
        return "Method in A"

class B(A):
    def method(self):
        return "Method in B"

class C(B):
    def method(self):
        return "Method in C"
