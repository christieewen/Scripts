import numpy as np
import sys

def main(args):
   np.matrix(zip(*args[1])).T.T

if __name__ == __main__:
   main(sys.argv)
   
