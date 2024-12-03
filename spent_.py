from docopt import docopt
from p import *
from tabulate import tabulate

usage='''
usage:
    spent_.py --init
    spent_.py --show [<name>]
    spent_.py --add <price> <name> [<massage>]
    spent_.py --remove <name>
    spent_.py --update <price> <name>

'''
args = docopt(usage)

if args['--init']:
    init()
    print('Your Table Successfully Created')
if args['--show']:
    name = args['<name>']
    price , results=show(name)
    print('Total expences:',price)
    print(tabulate(results))
if args['--add']:
    try:
        price = float(args['<price>'])
        add(price , args['<name>'] , args['<massage>'])
        print('item aded')
    except:
        print(usage)
if args['--remove']:
    name = args['<name>']
    remove(name)
    print('item deleted')
if args['--update']:
    price = args['<price>']
    name = args['<name>']
    update(price,name)
    print('item updated')