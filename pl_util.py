from pl_base_classes import ppl, obj_function, constraint, var_constraints

# returns a new problem now in standard form,
# plus a dictionary
def to_standard_form(p):
  st_dict = dict()

  st_var_cons = var_constraints()
  st_cT = []

  # altering the constraints upon variables
  for v in p.var_cons:
    if p.var_cons[v] == '<':
      new_v = '¬{v}'.format(v=v)
      st_dict[v] = new_v
      st_var_cons[new_v] = '>'
      st_cT.append()
    elif p.var_cons[v] == 'L':
      # v = v' - v"
      new_v1 = "{v}'".format(v=v)
      new_v2 = '{v}"'.format(v=v)
      st_dict[v] = "{v1}-{v2}".format(v1=new_v1,v2=new_v2)
      st_var_cons[new_v1] = '>'
      st_var_cons[new_v2] = '>'
    else:
      st_var_cons[v] = '>'


  return None, st_dict

if __name__ == '__main__':
  objective = obj_function('max', [1.0,1.0,3.0])
  constraints = list()
  constraints.append(constraint([7.0,2.0,3.0],'>',28))
  constraints.append(constraint([2.0,12.0,4.0],'<',24))
  constraints.append(constraint([7.0,-2.0,5.0],'=',14))
  var_cons = var_constraints(['<','L','>'])
  p = ppl(objective,constraints,var_cons)

  st_p, st_dict = to_standard_form(p)

  print(p)  
  print(st_dict)