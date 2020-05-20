import urllib.request
from tqdm import tqdm
from optparse import OptionParser

parse = OptionParser("""
Download.py [Options]

======================

-u / --url   >>> : Link
-d / --dir  >>> : dir

ex:
    Download.py -u https://www.kau.edu.sa/Files/030/Files/60761_Linux.pdf
    Download.py --url https://www.kau.edu.sa/Files/030/Files/60761_Linux.pdf
    Download.py -d C://User/Mahmoud/Desktop/
    Download.py --dir C://User/Mahmoud/Desktop/
""")

parse.add_option("-u", "--url", dest="url", type="string", help="url Please")
parse.add_option("-d", "--dir", dest="dir", type="string", help="dir Please")
(options, args) = parse.parse_args()
if options.url != None:
    print(parse.usage)
    exit(0)
else:
    url = str(options.url)
    if options.dir != None:
        d = str(options.dir)
        file_mame = url.split("/")[-1]
        opfile = open(d + "" + file_mame + "wb")
    else:
        opfile = open(file_mame+"wb")
    openurl = urllib.request.urlopen(url)
    print(openurl.info())
    block_size = 590
    file_size = int(openurl.headers("Content Length"))
    for i in tqdm(range(file_size)):
        buffer = openurl.read(block_size)
        i = i + block_size
        opfile.write(buffer)
    opfile.close()
