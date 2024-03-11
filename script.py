
import os
import random

# 指定文件夹路径
folder_path = r'E:\lizhengcan\ISPRS-CD\train_set1'

# 获取文件夹中所有文件名
file_names = os.listdir(os.path.join(folder_path,"gt"))
# 将文件名保存到list.txt
with open(os.path.join(folder_path,'list.txt'), 'w') as file:
    for file_name in file_names:
        file.write(file_name + '\n')

# 随机选择500行作为test集
test_lines = random.sample(file_names, 500)

# 将选中的行从lines中移除，剩余的作为train集
for line in test_lines:
    file_names.remove(line)

train_lines=file_names
# 将test集写入test.txt
train_path=os.path.join(folder_path,'train')
if not os.path.exists(train_path):
    os.makedirs(train_path)
test_path=os.path.join(folder_path,'test')
if not os.path.exists(test_path):
    os.makedirs(test_path)

with open(os.path.join(test_path,'test.txt'), 'w') as test_file:
    for line in test_lines:
        test_file.write(line+ '\n')

# 将train集写入train.txt
with open(os.path.join(train_path,'train.txt'), 'w') as train_file:
    for line in train_lines:
        train_file.write(line+ '\n')




import shutil

# 源文件夹和目标文件夹路径

source_folder1 = os.path.join(folder_path,"gt")
target_folder1 = os.path.join(train_path,"gt")
source_folder2 = os.path.join(folder_path,"T1")
target_folder2 = os.path.join(train_path,"T1")
source_folder3 = os.path.join(folder_path,"T2")
target_folder3 = os.path.join(train_path,"T2")
if not os.path.exists(target_folder1):
    os.makedirs(target_folder1)
if not os.path.exists(target_folder2):
    os.makedirs(target_folder2)
if not os.path.exists(target_folder3):
    os.makedirs(target_folder3)

for filename in train_lines:

    source_file_path=os.path.join(source_folder1,filename)
    target_file_path=os.path.join(target_folder1,filename)
    shutil.copyfile(source_file_path, target_file_path)
    source_file_path=os.path.join(source_folder2,filename[:-4]+"第二期影像.tif")
    target_file_path=os.path.join(target_folder2,filename[:-4]+"第二期影像.tif")
    shutil.copyfile(source_file_path, target_file_path)
    source_file_path=os.path.join(source_folder3,filename[:-4]+"第三期影像.tif")
    target_file_path=os.path.join(target_folder3,filename[:-4]+"第三期影像.tif")
    shutil.copyfile(source_file_path, target_file_path)



source_folder1 = os.path.join(folder_path,"gt")
target_folder1 = os.path.join(test_path,"gt")
source_folder2 = os.path.join(folder_path,"T1")
target_folder2 = os.path.join(test_path,"T1")
source_folder3 = os.path.join(folder_path,"T2")
target_folder3 = os.path.join(test_path,"T2")
if not os.path.exists(target_folder1):
    os.makedirs(target_folder1)
if not os.path.exists(target_folder2):
    os.makedirs(target_folder2)
if not os.path.exists(target_folder3):
    os.makedirs(target_folder3)

for filename in test_lines:
    source_file_path = os.path.join(source_folder1, filename)
    target_file_path = os.path.join(target_folder1, filename)
    shutil.copyfile(source_file_path, target_file_path)
    source_file_path = os.path.join(source_folder2, filename[:-4] + "第二期影像.tif")
    target_file_path = os.path.join(target_folder2, filename[:-4] + "第二期影像.tif")
    shutil.copyfile(source_file_path, target_file_path)
    source_file_path = os.path.join(source_folder3, filename[:-4] + "第三期影像.tif")
    target_file_path = os.path.join(target_folder3, filename[:-4] + "第三期影像.tif")
    shutil.copyfile(source_file_path, target_file_path)



# 目标文件夹路径
destination_folder = os.path.join(folder_path,"ALL")

# 确保目标文件夹存在，如果不存在则创建
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# 剪切文件夹及其内容到目标文件夹
shutil.move(os.path.join(folder_path,"gt"), destination_folder)
shutil.move(os.path.join(folder_path,"T1"), destination_folder)
shutil.move(os.path.join(folder_path,"T2"), destination_folder)
shutil.move(os.path.join(folder_path,"list.txt"), destination_folder)


# 遍历文件夹中的所有文件
for filename in os.listdir(os.path.join(train_path,"T1")):
    # 构建新的文件名，删除第五位到第九位字符
    new_filename = filename[:4] + filename[9:]
    # 重命名文件
    os.rename(os.path.join(os.path.join(train_path,"T1"), filename), os.path.join(os.path.join(train_path,"T1"), new_filename))
for filename in os.listdir(os.path.join(train_path,"T2")):
    # 构建新的文件名，删除第五位到第九位字符
    new_filename = filename[:4] + filename[9:]
    # 重命名文件
    os.rename(os.path.join(os.path.join(train_path,"T2"), filename), os.path.join(os.path.join(train_path,"T2"), new_filename))
for filename in os.listdir(os.path.join(test_path,"T1")):
    # 构建新的文件名，删除第五位到第九位字符
    new_filename = filename[:4] + filename[9:]
    # 重命名文件
    os.rename(os.path.join(os.path.join(test_path,"T1"), filename), os.path.join(os.path.join(test_path,"T1"), new_filename))
for filename in os.listdir(os.path.join(test_path,"T2")):
    # 构建新的文件名，删除第五位到第九位字符
    new_filename = filename[:4] + filename[9:]
    # 重命名文件
    os.rename(os.path.join(os.path.join(test_path,"T2"), filename), os.path.join(os.path.join(test_path,"T2"), new_filename))