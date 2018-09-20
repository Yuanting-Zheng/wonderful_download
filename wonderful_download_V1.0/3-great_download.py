import os
f = open('md5_dict','r')
f1 = open('name_list','r')
f2 = open('download_dict','r')

os.chdir("/Volumes/storage/262")
a = f.read()
md5_dict = eval(a)

b = f1.read()
name_list = eval(b)

c = f2.read()
download_dict = eval(c)

for one in name_list:
    print(one)
    os.system("pwd")
    while os.path.exists(one) == False:
        print("checking file")
        os.system('echo os_working_now')
        os.system(download_dict[one])

    print("md5 running")
    md5_status = os.popen('md5sum ' + one)
    md5_result = md5_status.read()
    print(md5_result.strip())
    print("True " + one + ' ' + md5_dict[one])
    md5 = md5_result.split(' ')[0]

    while md5 != md5_dict[one]:
        command = 'rm '+ one
        command2 = 'rm '+one+'.aspx'
        os.system(command)
        os.system(command2)
        os.system(download_dict[one])
        while os.path.exists(one) == False:
            os.system(download_dict[one])
        md5_status = os.popen('md5sum ' + one)
        md5_result = md5_status.read()
        print(md5_result.strip())
        print("True " + one + ' ' + md5_dict[one])
        md5 = md5_result.split(' ')[0]

    print(one +' is done')


print('bye')





