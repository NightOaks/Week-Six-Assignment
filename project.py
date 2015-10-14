# author__'Devin Simoneaux'

# IWU CIS-125 Intro to CS

# Name of program

# Definition of Program

def populate(world, h, w):
    

def display(world, h, w):
    
    
def generation(world, h, w):
    
    
def main():
    
  import random
  
  world = []
  h = 80
  w = 22
  
  world = populate(world)
  world = display(world)
  
  letter = input("Enter any key.")
  while (letter != "q"):
      world = generation(world)
      display(world)
      letter = input("Enter any key.")
      
    
    
    