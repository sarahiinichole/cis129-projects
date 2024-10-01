#Sarah Heredia 
#September 30, 2024
#Lab 5 The Bottle Return Program 
#the main function

def main() :

 endProgram = 'no'
 while endProgram == 'no':
  totalBottles = getBottles()
  totalPayout = calcPayout (totalBottles)
  printInfo (totalBottles, totalPayout)

  endProgram = raw_input('Do you want to end program? (Enter yes or no): ')

def getBottles():
  totalBottles = 0 
  todayBottles = 0 
  counter = 1
  while counter <=7:
   todayBottles = input('Enter number of bottles for today: ')
   totalBottles = totalBottles + todayBottles 
   counter = counter + 1

  return totalBottles

def calcPayout(totalBottles):
  totalPayout = 0
  totalPayout = totalBottles * .10
  return totalPayout 

def printInfo(totalBottles, totalPayout):
  print ('The total number of bottles collected is'), totalBottles
  print ('The total paid out is $'), totalPayout

main()

