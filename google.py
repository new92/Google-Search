#Imports:

import sys
import urllib.parse
import webbrowser

#End of imports

#Program

def main(args):
    def quote(arg):
        if ' ' in arg:
            arg = '"%s"' % arg
        return urllib.parse.quote_plus(arg)

    qstring = '+'.join(quote(arg) for arg in args)
    url = urllib.parse.urljoin('https://www.google.com/search', '?q=' + qstring)
    webbrowser.open(url)

if __name__ == '__main__':
    main(sys.argv[1:])

#End of the program 
