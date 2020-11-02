import re
import random
def primary():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 13
  rnd = random.choices(quotes, k = 5)
  new_list= []
  for quote in rnd:
    new_list.append(quote.strip("\n"))

  print(new_list)

  

if __name__== "__main__":
  primary()
