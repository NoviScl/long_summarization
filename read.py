#import json
import re

# f_sections = open('train_sections.txt', 'w')
# f_summary = open('train_summary.txt', 'w')

# with open('train.txt', 'r') as f:
# 	for i in range(100):
# 		line = f.readline()
# 		line_dict = json.loads(line)
# 		f_summary.write(str(line_dict['abstract_text'])+'\n')
# 		f_sections.write(str(line_dict['sections'])+'\n')

# f_sections.close()
# f_summary.close()

# with open('train_sections.txt', 'r') as f:
# 	summ = 0
# 	num = 0
# 	for line in list(f):
# 		line2 = eval(line)
# 		num += len(line2)
# 		#summ += sum([len(l) for l in line2])
# 		summ += sum([len(sent.strip().split()) for sec in line2 for sent in sec])

# 	print (summ, num, summ/num)

# average: 13.2 sentences per section
# 469 words per section

def remove_tag(raw):
	#remove all tags and linebreakers
	clean = re.sub("<.*?>", "", raw)
	clean = re.sub("[\r\n]+", "", clean)
	return clean

# process summary txt file
f_out = open('train_summary_processed.txt', 'w')
with open('train_summary.txt', 'r') as f:
	i = 0
	f_l = f.readlines()
	for line in f_l:
		new_f =[]
		line2 = eval(line.strip())
		for sent in line2:
			new_sent = remove_tag(sent)
			new_f.append(new_sent)
		new_line = (' '.join(new_f))+'\n'
		f_out.write(new_line)
		i += 1
print (i)
f_out.close()

# with open('train_summary_processed.txt', 'r') as f:
# 	fl = list(f)
# 	print (sum([len(s.strip().split()) for s in fl])/len(fl))

# ave: 110 words per summary

