import numpy as np


#IN CASE OF USER INPUT

#printing the grid(Sudoku)
# Row = int(input("Enter the number of rows:"))
# Column = int(input("Enter the number of columns:"))

# grid = []
# print("Enter the entries row wise:")

# for l in range(Row):		 
# 	n =[]
# 	for m in range(Column):	 
# 		n.append(int(input()))
# 	grid.append(n)


# for l in range(Row):
# 	for m in range(Column):
# 		print(grid[l][m], end = " ")
# 	print()




# grid = [
#     [5,3,0,0,7,0,0,0,0],
#     [6,0,0,1,9,5,0,0,0],
#     [0,9,8,0,0,0,0,6,0],
#     [8,0,0,0,6,0,0,0,3],
#     [4,0,0,8,0,3,0,0,1],
#     [7,0,0,0,2,0,0,0,6],
#     [0,6,0,0,0,0,2,8,0],
#     [0,0,0,4,1,9,0,0,5],
#     [0,0,0,0,8,0,0,0,0]
# ]

# grid = [
#     [0,5,7,0,0,0,0,2,4],

#     [0,9,8,0,0,0,0,1,3],
#     [0,0,0,0,3,7,0,0,0],
#     [2,3,0,0,8,9,0,0,0],
#     [7,6,0,0,0,0,0,8,5],
#     [0,0,0,4,6,0,0,3,7],
#     [0,0,0,9,2,0,0,0,0],
#     [8,1,0,0,0,0,4,6,0],
#     [5,2,0,0,0,0,1,7,0]
# ]

grid= [
    [0,0,0,5,0,4,0,1,0],
    [6,8,0,0,0,9,0,7,0],
    [0,0,9,0,0,0,3,0,0],
    [3,5,0,0,7,0,0,0,8],
    [0,0,0,2,0,1,0,0,0],
    [1,0,0,0,4,0,0,5,9],
    [0,0,2,0,0,0,5,0,0],
    [0,9,0,3,0,0,0,4,2],
    [0,4,0,6,0,8,0,0,0]
]



def analyze(row, col , num):
    global grid

# check for number in row
    for i in range(0,9):
        if grid[row][i] == num:
            return False
        
# check for number in column        
    for i in range(0,9):
        if grid[i][col] == num :
            return False
        

# rounding of numbers to divide rows into sections of 3
    x = (row//3) * 3                
    y = (col//3) * 3

# check for number in square

    for i in range(0 ,3):
        for j in range(0 , 3):
            if grid [x+i][y + j] == num:
                return False
        
    return True


def solution():
    global grid
    for row in range(0,9):
        for col in range(0,9):
            if grid[row][col] == 0:
                for num in range(1,10):
                    if analyze(row, col , num):
                        grid[row][col] = num
                        solution()                       
                        grid[row][col] = 0
                return

    print("\n", np.matrix(grid))
    input("\n press ENTER for more solutions \n")

solution()

