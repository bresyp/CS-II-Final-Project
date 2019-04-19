
"""
NAME:Bresy

ASSIGNMENT #: A4-12

SUMMARY:
This program will ask the user for a maze file and try to find a solution
for the maze.

A maze is represented in a .txt file using the following symbols:
    X - wall
    O - an open cell (that's an upper case o)
    ! - target
    * - part of our path to the target

HONOR CODE:
On my honor I have neither given nor taken any unacknowledged aid on this code
"""

from graphics import *
import time

"""
Description: Read a maze from the given file.
Parameters:
    filename    Name of the .txt file where the maze is specified
Returns: A 2D list containing the maze
Plan: Open the given file, read each line, strip to remove newlines, if any,
        and add it to a 2D list.
"""
def read_maze(filename):
    maze_file = open(filename, 'r')
    maze = []
    row_length = None
    for line in maze_file:
        row = []
        # need to remove the new line (strip)
        for ch in line.strip().upper():
            row.append(ch)
        maze.append(row)
    return maze
    
"""
Description: Main function to read and solve a maze
Parameters: None
Returns: None
Plan: Ask the user for a maze file, read it, check if it is valid and solve it.
        Print the solution path as well as the solved maze.
"""
def is_valid_maze(maze):
    # checks to make sure the maze is not empty
    if len(maze) == 0:
        print "No rows in maze"
        return False
    # determines the number of cells per row based on the first row
    cells_per_row = len(maze[0])
    # iterates over every row in the maze
    for row in maze:
        # checks to see if the row has a different number of cells
        # from the first row
        if cells_per_row != len(row):
            print "Uneven rows"
            return False

        # iterates over every cell in the row
        for cell in row:
            # checks if the cell is a non-valid item
            if cell not in "XO!*":
                print "Invalid cell: " + cell
                return False
    # returns true since any invalid cause would have returned False above
    return True


"""
Description: Print the maze
Parameters:
    maze    the maze to be printed
Returns:    None
Plan:   Go through the given 2D list row by row and print each row on one line
""" 
def print_maze(maze):
    # iterate over every row in the maze
    for row in maze:
        # appends each cell's character to the line
        line = ""
        for cell in row:
            line += cell
        # prints the line (one row of cells)
        print line

"""
Description: Determines whether the given cell is in the maze
Parameters:
    maze    2D list containing the maze
    row     row number of the cell
    col     column number
Returns:
    True    if the cell belongs to the maze
    False   if it is out of bounds
Plan: I will find the number of rows by looping through and making a count and
find the number of cprint_maze(maze)olumns by taking the len of a row. I will use an if
statement to check whether the row is equal to or less than the total number of
rows and do the same for columns to determine whether it is valid or not.
"""
def in_maze(maze, row, col):
    # number of "mini"list in the 2D list is how many rows there will be
        count_rows = len(maze)-1
        
        #how many numbers are in each row will tell the number of columns
        #used 0 bc there will always be at least on "mini"list
        count_col = len(maze[0])-1
        
        #put condition as >= so it checks that the INDEX is in the maze
        
        if row <= count_rows and row >= 0:
             if col <= count_col and col >= 0:
                         return True
        else:
             return False


"""
Description: Attempts to solve the provided maze. This method assumes that
you have gotten to the current row and column in your grid by following
the path stored in "path" variable.
Parameters:
    maze    A 2D list containing the current state of the maze
    row     The next row to check
    col     The next column to check
    path    A string that denotes the directions you have gone so far
            from the starting cell (row = 0, col = 0)
            Directions are: D = down; U = up; R = right; L = left
Returns:
    True    If the maze is solved, i.e. the given cell (row, col) contains
            the target we're looking for.
    False   All other cases, including if this move will take us out of the maze

Plan: I will check to make sure that the cell is on a O. That means that my base
cases will be checking if its a X or * or !. If not it will use recursion to
check the next cell. It will return False anytime that the cell does not work
and from there try to take a different path.
"""
def solve_maze(maze, row, col, path,solutions):
    if in_maze(maze, row, col) == True:
        
        #all the bases cases for the maze
        if  maze[row][col] == "!":
            solutions.append(path)
        if maze[row][col] == "X":
            return False
        if maze[row][col] == "*":
            return False
        
        if  maze[row][col] == "O":
            #changes to star so wont go back 
            maze[row][col] = "*"

            #checks for each direction in it is possible
            #recursion allows that each cell to take care of itself 
            if solve_maze(maze,row,col+1,path +"R",solutions) == True:
                     maze[row][col] == "O" 
            if solve_maze(maze,row,col-1,path+"L",solutions) == True:
                     maze[row][col] == "O"
            if solve_maze(maze,row+1,col,path+"D",solutions) == True:
                     maze[row][col] == "O"
            if solve_maze(maze,row-1,col,path+ "U",solutions) == True:
                     maze[row][col] == "O"
                     
        return solutions
        return False


"""
Description: I will check the path and check what path is the shortest
Parameter:
solution - the solutions of the maze
Return:
the shortest solution
Plan:
I will loop through the list of solutions and then check which has the shortest
length and return that solution
"""
def shortest_path(solutions):
    min_len = 100
    shortest = ""
    for path in solutions:
       if len(path) < min_len:
           min_len = len(path)
           shortest = path
    return shortest
    
"""
Description: create the graphics maze
Parameter:
win - window that the maze will be drawn in
maze - the file version of the maze
Return:
graphics_maze - the drawn maze
Plan: Take the arranged form of the maze and will have to fit a certain format
in order to mimicking the format of the maze. Draw an overall outlineof the maze
with only a gap fo the entrance. Make variable so it is all resizable to the win
Noting will happen if there is an O but if it is an X it begin to draw a thin
line and if there is another X next (left or right) or below it, it will
continue to draw the line (recursion method might be needed here)
The ! will be drawn as a big white ball
"""

def create_maze(maze,win):
    width = win.getWidth()
    #create_outline_maze(win)    
    #how many numbers are in each row will tell the number of columns
    #used 0 bc there will always be at least on "mini"list
    cols = len(maze[0])
    x = 0
    y = width
    ref_point = Point(x,y)
    
    for rows in maze:
        for cell in rows:
            if cell == "O":
                x += width/cols
                
            if cell == "X":
                wall = Rectangle(Point(x-width/cols/10,y+width/cols/2),\
                                 Point(x+width/cols/100,y-width/cols/2))
                wall.setFill("black")
                wall.draw(win)
                
            if cell == "!":
                x += width/cols
                circle = Circle(Point(x,y),width/(cols*10))
                circle.draw(win)
                
        y -= width/cols
        x = 0
    
"""
Description: creates all the walls for the maze
Parameter:
    win - window it will all be drawn in
Return:
    none
Plan:
    Create points for each of ends of the "walls" of the maze and draw them on
    the window
"""
def create_outline_maze(win):
    width = win.getWidth()
    top_wall = Line(Point(width*.05,width*.95),Point(width*.95,width*.95))
    top_wall.draw(win)
    right_wall = Line(Point(width*.95,width*.95),Point(width*.95,width*.05))
    right_wall.draw(win)
    bottom_wall = Line(Point(width*.95,width*.05), Point(width*.05,width*.05))
    bottom_wall.draw(win)
    left_wall = Line(Point(width*.05,width*.05),Point(width*.05, width*.85))
    left_wall.draw(win)


"""
Description
Parameter:
Return:
Plan"""
"""
def pac_man_points(path,win):
    points = []
    width = win.getWidth()
    starter_point = Point(width*.025,width*.025)
    for letter in path:
        if letter == "R":
            starter_point = Point(width*.05*2 ,width*.025)
            points.append(starter_point)
        if letter == "L":
            starter_point = Point(width*.05- width *.01,width*.025)
            points.append(starter_point)
        if letter == "D":
            starter_point = Point(width*.025,width*.025)
            points.append(starter_point)
        if letter == "U":
            starter_point = Point(width*.025,width*.025)
            points.append(starter_point)
    return points

"""

"""
Description:
Parameter:
Return:
Plan:

def pac_man(path):
    points = pac_man_points(path)
    for point in points:
"""        
    
"""
Description:
Parameter:
Return:
Plan:
"""
def main():
    win = GraphWin("Circle Example", 600, 600)
    win.yUp()
    
    maze = read_maze("maze.txt")
 
                
    if True == is_valid_maze(maze):
        row = 0
        col = 0
        path = ""
        solutions = []
        create_maze(maze,win)
        solutions = solve_maze(maze,row,col,path,solutions)
        path = shortest_path(solutions)
        print path
        #points = pac_man_points(path,win)
        #print points
        #pac_man(points)
        
        
      

    #waits for the user to click the screen
    win.getMouse()
    #closes the window
    win.close()

if __name__ == "__main__":
    main()

