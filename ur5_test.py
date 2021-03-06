from ur5 import *
import unittest

data1 = r"""\x00\x00\x04\xdf\x10\x00\x00\x00&\x00\x00\x00\x00\x00\x00\x01\xbc\xc8\
x01\x01\x01\x00\x00\x00\x00\x07\x00?\xf0\x00\x00\x00\x00\x00\x00?\xf0\x00\x00\x0
0\x00\x00\x00\x00\x00\x00\xfb\x01?\xfa\xb7\x19\xa0\x00\x00\x00?\xfa\xb6\xf3\xe0\
x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xbe\x9ee\xbaB?6FA\xe0\xf5\xbeA\xf2"\
x1b\xfd\xbf\xfa\x03\x93Q\x10\xb4`\xbf\xfa\x03\x93Q\x10\xb4`\x00\x00\x00\x00\x00\
x00\x00\x00\xbf\xa4\xffLB@>wA\xf5\\$A\xf5y]\xfd?\xf7\xa1\xe6\x00\x00\x00\x00?\xf
7\xa1\x9b\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\xbf\xb1\x0c\x9aB@M\xd3
A\xef\x1e\xb4A\xfc\x1bJ\xfd\xbf\xc7U\xd6\x88\x85\xa3\x00\xbf\xc7T\xaa\x88\x85\xa
3\x00\x00\x00\x00\x00\x00\x00\x00\x00\xbd\x0f\xab\xccB?\xe2NB#\xae\x19B\x1b\x84d
\xfd?\xee\xad\x1c@\x00\x00\x00?\xee\xac\xea\x00\x00\x00\x00\x00\x00\x00\x00\x00\
x00\x00\x00=\xa5\x88\xb9B?6FB!\xeb\x81B\x14<,\xfd?\xe1\xb0z\xe0\x00\x00\x00?\xe1
\xb0\xe0@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00=N#\x03B?t\xbcB\x1e\\$A\xef
W\xef\xfd\x00\x00\x005\x04?\xc9\xf1 \xaa*Q\xbc\xbf\xdcH\xe2\xa9\xcc\xf5-?\xe0&\x
ae#~\xda\xbf?\xf5^3v\xdc\x1d\xc5?\xd0=\xa4\x1b\x94\x13s?\xed\xce\x06\xffR\x97U\x
00\x00\x00\xe1\x05-\xfcq\x00\x12\xd1-\x9f\xca\x0e93\xe2\xcd\x1b,\xc2\x8e\x1b\xe0
0\x17/\xfb\xbe\xf55\r\xc31\x98\xe4?\xf9\x07L\xcc\xa6Br\xbf\xea\xb1\xf6\x94\xc7\x
ee\x81\xc0\x1c\r|w\xee-)\xbe\xfa\x1a\xa2\xc5:u\x8d\xbf\x08xk3\xda\xe6\xa8?"s\xc5
\xd5\xc1\x0e`\xbff\xd1\x7f\xea\x07\x07\x00\xbf\xd2\xb9Uz\xcb\xed\xf5>\xdd\xb4\xd
e\xe3)\x87\xef?#M\xaa\xe7V\xb8\xa5\x00\x00\x00\x00\x00\x00\x00\x00?\xb6\xe6\x965
\xa1\x12E@z\x81\x0b\x99\xa7\x8d\xfc\xc0\x80\xcb\xfc\xb6\xfdv @\\b\xcb\xfe1\x03\x
f0?\xb8Y\xd1\x17\x86\xac\xdf?\xb5.\x08\xe6F\x91&?\xf9\x1f,\xaa\xcc\xd9\xeb?Po\x9
7u3\x99\x07\xbfb\xe8\x87\x86\xa2\xd8\xd2?\xf9\x1b|Q\x9c\xb6K\xbf\xf9\x1e\xc23\xb
d\x0e\xda\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x005\t@\x10\x1
4\xa0\xf7\xa5\x1b\x96@\x02\x90\x06\xa14\x8d\xa1?\xf5\xec3"\xad\x1a\xce\xbf\xd9\x
06k\x15Fh\xcb\xbf\xe8z\x02da\xe0Z\xbf\xe0I\x080\x15E\xb9\x00\x00\x00H\x03\x00\x0
2\x00\x00\x00\x01\x00\x00\x01\x01?p\x7f\xc0\x00\x00\x00\x00?p\x7f\xc0\x00\x00\x0
0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00A\x
dc(\x00B@\x08\xde?\x80UD:\x02\x8d\xe3\x01\x00\x00\xc4ex\xaa\x00\x00\x00%\x02\x01
\x01?\xa5\xd5\x97\x00\x00\x00\x00?\xa3\xc30\xe0\x00\x00\x00C\xe1<n\x18>\x87+\x02
C\xfa\x00\x00\xfd\x00\x00\x01\xbd\x06\xc0\x19W\x99(,/c@\x19W\x99(,/c\xc0\x19W\x9
9(,/c@\x19W\x99(,/c\xc0\x19W\x99(,/c@\x19W\x99(,/c\xc0\x19W\x99(,/c@\x19W\x99(,/
c\xc0\x19W\x99(,/c@\x19W\x99(,/c\xc0\x19W\x99(,/c@\x19W\x99(,/c@\n\xbb\x94\xed\x
dd\xc6\xb1@D\x00\x00\x00\x00\x00\x00@\n\xbb\x94\xed\xdd\xc6\xb1@D\x00\x00\x00\x0
0\x00\x00@\n\xbb\x94\xed\xdd\xc6\xb1@D\x00\x00\x00\x00\x00\x00@\n\xbb\x94\xed\xd
d\xc6\xb1@D\x00\x00\x00\x00\x00\x00@\n\xbb\x94\xed\xdd\xc6\xb1@D\x00\x00\x00\x00
\x00\x00@\n\xbb\x94\xed\xdd\xc6\xb1@D\x00\x00\x00\x00\x00\x00?\xf0\xc1R8-se?\xf6
W\x18J\xe7D\x87?\xd0\x00\x00\x00\x00\x00\x00?\xf3333333?\xd0\x00\x00\x00\x00\x00
\x00\x00\x00\x00\x00\x00\x00\x00\x00\xbf\xdb333333\xbf\xd9\x1a\x9f\xbev\xc8\xb4\
x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
x00\x00\x00\x00?\xb6\xd3\x1f\xcd"""


class UR5Test( unittest.TestCase ): 
    def XtestParseData0( self ):
        d = "".join( [x.strip() for x in data1.split('\n')] )
        d2 = eval( "'" + d + "'" )
        print len(d2), "".join( ["%02X " % ord(x) for x in d2[:20]] )
        print parseData( d2 )

    def testParseData( self ):
        d = open("logs/ur5_150116_123711.bin", "rb" ).read()
        print parseData( d )

if __name__ == "__main__":
    unittest.main() 

# vim: expandtab sw=4 ts=4

