# class defining the ppl
class ppl:
  def __init__(self, n = 0, m = 0, st = 'min', sf = [], 
               A = [[]], rt = [], b = [], xt = []):
    self.n = n         # number of variables
    self.m = m         # number of restrictions
    self.sa_type = st  # 'min' or 'max'  
    self.sa_func = sf  # c values
    self.A = A         # A values, size m,n
    self.b = b         # b values, size m
    self.r_type = rt   # '>', '<' or '=' for each restriction
    self.x_type = xt   # '>', '<' or 'T' for each x
