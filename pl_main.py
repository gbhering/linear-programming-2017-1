from pl_parser import parse_input

def main():
  count = 1
  for p in parse_input():
    print("Problem {}:".format(count))
    print(p)
    print("")
    count += 1

if __name__ == '__main__':
  main()