from pl_base_classes import ppl, obj_function, restriction, var_restrictions

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
    obj = obj_function(obj_type, cT)

    # the restrictions
    s = list()
    for j in range(m):
      unparsed_rest = input().split()
      A = [float(a) for a in unparsed_rest[:-2]]
      rest_t = unparsed_rest[-2]
      b = float(unparsed_rest[-1])
      s.append(restriction(A,rest_t,b))

    # each var is > 0, < 0 or L(unrestricted)
    unparsed_vr = input().split()
    vr = var_restrictions()
    for i in range(n): vr['x'+str(i+1)]=unparsed_vr[i]

    yield ppl(obj,s,vr)


# for testing sake
if __name__ == '__main__':
    for p in parse_input():
      print(p, '\n')