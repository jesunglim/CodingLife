import os
import shutil

input_path = "C:\\Users\\jesung\\Downloads\\img_align_celeba\\img_align_celeba\\"

output_path = "C:\\Users\\jesung\\Downloads\\sorted_celeba\\"


file_list = os.listdir(input_path)


count = 0
for file in file_list:
    count += 1 
    folder_name = output_path + str(count)

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        copy = input_path + str(file)
        paste = output_path + str(count)+ '\\' + str(count) + '.jpg'
        shutil.copyfile(copy, paste)
        print("Progress:%s / %s" %(count, len(file_list)))


print("Done!")        
