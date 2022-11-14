def solveNQ(n, initial, ir, ic):  #ir - initial row, ic - initial col
  col = {ic}
  posDiag = {ir+ic}
  negDiag = {ir-ic}

  board = [['-']*n for i in range(n)]
  res = []

  def backtrack(r):
    
    if r==n:
      copy = [' '.join(row) for row in board]
      res.append(copy)
      return
    
    for c in range(n):    # run a for loop after running the base condition
      if r==ir:
        board[ir] = initial
        backtrack(r+1)
      
      else:
        if c in col or (r+c) in posDiag or (r-c) in negDiag:
          continue
        
        col.add(c)
        posDiag.add(r+c)
        negDiag.add(r-c)
        board[r][c] = 'Q'

        if (r+1) != ir:
          backtrack(r+1)
        else:
          backtrack(r+2)

        col.remove(c)
        posDiag.remove(r+c)
        negDiag.remove(r-c)
        board[r][c] = '-'

  backtrack(ir)

  if len(res)>0:
    for i in res[0]:
      print(i)
  else:
    print("NO soln")

solveNQ(4, ['-','Q','-', '-'],0,1)
