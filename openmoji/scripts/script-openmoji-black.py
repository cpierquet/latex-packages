#individuals pdf must be renamed 0001-name.pdf (because more than 1000 files)
#so, the merged file will be with 'correct' order

import glob
f = open("aaaa.txt","w")     #file for generated macro
g = open("aaab.txt","w")     #file for generated macro for doc

n = 1
for filepath in glob.iglob('*.pdf'):
    res = r'\defineOpenmojiBlack{' + str(n) + r'}{' + filepath[19:-4].lower() + r'}' + '\n'
    resb = r'\showcaseopenmojiblack{' + filepath[19:-4].lower() + r'}{' + str(n) + r'}' + '\n'
    f.write(res)
    g.write(resb)
    n += 1
f.close()
g.close()