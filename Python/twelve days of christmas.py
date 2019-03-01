g=['Twelve Drummers Drumming','Eleven Pipers Piping','Ten Lords a Leaping','Nine Ladies Dancing','Eight Maids a Milking','Seven Swans a Swimming','Six Geese a Laying','Five Golden Rings','Four Calling Birds','Three French Hens','Two Turtle Doves','A Partridge in a Pear Tree\n',]
d=['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth','eleventh','twelfth']
for i in range(12):
 print 'On the '+d[i]+' day of Christmas\nmy true love sent to me:'
 print '\n'.join(g[11-i:])
 g[11] = 'and A Partridge in a Pear Tree\n'