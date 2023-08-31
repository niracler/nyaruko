import os
import click

def list_python_files(folder_path):
    # 获取文件夹中所有文件的列表
    file_list = os.listdir(folder_path)

    # 迭代遍历文件列表
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)  # 获取文件的绝对路径

        # 判断文件是否是以 '.py' 结尾
        if file_path.endswith('.md') and os.path.isfile(file_path):
            print(file_name)  # 输出文件名

        # 判断文件是否是文件夹
        elif os.path.isdir(file_path):
            # 递归调用函数来遍历子文件夹
            list_python_files(file_path)

@click.command()
def cli():
    click.echo("Hello World!")
    folder_path = '/Users/niracler/iCloud云盘（归档）/Obsidian/Note/'
    list_python_files(folder_path)