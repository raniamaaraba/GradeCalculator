# Activity Python 3: Task 1
# File: ACT_Python_HeaderTemplate_Team150_maarabrn.py 
# Date:    1 30 2024
# By:      Rania Maaraba
# Section: 09
# Team:    150
# 
# ELECTRONIC SIGNATURE
# Rania Maaraba
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.

import math

g = open('grades.txt', 'r')
file = open('letterGrade.txt', 'w')
file.write()


grades = g.readlines()

print("Index     Total     Letter")

for i in range(1,len(grades)-1):
    calculations = grades[i].split()
    index = float(calculations[0])
    RAT=float(calculations[1])
    CFU=float(calculations[2])
    HW=float(calculations[3])
    Ex=float(calculations[5])
    pro=float(calculations[4])

    final_g = (0.05*(RAT)) + (0.15*(CFU)) + (0.15*(HW)) + (0.20*(pro)) + (0.45*(Ex))
    #Grade % = 0.05*RAT + 0.15*CFU + 0.15*HW + 0.20*Project + 0.45*Exam
    
    if 90 <= final_g < 100:
        Letter = "A"
    elif 80 <= final_g < 90:
        Letter = "B"
    elif 70 <= final_g < 80:
        Letter = "C"
    elif 60 <= final_g < 70:
        Letter = "D"
    elif final_g < 60:
        Letter = "F"

        
    print("{:.0f}".format(index), "   ", "{:.2f}".format( final_g) ,"  ", Letter)
        
    
#write single list tupe heasers
       
file.close()
