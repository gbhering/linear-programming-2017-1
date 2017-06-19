def print_ppl(ppl):
  print_ppl_args(ppl.n, ppl.m, ppl.ppl_type, ppl.target, ppl.t_vars,
            ppl.A, ppl.r_type, ppl.b, ppl.x, ppl.x_type)

def print_ppl_args(n, m, ppl_type, target, t_vars, 
                    A, r_type, b, x, x_type):
    
    print(ppl_type, end=' ')
    for v in zip(target, t_vars):
      print( ('+' if v[0]>=0 else '') + str(v[0]) + str(v[1]), end=' ' )
    print('')

    for r in range(m):
      for a in range(n):
        if A[r][a] > 0:
          print("+", repr(+A[r][a]), x[a], end=' ')
        if A[r][a] < 0:
          print("-", repr(-A[r][a]), x[a], end=' ')

      print(r_type[r], b[r])

    if x_type[0] != 'L':
      print(x[0], x_type[0], '0', end='')
    for r in range(1,n):
      if x_type[r] != 'L':
        print(',', x[r], x_type[r], '0', end=' ')

    print('')

