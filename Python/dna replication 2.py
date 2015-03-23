bases = {'A':'T','T':'A','G':'C','C':'G'}
codons = {
'TTT':'Phe',
'TTC':'Phe',
'TTA':'Leu',
'TTG':'Leu',
'TCT':'Ser',
'TCC':'Ser',
'TCA':'Ser',
'TCG':'Ser',
'TAT':'Tyr',
'TAC':'Tyr',
'TAA':'STOP',
'TAG':'STOP',
'TGT':'Cys',
'TGC':'Cys',
'TGA':'STOP',
'TGG':'Trp',
'CTT':'Leu',
'CTC':'Leu',
'CTA':'Leu',
'CTG':'Leu',
'CCT':'Pro',
'CCC':'Pro',
'CCA':'Pro',
'CCG':'Pro',
'CAT':'His',
'CAC':'His',
'CAA':'Gln',
'CAG':'Gln',
'CGT':'Arg',
'CGC':'Arg',
'CGA':'Arg',
'CGG':'Arg',
'ATT':'Ile',
'ATC':'Ile',
'ATA':'Ile',
'ATG':'Met',
'ACT':'Thr',
'ACC':'Thr',
'ACA':'Thr',
'ACG':'Thr',
'AAT':'Asn',
'AAC':'Asn',
'AAA':'Lys',
'AAG':'Lys',
'AGT':'Ser',
'AGC':'Ser',
'AGA':'Arg',
'AGG':'Arg',
'GTT':'Val',
'GTC':'Val',
'GTA':'Val',
'GTG':'Val',
'GCT':'Ala',
'GCC':'Ala',
'GCA':'Ala',
'GCG':'Ala',
'GAT':'Asp',
'GAC':'Asp',
'GAA':'Glu',
'GAG':'Glu',
'GGT':'Gly',
'GGC':'Gly',
'GGA':'Gly',
'GGG':'Gly'
}


print 'Input a DNA sequence: '
strand = raw_input().replace(' ','')
codon = ''
otherstrand = ''


for i in range(0, len(strand), 3):
	for j in range(3):
		otherstrand += bases[strand[i+j]] + " "
	if strand[i:i+3] in codons:
		codon += codons[strand[i:i+3]] + " "
print otherstrand
print codon