# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 17:23:07 2019

@author: Han
"""

import numpy as np
from random import choice

#def read_grid():

def comp(x, y):
    for i in range(len(x)):
        if x[i] not in y:
            return False
    return True

def read_grid(filename):
    # read the bff file as a txt file
    data=open(filename)
    # output the content in the data
    lines=data.read()
    # get the grid between "GRID START"  and "GRID STOP"
    lines = lines.split('GRID START')[-1]
    lines = lines.split('GRID STOP')[0]
    # get rid of new line characters
    lines = lines.strip().split("\n")
    lines = np.array(lines)
    # Count how many spaces between each available slot
    randomcheck = lines[1]
    count = 0
    for i in range(len(randomcheck)):
        if randomcheck[i+1]==" ":
            count = count +1
        else:
            break
    glst=[]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j]=="o":
                glst.append([j/(count-1)+1,2*i+1])
    return glst
global glst

def read_numbers(filename):
    '''get the rest variables'''
    # read the bff file as a txt file
    data = open(filename)
    # output the content in the data
    lines = data.read()
    # get the grid between "GRID START"  and "GRID STOP"
    splitline1 = lines.split("GRID START")[-1]
    splitline2 = splitline1.split("GRID STOP")[-1]
    splitline2 = splitline2.strip("\n").split("\n")
    rest_array = np.array(splitline2)
    Anum = 0
    Bnum = 0
    Cnum = 0
    xlist = []
    ylist = []
    vxlist = []
    vylist = []
    Pxlist = []
    Pylist = []
    for i in range(len(rest_array)):
        for j in range(len(rest_array[i])):
            if rest_array[i][j] == "A":
                Anum = rest_array[i][j + 2]
                Anum = int(Anum)
            if rest_array[i][j] == "B":
                Bnum = rest_array[i][j + 2]
                Bnum = int(Bnum)
            if rest_array[i][j] == "C":
                Cnum = rest_array[i][j + 2]
                Cnum = int(Cnum)
            if rest_array[i][j] == "L":
                xvalue = rest_array[i][j + 2]
                xvalue = int(xvalue)
                xlist.append(xvalue)
                yvalue = rest_array[i][j + 4]
                yvalue = int(yvalue)
                ylist.append(yvalue)
                if rest_array[i][j + 6] != "-" and rest_array[i][j + 8] != "-":
                    vxvalue = rest_array[i][j + 6]
                    vxvalue = int(vxvalue)
                    vyvalue = rest_array[i][j + 8]
                    vyvalue = int(vyvalue)
                    vxlist.append(vxvalue)
                    vylist.append(vyvalue)
                elif rest_array[i][j + 6] == "-" and rest_array[i][j + 9] == "-":
                    vxvalue = "-1"
                    vxvalue = int(vxvalue)
                    vyvalue = "-1"
                    vyvalue = int(vyvalue)
                    vxlist.append(vxvalue)
                    vylist.append(vyvalue)
                elif rest_array[i][j + 6] == "-" and rest_array[i][j + 9] != "-":
                    vxvalue = "-1"
                    vxvalue = int(vxvalue)
                    vyvalue = rest_array[i][j + 9]
                    vyvalue = int(vyvalue)
                    vxlist.append(vxvalue)
                    vylist.append(vyvalue)
                elif rest_array[i][j + 6] != "-" and rest_array[i][j + 8] == "-":
                    vxvalue = rest_array[i][j + 6]
                    vxvalue = int(vxvalue)
                    vyvalue = "-1"
                    vyvalue = int(vyvalue)
                    vxlist.append(vxvalue)
                    vylist.append(vyvalue)
            if rest_array[i][j] == "P":
                Pxlist.append(int(rest_array[i][j + 2]))
                Pylist.append(int(rest_array[i][j + 4]))
    Plst = []
    for i in range(len(Pxlist)):
        Plst.append([Pxlist[i],Pylist[i]])
    return Anum, Bnum, Cnum, xlist, ylist, vxlist, vylist, Plst
class Blocks:
    def __init__(self,type, size,num):
        self.type = type
        self.size = size
        self.num = num
    def type(self,rest_array):
        type = []
        for i in range(len(rest_array)):
            for j in range(len(rest_array)):
                if rest_array[i][j]=="A":
                    type = "A"
                if rest_array[i][j]== "B":
                    type = "B"
                if rest_array[i][j]=="C":
                    type = "C"
        return type
import random
from random import choice
def random_block(Anum,Bnum,Cnum,glst):
    delete_lst=[]
    for u in range(len(glst)):
        delete_lst.append(glst[u])
    reflect=[]
    for i in range(Anum):
        A = random.choice(delete_lst)
        reflect.append(A)
        delete_lst.remove(A)
    refract=[]
    for i in range(Cnum):
        C = choice(delete_lst)
        refract.append(C)
        delete_lst.remove(C)
    opaque= []
    for i in range(Bnum):
        B = choice(delete_lst)
        opaque.append(B)
    sreflect=[]
    srefract=[]
    sopaque=[]
    for a in range(len(reflect)):
        x,y = reflect[a]
        side = [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]
        sreflect.extend(side)
    for b in range(len(refract)):
        x,y = refract[b]
        side = [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]
        srefract.extend(side)
    for c in range(len(opaque)):
        x,y = opaque[c]
        side = [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]
        sopaque.extend(side)
    return reflect, refract, opaque, sreflect, srefract, sopaque
global reflect,refract,opaque,sreflect,srefract,sopaque
def lazor_run(xlist,ylist,vxlist,vylist,Plst,reflect,refract,opaque,sreflect,srefract,sopaque,Anum,Bnum,Cnum,glst):
    lazor = []
    branch = []
    while comp(Plst, lazor)==False:
        reflect, refract, opaque, sreflect, srefract, sopaque = random_block(Anum,Bnum,Cnum,glst)
        lazor[:]=[]
        for i in range(len(xlist)):
            x = xlist[i]
            y = ylist[i]
            vx = vxlist[i]
            vy = vylist[i]
            bx = 8
            by = 8
            lazor=[[x,y]]
            branch[:]=[]
            while 0 < x < bx and 0 < y < by:
                x = x + vx
                y = y + vy
                lazor.append([x,y])
                #
                if [x,y] in sreflect:
                    if x % 2 == 0:
                        vx = (-1)*vx
                    else:
                        vy = (-1)*vy
        
                elif [x,y] in srefract:
                    srefract[:]=[]
                    branch.append([x,y,vx,vy])
                    if x % 2 == 0:
                        vx = (-1)*vx
                    else:
                        vy = (-1)*vy
                #
                elif [x,y] in sopaque:
                    break

            if len(branch) != 0:
                #branch loop
                for x,y,vx,vy in branch:
                    while 0 < x < bx and 0 < y < by:
                        x = x + vx
                        y = y + vy
                        lazor.append([x,y])
                        if [x,y] in sreflect:
                            if x % 2 == 0:
                                vx = (-1)*vx
                            else:
                                vy = (-1)*vy
                        #
                        elif [x,y] in sopaque:
                            break
    return (reflect, refract, opaque)

def soln_map(reflect,refract,opaque):
    lst=["x"]*25
    lst=np.array(lst)
    lst=lst.reshape(5,5)
    for i in range(len(glst)):
        m = glst[i][0]
        n = glst[i][1]
        lst[int((n-1)/2)][int((m-1)/2)]="o"
    for i in range(len(reflect)):
        m = reflect[i][0]
        n = reflect[i][1]
        lst[int((n-1)/2)][int((m-1)/2)]="A"
    for i in range(len(refract)):
        m = refract[i][0]
        n = refract[i][1]
        lst[int((n-1)/2)][int((m-1)/2)]="C"
    for i in range(len(opaque)):
        m = opaque[i][0]
        n = opaque[i][1]
        lst[int((n-1)/2)][int((m-1)/2)]="B"
    solnMap = open("solnMap.txt", "w")
    solnMap.write(str(lst))
    solnMap.close()

glst = read_grid("mad_1.bff")

[Anum, Bnum, Cnum, xlist, ylist, vxlist, vylist, Plst]= read_numbers("mad_1.bff")
[reflect,refract,opaque,sreflect,srefract,sopaque]=random_block(Anum,Bnum,Cnum,glst)
[reflect,refract,opaque]=lazor_run(xlist,ylist,vxlist,vylist,Plst,reflect,refract,opaque,sreflect,srefract,sopaque,Anum,Bnum,Cnum,glst)
soln_map(reflect,refract,opaque)