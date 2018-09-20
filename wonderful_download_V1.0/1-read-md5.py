f = open("MD5infoPRJNA263122.txt", "r")
f1 = open("md5_dict",'w')
lines = f.readlines()
md5info = {}
for line in lines[1:]:
    line = line.strip()
    name_md5 = line.split('\t')
    name = name_md5[0]
    md5s = name_md5[1].split(';')
    md5_1_name = name + '_1.fastq.gz'
    md5_2_name = name + '_2.fastq.gz'
    md5_1 = md5s[0]
    md5_2 = md5s[1]
    md5info[md5_1_name] = md5_1
    md5info[md5_2_name] = md5_2

print(md5info)
f1.write(str(md5info))
f1.close()

