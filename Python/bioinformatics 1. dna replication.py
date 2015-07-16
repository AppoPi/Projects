
print 'Input a DNA sequence: '
strand = raw_input()
compl = ''

for i in range(len(strand)):
	if strand[i] == 'A':
		compl += 'T'
	elif strand[i] == 'T':
		compl += 'A'
	elif strand[i] == 'G':
		compl += 'C'
	elif strand[i] == 'C':
		compl += 'G'
	else:
		compl += strand[i]

print compl

output = ''
strand = strand.replace(' ', '')
for i in range(0, len(strand), 3):
	codon = strand[i:i+3]
	if codon == 'TTT' or codon == 'TTC':
		output += 'Phe '
	elif codon == 'TTA' or codon == 'TTG' or codon == 'CTT' or codon == 'CTC' or codon == 'CTA' or codon == 'CTG':
		output += 'Leu '
	elif codon == 'ATT' or codon == 'ATC' or codon == 'ATA':
		output += 'Ile '
	elif codon == 'ATG':
		output += 'Met '
	elif codon == 'GTT' or codon == 'GTC' or codon == 'GTA' or codon == 'GTG':
		output += 'Val '
	elif codon == 'TCT' or codon == 'TCC' or codon == 'TCA' or codon == 'TCG':
		output += 'Ser '
	elif codon == 'CCT' or codon == 'CCC' or codon == 'CCA' or codon == 'CCG':
		output += 'Pro '
	elif codon == 'ACT' or codon == 'ACC' or codon == 'ACA' or codon == 'ACG':
		output += 'Thr '
	elif codon == 'GCT' or codon == 'GCC' or codon == 'GCA' or codon == 'GCG':
		output += 'Ala '
	elif codon == 'TAT' or codon == 'TAC':
		output += 'Tyr '
	elif codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
		output += 'Stop'
	elif codon == 'CAT' or codon == 'CAC':
		output += 'His '
	elif codon == 'CAA' or codon == 'CAG':
		output += 'Gln '
	elif codon == 'AAT' or codon == 'AAC':
		output += 'Asn '
	elif codon == 'AAA' or codon == 'AAG':
		output += 'Lys '
	elif codon == 'GAT' or codon == 'GAC':
		output += 'Asp '
	elif codon == 'GAA' or codon == 'GAG':
		output += 'Glu '
	elif codon == 'TGT' or codon == 'TGC':
		output += 'Cys '
	elif codon == 'TGG':
		output += 'Trp '
	elif codon == 'CGT' or codon == 'CGC' or codon == 'CGA' or codon == 'CGG' or codon == 'AGA' or codon == 'AGG':
		output += 'Arg '
	elif codon == 'AGT' or codon == 'AGG':
		output += 'Ser '
	elif codon == 'GGT' or codon == 'GGC' or codon == 'GGA' or codon == 'GGG':
		output += 'Gly '

print output