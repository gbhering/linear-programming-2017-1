# class defining the ppl
class ppl:
  def __init__(self, n = 0, m = 0, 
                ppl_type = 'min', target = [], tv = [],
                A = [[]], rt = [], b = [], x = [], xt =[]):
    self.n = n                # number of variables
    self.m = m                # number of restrictions
    self.ppl_type = ppl_type  # 'min' or 'max'  
    self.target = target      # c values
    self.t_vars = tv          # x labels
    self.A = A                # A values, size m,n
    self.x = x                # x variable names, n size
    self.b = b                # b values, size m
    self.r_type = rt          # '>', '<' or '=' for each restriction
    self.x_type = xt          # '>', '<' or 'T' for each x

    def standard_form(self):
      sf_ppl = ppl()

      sf_ppl.sa = list(self.sa_func) \
      if self.ppl_type == 'max' \
      else [-c for c in self.sa_func]

      return sf_ppl