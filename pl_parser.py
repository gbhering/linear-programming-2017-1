def parse_input():
  # number of problems to be solved
  p = int(input())

  for it in range(p):
    # number of variables and of restrictions
    n, m = [int(x) for x in input().split()]

    # the actual problem
    unparsed_obj = input().split()
    obj_type = unparsed_obj[0]
    cT = [float(c) for c in unparsed_obj[1:]]

    # the restrictions
    A = list()
    rest_t = list()
    b = list()
    for j in range(m):
      restriction = input().split()
      A.append([float(a) for a in restriction[:-2]])
      rest_t.append(restriction[-2])
      b.append(float(restriction[-1]))

    # each var is > 0, < 0 or L(unrestricted)
    var_rest = input()

    yield obj_type, cT, A, rest_t, b, var_rest


# for testing sake
if __name__ == '__main__':
    for obj_type, cT, A, rest_t, b, var_rest in parse_input():
      print(obj_type, cT)
      for j, Aj in enumerate(A): print(Aj, rest_t[j], b[j])
      print(var_rest)
      print()