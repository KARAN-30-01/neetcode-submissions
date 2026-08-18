class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checkarr(arr):
            bol = True
            extr=[]
            for i in arr:
                if i != '.':    
                    extr.append(i) 

            if not len(extr) == len(set(extr)):
                bol= False

            for element in arr:
                if element != '.':
                    if not (1 <= int(element) <= 9):
                        bol = False
                        break      
            return bol 

        bol = True

        for i in board:  
            
            if checkarr(i) == False:
                return False 
        
        cols = [[0] * 9 for _ in range(9)]

        for r in range(9):
            for c in range(9):
        
                cols[c][r] = board[r][c]

        for i in cols:  
            
            if checkarr(i) == False:
                return False
            
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):

                box = []

                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        box.append(board[i][j])

                if checkarr(box) == False:
                    return False 
        
        return bol