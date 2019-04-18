# Lazor Group Project 
DO YOU FACE A PROBLEM SOLVING LAZOR GAME? 
HERE IS YOUR IDEAL ‘CHEAT’ TOOL.
## Group Members: Zhenqin Wang, Han Zhang, Han Zong
## Getting Started

Make sure you have python (any version above 2.7) installed on your computer. Make sure you have the correct board file format files (.bff) available to access in a designated folder. Download "LazorSolver.py" under the designated folder. 

## Running the tests
In order to change to the wanted map, simple change filename (in this case "mad_1.bff") to the wanted .bff file. 
[Anum, Bnum, Cnum, xlist, ylist, vxlist, vylist, Plst]= read_numbers("mad_1.bff") 

Solutions will pop as a txt file under the folder path (with "A" as position of reflection block, "B" as position of opaque block, "C" as refraction block"). 
# Basic algorithm and ways to solve in this project
As long as the bff is uploaded and opened, it will establish a coordinate based on the problem. Also, all the prerequisites for the problem (say 2 opaques and reflections), the start point of laser and the point we need to cross will be established in the coordinates. Most importantly, the laser will become a function in the coordinate. Every time it meets a block, the function will adjust to the block and change its slope or intersect in the coordinate and continue in the exact direction until it meets another block, and change again. All the possible paths will be considered. At last, when all the prerequisites are met, the results will be saved and output a result file. 
Also, we have series of codes like class function, random function. If you want to check the code and learn something from it, you will get a lot of skills. 
It’s pretty easy to read the result. Just enjoy the feeling of commanding all the levels of the lazor game !
