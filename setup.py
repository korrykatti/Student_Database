# Automagically Creates all the important folders required for the program to work
# 
import os


print("If you are launching this program for the first time then only use it")
#Creates db_data folder
os.mkdir('db_data')
os.mkdir('logs')
for i in range(1,13):
    a = str(i)
    os.mkdir(a)



