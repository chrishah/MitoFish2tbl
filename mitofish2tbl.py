#!/usr/bin/python

import sys

known_features = ['CDS', 'rRNA', 'tRNA', 'D-loop']
features = []

def parse_startend(text):
	if text.startswith('complement'):
		startend = list(reversed(text.replace('complement(','').replace(')','').split("..")))
	else:
		startend = text.split("..")
		
	return "%s\t%s" %(startend[0],startend[1])
	
mitofish = sys.argv[1]
print "mitofish file to convert: %s" %mitofish
outfile = "%s.tbl" %".".join(mitofish.split(".")[:-1])
print "writing to: %s" %outfile
fh = open(mitofish)
sampleID = fh.readline().split("\t")[0]

for line in fh.readlines():
#	print line.rstrip()
	cols = line.rstrip().split("\t")
#	print cols
	if cols[1]:
		if cols[1] in known_features:
#			print cols[1]
#			print sorted(startend)
			features.append([cols[1]])
			features[-1].extend(cols[2:])
#		else:
#			print "unknown feature"
	elif cols[3]:
		if features:
			features[-1].extend(cols[3:])

fh = open(outfile,'w')
fh.write(">Feature %s\n" %sampleID)
for i in range(len(features)):
#	print '#',i,len(features[i]),features[i]
	if features[i][0] == 'CDS':
		#print start / end
#		if features[i][1].startswith('complement'):
#			startend = list(reversed(features[i][1].replace('complement(','').replace(')','').split("..")))
#		else:
#			startend = features[i][1].split("..")
			
		fh.write("%s\tgene\n\t\t\tgene\t%s\n" %(parse_startend(features[i][1]),features[i][5]))


		fh.write("%s\tCDS\n" %(parse_startend(features[i][1])))
		for j in range(6, len(features[i]), 2):
			fh.write("\t\t\t%s\t%s\n" %(features[i][j],features[i][j+1]))
		fh.write("\t\t\t%s\t%s\n" %(features[i][2],features[i][3]))

	elif features[i][0] == 'rRNA' or features[i][0] == 'tRNA':
		fh.write("%s\t%s\n" %(parse_startend(features[i][1]),features[i][0]))
		for j in range(2, len(features[i]), 2):
			fh.write("\t\t\t%s\t%s\n" %(features[i][j],features[i][j+1]))
	elif features[i][0] == 'D-loop':
		fh.write("%s\t%s\n" %(parse_startend(features[i][1]),features[i][0]))
		for j in range(2, len(features[i]), 2):
                        fh.write("\t\t\t%s\t%s\n" %(features[i][j],features[i][j+1]))

#print "\t\t\tgene\t%s" %(startend[0],startend[1],features[i][5])
		
