import re
import sys
import os



filename = sys.argv[1]
new_filename = filename + "_0"
with open(filename, "r") as r, open(new_filename, "w") as w:
        for line in r:
            if re.search(r"95\.211\.243\.137\t'556':.+'11058'|'10894'|'10778'", line):
                line = re.sub(r"95\.211\.243\.137\t'556':", r"194.42.152.44\t'10860':", line)
            #print(line)
            w.writelines(line)
r.close()
w.close()
os.replace(new_filename,filename)