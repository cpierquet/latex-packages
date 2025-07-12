#individuals pdf must be renamed 001-name.pdf (because less than 1000 files)
#so, the merged file will be with 'correct' order

import glob
f = open("aaaa.txt","w")     #file for generated macro
g = open("aaab.txt","w")     #file for generated macro for doc

n = 1
res = ""
for filepath in glob.iglob('*.pdf'):
    res = r'\GenerateTablerIconFilled{' + str(n) + r'}{' + filepath[4:-4] + r'}' + '\n'
    resb = r'\showcasetablericonfilled{' + filepath[4:-4] + r'}{' + str(n) + r'}' + '\n'
    f.write(res)
    g.write(resb)
    n += 1
f.close()
g.close()