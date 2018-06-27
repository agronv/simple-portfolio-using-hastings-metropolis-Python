# folder_creation.py

import os
import errno
import random
import shutil

# first we make our directory
try:
    os.makedirs("quotes")
# if the directory already exists we will do nothing
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

# next we open our tickers folder and store the contents as a list
file = open("tickers.txt","r")
ticker_list = []
for line in file:
# we have to strip \n
    ticker_list.append(line.strip("\n"))
file.close()

# next we randomly pick 100 indexes from our ticker list, I'm uing a set so that
# there is no repetition. this loop will stop when we have 100 indexes
length = len(ticker_list)-1
tickernum = 0
ticker_100_set = set()
while(tickernum < 100):
    index = random.randint(0, length)
    ticker_100_set.add(index)
    tickernum = len(ticker_100_set)

# next we store the 100 tickers within a list
ticker_100_list = []
for i in ticker_100_set:
    ticker_100_list.append(ticker_list[i])

# create a new file names 100tickers.txt
tickerfile = open("100tickers.txt","w+")

# ths for loop will delete all the contents within the directory we just created, quotes
for the_file in os.listdir(r"C:\Users\avela\c++\minimum_variance\quotes"):
    file_path = os.path.join(r"C:\Users\avela\c++\minimum_variance\quotes", the_file)
    try:
        if os.path.isfile(file_path):
            os.unlink(file_path)
        # we will also delete every sub directory within the folder
        elif os.path.isdir(file_path): shutilrmtree(file_path)
    except Excepetion as e:
        print(e)

# as we write each ticker into the file 100tickers.txt, we also copy the data of
# the correspongind ticker into the quotes directory
for i in ticker_100_list:
    tickerfile.write(i+"\n")
    shutil.copy2(r"C:\Users\avela\c++\minimum_variance\quotes"+i+".txt",
                 r"C:\Users\avela\c++\minimum_variance\quotes\quotes"+i+".txt")

# lastly we will move the 100tickers.txt file into the quotes directory, but
# first we have to close our file
tickerfile.close()
os.rename(r"C:\Users\avela\c++\minimum_variance\100tickers.txt",
             r"C:\Users\avela\c++\minimum_variance\quotes\100tickers.txt")
