import numpy 


frame = numpy.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]])

def show_matrix_(frame) :
    for row in frame : 
        print(" ".join(str(cell) for cell in row)) 
    print()

def analyse_cell(frame, index_row, index_col):
    
    number_neighbors_alive = 0
    rows, cols = frame.shape  
    
    
    for row in range(index_row - 1, index_row + 2):  
        for col in range(index_col - 1, index_col + 2):
            
            if 0 <= row < rows and 0 <= col < cols:
                
                if row == index_row and col == index_col:
                    continue
                
                
                if frame[row][col] == 1:
                    number_neighbors_alive += 1
    
    return number_neighbors_alive

def next_state_matrix(frame):
    
    rows, cols = frame.shape 
    next_frame = frame.copy()  

    for row in range(rows):
        for col in range(cols): 
            alive_neighbors = analyse_cell(frame, row, col)
            
            
            if frame[row][col] == 0 and alive_neighbors == 3:
                next_frame[row][col] = 1  
            elif frame[row][col] == 1 and alive_neighbors in [2, 3]:
                next_frame[row][col] = 1  
            else:
                next_frame[row][col] = 0  
    
    return next_frame
          

