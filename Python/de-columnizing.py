import re

input1 = '''24
This is an example piece of text. This is an exam-
ple piece of text. This is an example piece of
text. This is an example
piece of text. This is a +-----------------------+
sample for a challenge.  |                       |
Lorum ipsum dolor sit a- |       top class       |
met and other words. The |        feature        |
proper word for a layout |                       |
like this would be type- +-----------------------+
setting, or so I would
imagine, but for now let's carry on calling it an
example piece of text. Hold up - the end of the
                 paragraph is approaching - notice
+--------------+ the double line break for a para-
|              | graph.
|              |
|   feature    | And so begins the start of the
|   bonanza    | second paragraph but as you can
|              | see it's only marginally better
|              | than the other one so you've not
+--------------+ really gained much - sorry. I am
                 certainly not a budding author
as you can see from this example input. Perhaps I
need to work on my writing skills.'''

input2 = '''22
+-------------+ One hundred and fifty quadrillion,
|             | seventy-two trillion, six hundred
| 150 072 626 | and twenty-six billion, eight hun-
| 840 312 999 | dred and fourty million, three
|             | hundred and thirteen thousand sub-
+-------------+ tract one is a rather large prime
                number which equals one to five if
calculated modulo two to six respectively.

However, one other rather more in- +-------------+
teresting number is two hundred    |             |
and twenty-one quadrillion, eight  | 221 806 434 |
hundred and six trillion, four     | 537 978 679 |
hundred and thirty-four billion,   |             |
five hundred and thirty-seven mil- +-------------+
million, nine hundred and seven-
                                ty-eight thousand,
+-----------------------------+ six hundred and
|                             | seventy nine,
| Subscribe for more Useless  | which isn't prime
|      Number Facts(tm)!      | but is the 83rd
+-----------------------------+ Lucas number.'''

def decolumnize(text):
	p = '(?<=[a-z])-[ \n]|[ ]*\+[-]*\+|\|[A-z0-9()!., ]+\||  '
	text = re.sub(p, '', text)
	text = re.sub('\n(?!\n)', '', text)
	text = re.sub('\n', '\n\n', text)
	return text[text.index(' ')+1:]

print decolumnize(input2)