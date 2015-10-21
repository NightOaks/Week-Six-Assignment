# author__'Devin Simoneaux'

# IWU CIS-125 Intro to CS

# Name of program

# Definition of Program

def populate(stuff, h=22, w=80):
  import random
  
  for x in range(h):
    row = []
    for y in range(w):
      r = Random.randint(0,1)
      if r == 0:
        row.append(" ")
      else:
        rown.append("*")
      stuff.append(row)

def display(petri_dish, h=22, w=80):
  for x in range(h):
    rowString = ""
    for y in range(w):
      rowString += dish[x][y]
    worldString += rowString + "/n"
  print(worldString)
  
  
  
  
def generation(petri_dish, h=22, w=80):
    new_world = []
    
    for x in range(h):
      row = []
      for y in range(w):
        row.append(0)
      new_world.append(row)
    
      #Count neighbors
    n = 0
    for x in range(1,h-1):
      for y in range(1,w-1):
        n = petri_dish[x-1][y-1] + petri_dish[x-1][y] + petri_dish[x-1][y-1] + petri_dish[x][y-1] + petri_dish[x][y+1] + petri_dish[x+1][y-1] + petri_dish[x+1][y] + petri_dish[x+1][y+1]
            
        if petri_dish[x][y] == 0:
          if n == 3:
            new_world[x][y] = 1
          else:
            new_world[x][y] = 0
        else: #(cell is alive)
          if n < 2 or n > 3:
            new_world[x][y] = 0
              
    petri_dish = new_world
    
def main():
    
  import random
  
  world = []
  h = 80
  w = 22
  
  populate(world, h, w)
  display(world, h, w)
  
  letter = input("Enter any key. If you want to quit, hit 'q'.")
  
  while (letter != "q"):
      generation(new_world, h, w)
      display(world)
      letter = input("Enter any key. If you want to quit, hit 'q'.")
  
  print("Goodbye")
  
  if __name__ == '__main__':
    main()
      
    
    
    