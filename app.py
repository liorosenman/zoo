import sys
from icecream import ic
from definitions import Actions
from DataTransitions import json_to_list
animals = []

def display_options():
    for action in Actions:
        print (f"{action.value} --- {action.name}")


def print(animals):
    pass

def add(animals):
    pass

def update(animals):
    pass

def delete(animals):
    pass

if __name__ == "__main__":
    while True:
        display_options()
        animals = json_to_list()
        choose = input("What you want to do? ")
        choice_int = int(choose)


        

