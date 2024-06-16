
class Mathe:
    def __init__(self):
        pass

    def new_matrix(max_rows, max_cols, value):
        array = []

        i = 0

        while i < max_cols*max_rows:
            array.append(value)
            i += 1
        
        return array
    

    def getting_row_col(n, col_max):
        row = int(n // col_max)
        col = n - row * col_max

        return (row, col)
    
    def getting_num(row, col, max_col):
        n = (row * max_col) + col

        return n