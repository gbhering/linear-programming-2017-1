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

        # read size of the problem
        n, m = [int(nm) for nm in in_file.readline().split()]
        
        # read the objective function
        temp = in_file.readline().split()
        sa_type = temp[0]
        sa_func = [float(c) for c in temp[1:]]

        # read the restrictions
        temp = [ in_file.readline().split() for j in range(m) ]
        A = [list(map(float,r[:-2])) for r in temp]
        r_type = [r[-2] for r in temp]
        b = [float(r[-1]) for r in temp]

        # read the variable types
        x_type = in_file.readline().split()

        parsed_ppl = ppl(
          n, m, sa_type, sa_func, A, r_type, b, x_type)
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
    n, m = [int(nm) for nm in input().split()]
    
    # read the objective function
    temp = input().split()
    sa_type = temp[0]
    sa_func = [float(c) for c in temp[1:]]

    # read the restrictions
    temp = [ input().split() for j in range(m) ]
    A = [list(map(float,r[:-2])) for r in temp]
    r_type = [r[-2] for r in temp]
    b = [float(r[-1]) for r in temp]

    # read the variable types
    x_type = input().split()

    parsed_ppl = ppl(
      n, m, sa_type, sa_func, A, r_type, b, x_type)
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