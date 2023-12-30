from helpers.generator import Generator
from helpers.splitter import Splitter
import argparse

parser = argparse.ArgumentParser(description='Generate Chapters or Split video by chapters',
                                 prog='python chapGenerator.py', epilog='Developed by: Sohaieb Azaiez')
parser.add_argument('-m', '--mode', dest='mode', action='store', default='generate', metavar='generate',
                    help='set split/generate mode (default: generate)')

args = parser.parse_args()

match args.mode:
    case 'generate':
        g = Generator()
        g.generate()

    case 'split':
        sp = Splitter()
        sp.split()
