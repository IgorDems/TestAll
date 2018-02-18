import os
import re

d = {}
# root = "/Users/igor/PycharmProjects/TestAll/Uni/"
root = "DIR"
keyword = ".html"
asd = "qwert"


# listOfFiles = os.listdir("/Users/igor/PycharmProjects/TestAll/Uni/DIR")
def files(root, keyword):
    level = 0
    for (dir, path, files) in os.walk(root):
        d[dir] = []
        count = 0
        level = level + 1*2


        for f in files:

            if f.endswith(keyword):
                count = count + 1
                path = os.path.join(dir, f)
                if os.path.exists(path):
                    d[dir] = count

                print("   " +level * "____" + "|File = ", os.path.basename(path))
        print("|__" +(level-1) * "_" + "/DIR = ", os.path.dirname(path))

    print("------------------------------------------------------------------")
    print(d)


files(root, keyword)

# def list_files(startpath):
#     for root, dirs, files in os.walk(startpath):
#         level = root.replace(startpath, '').count(os.sep)
#         indent = ' ' * 4 * (level)
#         print('{}{}/'.format(indent, os.path.basename(root)))
#         subindent = ' ' * 4 * (level + 1)
#         for f in files:
#             print('{}{}'.format(subindent, f))
#
#
# list_files("DIR")


# def get_directory_structure(rootdir):
#     """
#     Creates a nested dictionary that represents the folder structure of rootdir
#     """
#     dir = {}
#     rootdir = rootdir.rstrip(os.sep)
#     start = rootdir.rfind(os.sep) + 1
#     for path, dirs, files in os.walk(rootdir):
#         folders = path[start:].split(os.sep)
#         subdir = dict.fromkeys(files)
#         parent = reduce(dict.get, folders[:-1], dir)
#         parent[folders[-1]] = subdir
#     return dir
#
#
# get_directory_structure('DIR')

# def showFolderTree(path, show_files=False, indentation=2, file_output=False):
#     """
#     Shows the content of a folder in a tree structure.
#     path -(string)- path of the root folder we want to show.
#     show_files -(boolean)-  Whether or not we want to see files listed.
#                             Defaults to False.
#     indentation -(int)- Indentation we want to use, defaults to 2.
#     file_output -(string)-  Path (including the name) of the file where we want
#                             to save the tree.
#     """
#
#     tree = []
#
#     if not show_files:
#         for root, dirs, files in os.walk(path):
#             level = root.replace(path, '').count(os.sep)
#             indent = ' ' * indentation * (level)
#             tree.append('{}{}/'.format(indent, os.path.basename(root)))
#
#     if show_files:
#         for root, dirs, files in os.walk(path):
#             level = root.replace(path, '').count(os.sep)
#             indent = ' ' * indentation * (level)
#             tree.append('{}{}/'.format(indent, os.path.basename(root)))
#             for f in files:
#                 subindent = ' ' * indentation * (level + 1)
#                 tree.append('{}{}'.format(subindent, f))
#
#     if file_output:
#         output_file = open(file_output, 'w')
#         for line in tree:
#             output_file.write(line)
#             output_file.write('\n')
#     else:
#         # Default behaviour: print on screen.
#         for line in tree:
#             print(line)
#
#
# showFolderTree(path="/Users/igor/PycharmProjects/TestAll/Uni/DIR/", show_files=False, indentation=2, file_output=False)
