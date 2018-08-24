import argparse

def parseArgs():
    parser = argparse.ArgumentParser(description='A KNN and LDA approach for recognising handwriting numbers using the MNIST Dataset.')

    # parser.add_argument('integers', metavar='N', type=int, nargs='+',
    #                     help='interger list')

    # parser.add_argument('--sum', action='store_const',
    #                     const=sum, default=max,
    #                     help='sum the integers (default: find the max)')

    args = parser.parse_args()
    # print(args.sum(args.integers))
