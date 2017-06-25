from collections import MutableMapping as MM
from collections import defaultdict

# definition of the objective function container
class obj_function(MM):  
  def __init__(self, obj_type='min', cT=[], var_names=[]):
    self.obj_type = obj_type
    self.cT = cT

    # only allows for custom naming if there are names for every var
    self.var_names = var_names \
    if len(var_names) == len(cT) \
    else ['x'+str(i) for i in range(1,len(cT)+1)]

  def __len__(self): return len(self.cT)
  def __contains__(self,item): return item in self.var_names
  def __iter__(self): return self.var_names.__iter__()
  def keys(self): return self.var_names
  def values(self): return self.cT

  def __getitem__(self, key):
    if type(key) == type(str()):
      if key not in self.var_names: return 0.0
      else: return self.cT[self.var_names.index(key)]
    elif type(key) == type(int()):
      return self.cT[key]

  def __delitem__(self, key):
    if type(key) == type(str()):
      if key in self.var_names:
        del self.cT[self.var_names.index(key)]
        del self.var_names[self.var_names.index(key)]
    elif type(key) == type(int()):
        del self.cT[key]
        del self.var_names[key]
    
  def __repr__(self):
    return self.obj_type + ' ' + ' + '.join(
      [str(self.cT[i])+vn for i, vn in enumerate(self.var_names)])

  def __setitem__(self, key, value):
    if key in self.var_names:
      self.cT[self.var_names.index(key)] = value
    else:
      self.cT.append(value) 
      self.var_names.append(key) 


# definition of the restricion container
class restriction(MM):  
  def __init__(self, a=[], rest_type='=', b=0, var_names=[]):
    self.rest_type = rest_type
    self.a = a
    self.b = b

    # only allows for custom naming if there are names for every var
    self.var_names = var_names \
    if len(var_names) == len(a) \
    else ['x'+str(i) for i in range(1,len(a)+1)]

  def __len__(self): return len(self.a)
  def __contains__(self,item): return item in self.var_names
  def __iter__(self): return self.var_names.__iter__()
  def keys(self): return self.var_names
  def values(self): return self.a

  def __getitem__(self, key):
    if type(key) == type(str()):
      if key not in self.var_names: return 0.0
      else: return self.cT[self.var_names.index(key)]
    elif type(key) == type(int()):
      return self.cT[key]

  def __delitem__(self, key):
    if type(key) == type(str()):
      if key in self.var_names:
        del self.cT[self.var_names.index(key)]
        del self.var_names[self.var_names.index(key)]
    elif type(key) == type(int()):
        del self.cT[key]
        del self.var_names[key]
    
  def __repr__(self):
    rest = ' + '.join([str(self.a[j])+vn for j,vn in enumerate(self.var_names)])
    return "{} {} {}".format(rest, self.rest_type, str(self.b))

  def __setitem__(self, key, value):
    if key in self.var_names:
      self.cT[self.var_names.index(key)] = value
    else:
      self.cT.append(value) 
      self.var_names.append(key) 


# definition of the container for the restricions upon variables
class var_restrictions(MM):  
  def __init__(self, rest_types=[], var_names=[]):
    self.rest_types = rest_types
    # only allows for custom naming if there are names for every var
    self.var_names = var_names \
    if len(var_names) == len(rest_types) \
    else ['x'+str(i) for i in range(1,len(rest_types)+1)]

  def __len__(self): return len(self.var_names)
  def __contains__(self,item): return item in self.var_names
  def __iter__(self): return self.var_names.__iter__()
  def keys(self): return self.var_names
  def values(self): return self.rest_types

  def __getitem__(self, key):
    if key not in self.var_names: return 'L'
    else: return self.rest_types[self.var_names.index(key)]

  def __delitem__(self, key):
    if key in self.var_names:
      del self.rest_types[self.var_names.index(key)]
      del self.var_names[self.var_names.index(key)]
    
  def __repr__(self):
    return ', '.join(
      [ v+' '+t+' 0' for v,t in zip(self.var_names,self.rest_types) if t != 'L' ])

  def __setitem__(self, key, value):
    if key in self.var_names:
      self.rest_types[self.var_names.index(key)] = value
    else:
      self.rest_types.append(value) 
      self.var_names.append(key) 


# the main class, the class we're all here to see
class ppl:
  def __init__(self, 
    objective=obj_function(), rest=list(),var_rest=var_restrictions()):
    self.obj_function = objective
    self.restrictions = rest
    self.var_rest = var_rest

  def __repr__(self):
    return "{}\ns.a {}\n    {}".format(
      self.obj_function,
      '\n    '.join([str(r) for r in self.restrictions]),
      self.var_rest)
      


# for testing sake
if __name__ == '__main__':
  # P1
  obj1 = obj_function('min',[50.0,100.0])
  res1 = list()
  res1.append(restriction([7.0,2.0],'>',28))
  res1.append(restriction([2.0,12.0],'>',24))
  res1.append(restriction([7.0,-2.0],'>',14))
  vr1 = var_restrictions(['>','>'])

  ppl1 = ppl(obj1,res1,vr1)
  print(ppl1)