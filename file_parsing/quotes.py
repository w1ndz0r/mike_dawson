import sys

filename = sys.argv[1]
#filename = 'in.txt'
new_filename = filename + "_done"
with open(filename, "r") as r, open(new_filename, "w") as w:
        for line in r:
            line = line.split('\t')
            #print(line[0])
            date = line[0].split(' ')
            s = date[1]
            day = s[:-1]
            if date[0] == 'Jan': month = '01'
            if date[0] == 'Feb': month = '02'
            if date[0] == 'Mar': month = '03'
            if date[0] == 'Apr': month = '04'
            if date[0] == 'May': month = '05'
            if date[0] == 'Jun': month = '06'
            if date[0] == 'Jul': month = '07'
            if date[0] == 'Aug': month = '08'
            if date[0] == 'Sep': month = '09'
            if date[0] == 'Oct': month = '10'
            if date[0] == 'Nov': month = '11'
            if date[0] == 'Dec': month = '12'
            year = date[2]
            fulldate = year+'.'+month+'.'+day+' 00:00'
            line[0] = fulldate
            line[5] = line[5].replace(",","")+"\n"
            line = line[0:6]
            line = ','.join(line)
            #print(line)
            w.writelines(line)
r.close()
w.close()
