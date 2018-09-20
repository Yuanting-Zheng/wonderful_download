f = open('PRJNA263122.txt', 'r')
f1 = open('download_info', 'w')
f2 = open('download_dict','w')
f3 = open('name_list','w')
download_dict = {}
lines = f.readlines()
name_list = []
ex_line = 'ascp -k 1 -QT -l 300m -P33001 -i /Users/mac/Applications/Aspera\ CLI/etc/asperaweb_id_dsa.openssh era-fasp@fasp.sra.ebi.ac.uk:'
back_line = ' /Volumes/storage/262'
for line in lines[1:]:
    line = line.strip()
    elements = line.split()
    sample = elements[1][3:]
    acps = elements[1].split(';')
    acp_1 = acps[0][17:]
    acp_2 = acps[1][17:]
    d1 = ex_line + acp_1 + back_line
    d2 = ex_line + acp_2 + back_line

    name_1 = acp_1[-21:]
    name_2 = acp_2[-21:]
    name_list.append(name_1)
    name_list.append(name_2)

    download_dict[name_1]=d1
    download_dict[name_2]=d2

    f1.write(d1 + '\n')
    f1.write(d2 + '\n')




f2.write(str(download_dict))
f3.write(str(name_list))
f.close()
f1.close()
f2.close()
f3.close()



