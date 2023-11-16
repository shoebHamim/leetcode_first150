# naive approach 
def isValidSudoku(board):
  i=0
  while i<9:
    row=board[i]
    # row checking
    for r in row:
      if r=='.':
        continue
      if 0>int(r)>9 or row.count(r)>1:
        return False 
    # sub box checking
    if i%3==0:
      col=i
      col_end=col+3
      r=0
      while r<9:
        # single sub_box check
        st=set()
        for c in range(col,col_end):
          for k in range(3):
            elem=board[r+k][c]
            if elem=='.':
              continue
            if 0>int(elem)>9 or elem in st:
              return False
            st.add(elem)
        r+=3

      
    # column checking
    j=0
    s=set()
    while j<9:
      val=board[j][i]
      if val=='.':
        j+=1
        continue
      if int(val) in s or 0>int(val)>9:
        return False
      s.add(int(val))
      j+=1

    i+=1
  return True

board =[
[".",".",".",".","5",".",".","1","."],
[".","4",".","3",".",".",".",".","."],
[".",".",".",".",".","3",".",".","1"],
["8",".",".",".",".",".",".","2","."],
[".",".","2",".","7",".",".",".","."],
[".","1","5",".",".",".",".",".","."],
[".",".",".",".",".","2",".",".","."],
[".","2",".","9",".",".",".",".","."],
[".",".","4",".",".",".",".",".","."]]

# print(isValidSudoku(board))

# same login ,less code(good implementation)
def isValidSudoku(board):
  row_dict={}
  col_dict={}
  square_dict={}
  for row in range(9):
    for col in range(9):
        elem=board[row][col]
        if elem=='.':
            continue
        if 0>int(elem)>9 or elem in row_dict.get(row,set()) or elem in col_dict.get(col,set()) or elem in square_dict.get((row//3,col//3),set()):
            return False
        found_inside=row_dict.get(row,set())
        found_inside.add(elem)
        row_dict[row]=found_inside
        found_inside=col_dict.get(col,set())
        found_inside.add(elem)
        col_dict[col]=found_inside
        found_inside=square_dict.get((row//3,col//3),set())
        found_inside.add(elem)
        square_dict[(row//3,col//3)]=found_inside
  return True



board =[
[".",".",".",".","5",".",".","1","."],
[".","4",".","3",".",".",".",".","."],
[".",".",".",".",".","3",".",".","1"],
["8",".",".",".",".",".",".","2","."],
[".",".","2",".","7",".",".",".","."],
[".","1","5",".",".",".",".",".","."],
[".",".",".",".",".","2",".",".","."],
[".","2",".","9",".",".",".",".","."],
[".",".","4",".",".",".",".",".","."]]

print(isValidSudoku(board))



    