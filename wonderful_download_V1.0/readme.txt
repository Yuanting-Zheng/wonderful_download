#该下载脚本是为了从ENA上高速下载原始数据并且防止数据错误而设置md5check的脚本

# 准备两个文件
#（1）下载序列的md5值 eg.md5info
#（2）下载序列的ftp地址(fasq_ftp) eg.PRJNA301892


# 在python文件1和2中对应修改读入文件的名称
#修改 存储地址
#注意，文件3中的目录切换到存储地址中

# 得到 md5.dict name_list download_dict 三个文件检查之后，运行3即可