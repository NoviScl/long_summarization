import json
import re 

# change this to your data directory
FILE_DIR = "../pubmed/train.txt"
# take the first 10000 lines
LINES = 10

# this file is the input data (articles)
f_article = open("articles.txt", "w+")
# this file stores the target data (summary)
f_summary = open("summary.txt", "w+")

def remove_tag(raw):
	#remove all tags and linebreakers
	clean = re.sub("<.*?>", "", raw)
	clean = re.sub("[\r\n]+", "", clean)
	return clean

# for article, each line is a list of sections(lists)
# for summary, each line is a list of summary sentences

with open(FILE_DIR, 'r') as f:
	for i in range(LINES):
		line = f.readline()
		# convert to a dict
		line_dict = json.loads(line)
		summary_list = line_dict['abstract_text']
		article_lists = line_dict['sections']

		new_summ = []
		for sent in summary_list:
			sent = remove_tag(sent)
			new_summ.append(sent)
		new_line = ' '.join(new_summ) + '\n'
		f_summary.write(new_line)

		article_lists = [' '.join(section) for section in article_lists]
		new_line = ' '.join(article_lists)
		new_line = remove_tag(new_line)
		f_article.write(new_line + '\n')

f_article.close()
f_summary.close()

