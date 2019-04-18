# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 17:23:07 2019

@author: Han
"""

import numpy as np
from random import choice
# Make a function to do the comparison. If all the target points 
# are in the path of the laser, then return true.
def comp(x, y):
    for i in range(len(x)):
        if x[i] not in y:
            return False
    return True
# Make a function to read the coordinates where the blocks are allowed
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
    # Calculate the length and the width of the grid
    if count == 1:
        bx = len(lines[0])+1
        by = len(lines)*2
    else:
        bx = (len(lines[0])-1)/2+2
        by = len(lines)*2
    # Make a list to save the coordinates where the blocks are allowed
    glst=[]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j]=="o":
                if count == 1:
                    glst.append([j+1,2*i+1])
                else:
                    glst.append([j/(count-1)+1,2*i+1])
    return glst, bx, by
# Make a function to read the numbers of reflect blocks, refract blocks,
# and opaque blocks. It also read the coordinate of the starting point,
# the direaction of the laser, and the corrdinates of the target points
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
    # get the numbers of reflect blocks A, refract blocks C,
    # and opaque blocks B
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
            # get the coordinate of the starting point,
            # the direaction of the laser
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
            # get the corrdinates of the target points
            if rest_array[i][j] == "P":
                Pxlist.append(int(rest_array[i][j + 2]))
                Pylist.append(int(rest_array[i][j + 4]))
    # make a list to combine Px with Py
    Plst = []
    for i in range(len(Pxlist)):
        Plst.append([Pxlist[i],Pylist[i]])
    return Anum, Bnum, Cnum, xlist, ylist, vxlist, vylist, Plst
# use a class object to describe the blocks
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
# make a function to randomly choose coordinates to be the locations of 
# the reflect/refract/opaque blocks
def random_block(Anum,Bnum,Cnum,glst):
    # make a new list to save all the coordinates of blocks allowed
    # then randomly choose coordinates in this list to be the locations of
    # these blocks, and remove these coordinates from the list
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
    # make three lists to save the coordinates of the edges of each blocks
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
# make a function to let the laser beams run from the starting point and have
# different response when runs into different blocks
def lazor_run(xlist,ylist,vxlist,vylist,Plst,reflect,refract,opaque,sreflect,srefract,sopaque,Anum,Bnum,Cnum,glst,bx,by):
    lazor = []
    branch = []
    # if the target points are not all in the path of the laser beams,
    # then continue the loop to randomly choose different coordinates for
    # the blocks
    while comp(Plst, lazor)==False:
        reflect, refract, opaque, sreflect, srefract, sopaque = random_block(Anum,Bnum,Cnum,glst)
        lazor[:]=[]
        # the laser beams run from the starting point and have a direction of
        # vx and vy
        for i in range(len(xlist)):
            x = xlist[i]
            y = ylist[i]
            vx = vxlist[i]
            vy = vylist[i]
            lazor=[[x,y]]
            branch[:]=[]
            # if the laser beams do not reach the edge of the grid, then
            # continue the loop
            while 0 < x < bx and 0 < y < by:
                x = x + vx
                y = y + vy
                # make a list to save the path of the laser beams
                lazor.append([x,y])
                # if the laser beams reach the edge of the reflect block,
                # the direction will change
                if [x,y] in sreflect:
                    # if the x-coordinate is even, the vx direction will change
                    # to -vx
                    if x % 2 == 0:
                        vx = (-1)*vx
                    # if the x-coordinate is odd, the vy direction will change
                    # to -vy
                    else:
                        vy = (-1)*vy
                # if the laser beams reach the edge of the refract block,
                # a branch will occur. The direction of beam will change 
                # and the direction of the other beam will not change
                elif [x,y] in srefract:
                    # Since each refract block only works once, so remove the
                    # the coordinates of the edges of the refract blocks after
                    # it works
                    srefract[:]=[]
                    # Save the coordinate and the direction of the branch point
                    branch.append([x,y,vx,vy])
                    # For the beam of which the direction is changed
                    # if the x-coordinate is even, the vx direction will change
                    # to -vx
                    if x % 2 == 0:
                        vx = (-1)*vx
                    # if the x-coordinate is odd, the vy direction will change
                    # to -vy
                    else:
                        vy = (-1)*vy
                # if the laser beams reach the edge of the opaque block, the 
                # beam will stop, so break the loop
                elif [x,y] in sopaque:
                    break
            # if there is branch point, make a loop for the beam of which 
            # the direction is not changed
            if len(branch) != 0:
                #branch loop
                for x,y,vx,vy in branch:
                    # if the laser beams do not reach the edge of the grid, then
                    # continue the loop
                    while 0 < x < bx and 0 < y < by:
                        x = x + vx
                        y = y + vy
                        # Save the path of the laser beams in the same list
                        lazor.append([x,y])
                        # if the laser beams reach the edge of the reflect block,
                        # the direction will change
                        if [x,y] in sreflect:
                            # if the x-coordinate is even, the vx direction will change
                            # to -vx
                            if x % 2 == 0:
                                vx = (-1)*vx
                            # if the x-coordinate is odd, the vy direction will change
                            # to -vy
                            else:
                                vy = (-1)*vy
                        # Since there is only one refract block at most, we
                        # don't consider it will run into another refract block
                        # if the laser beams reach the edge of the opaque block, the 
                        # beam will stop, so break the loop
                        elif [x,y] in sopaque:
                            break
    return (reflect, refract, opaque)
# Output the solution in a txt file
def soln_map(reflect,refract,opaque):
    # make a 5*5 array
    # x = no block allowed
    # o = block allowed
    # A = reflect block
    # B = opaque block
    # C = refract block
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

[glst,bx,by] = read_grid("mad_1.bff")

[Anum, Bnum, Cnum, xlist, ylist, vxlist, vylist, Plst]= read_numbers("mad_1.bff")
[reflect,refract,opaque,sreflect,srefract,sopaque]=random_block(Anum,Bnum,Cnum,glst)
[reflect,refract,opaque]=lazor_run(xlist,ylist,vxlist,vylist,Plst,reflect,refract,opaque,sreflect,srefract,sopaque,Anum,Bnum,Cnum,glst,bx,by)
soln_map(reflect,refract,opaque)