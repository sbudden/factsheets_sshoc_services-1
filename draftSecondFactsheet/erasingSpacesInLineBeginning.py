__author__ = 'Michael Dahnke'

import re

c = 0

infile = open('../../corpora/useCases/01UDPipeResearchQuestion/useCaseOfLanguageResourceSwitchboard.html', encoding='UTF-8')
content = infile.read()
infile.close()

while '\n ' in content:
    content = re.sub('\n ', '\n', content, re.U)

while '\n\n' in content:
    content = re.sub('\n\n', '\n', content, re.U)

while '\n\n   ' in content:
    content = re.sub('\n\n	', '\n', content, re.U)

while '\n   ' in content:
    content = re.sub('\n	', '\n', content, re.U)

outfile = open('../../corpora/useCases/01UDPipeResearchQuestion/useCaseOfLanguageResourceSwitchboard.html', mode='w', encoding='UTF-8')
outfile.write(content)
outfile.close()

