'''
IMPORTS

def main(main parameters):
    DO THINGS
    
if __name__ == '__main__':
    DEFINE ARGUMENT PARSER
    PARSE ARGS
    VALIDATE OR MANIPULATE ARGS, IF NEEDED
    main(arguments)
'''

import argparse

def main(character, number):
    print(character * number)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int, help='A number')
    parser.add_argument('-c', type=str, help='Character to print', default='#')
    args = parser.parse_args()
    
    main(args.c, args.number)
    