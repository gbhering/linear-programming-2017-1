from sys import argv
from pl_parser import parse_ppl

def show_help():
  print("Usage: {} [-q|-i input_file]".format(argv[0]))
  print("-i\tuse to read from file instead of stdin")
  print("-q\trun program quietly")

if __name__ == '__main__':
  fname = None
  verbose = True
  
  if '-h' in argv:
    show_help()
    exit()

  if '-q' in argv:
    verbose = False

  if '-i' in argv:
    try:
      fname = argv[argv.index('-i')+1]
    except:
      show_help()
      exit()

  parse_ppl(fname=fname, verbose=verbose)