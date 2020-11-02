import re
import random
def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 13
  rnd = random.choices(quotes, k = 5) #Select a specific number of quotes to be outputted
  new_list= []
  for quote in rnd:
    new_list.append(quote.strip("\n"))#Remove the new line character

  print(new_list)

  

if __name__== "__main__":
  primary()
