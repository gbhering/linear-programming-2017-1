from pl_util import print_ppl
from pl_base_classes import ppl

# All the time we trust the input is well formed #
# TODO: Specify somewhere what's a well formed input #
 
# returns a list of ppl objects
def read_from_file(fname, verbose):
  parsed_ppls=[]
  try:
    with open(fname, mode='r+') as in_file:
      for t in range(1, int(in_file.readline())+1):
        if verbose: print("Case {}:".format(t))

        parsed_ppl = ppl()

        # read size of the problem
        n, m = map(int, in_file.readline().split())
        parsed_ppl = ppl(n=n, m=m)
        
        # read the objective function
        temp = in_file.readline().split()
        parsed_ppl.ppl_type = temp[0]
        parsed_ppl.target = [float(c) for c in temp[1:]]
        parsed_ppl.t_vars = ['x'+str(i) for i in range(1,len(temp[1:])+1)]

        # read the restrictions
        temp = [ in_file.readline().split() for j in range(m) ]
        parsed_ppl.A = [list(map(float,r[:-2])) for r in temp]
        parsed_ppl.r_type = [r[-2] for r in temp]
        parsed_ppl.b = [float(r[-1]) for r in temp]
        parsed_ppl.x = ['x'+str(i) for i in range(1,n+1)]

        # read the variable types
        parsed_ppl.x_type = in_file.readline().split()

        parsed_ppls.append(parsed_ppl)

        if verbose:
          print_ppl(parsed_ppl)
          print('')

    return parsed_ppls

  except FileNotFoundError:
    print("Couldn't find the file", fname)
    exit()


# returns a list of ppl objects
def read_from_input(verbose):
  parsed_ppls = []

  for t in range(1, int(input())+1):
    if verbose: print("Case {}:".format(t))

    # read size of the problem
    n, m = map(int, input().split())
    parsed_ppl = ppl(n=n, m=m)
    

    # read the objective function
    temp = input().split()
    parsed_ppl.ppl_type = temp[0]
    parsed_ppl.target = [float(c) for c in temp[1:]]
    parsed_ppl.t_vars = ['x'+str(i) for i in range(len(1,temp[1:])+1)]

    # read the restrictions
    temp = [ input().split() for j in range(m) ]
    parsed_ppl.A = [list(map(float,r[:-2])) for r in temp]
    parsed_ppl.r_type = [r[-2] for r in temp]
    parsed_ppl.b = [float(r[-1]) for r in temp]
    parsed_ppl.x = ['x'+str(i) for i in range(1,n+1)]

    # read the variable types
    parsed_ppl.x_type = input().split()

    parsed_ppls.append(parsed_ppl)

    if verbose:
      print_ppl(parsed_ppl)
      print('')

  return parsed_ppls

def parse_ppl(fname=None, verbose=True):
  if fname:
    read_from_file(fname,verbose=verbose)
  else:
    read_from_input(verbose=verbose)

if __name__ == '__main__':
  read_from_input(fname=None, verbose=True)