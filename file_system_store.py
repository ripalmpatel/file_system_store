# FileSystemStore keeps track of added files and generated hierarchical directory structure

class FileSystemStore:
    def __init__(self, separator):
        self.separator = separator
        self.root_dir = {}

    def add_file(self, path):
        cur_dir = self.root_dir
        segments = path.split(self.separator)
        seg_no = len(segments)
        if seg_no > 1: # File with directory in path
            for i in range(0, seg_no-1):
                segment = segments[i]
                if segment != "":
                    if segment not in cur_dir.keys():
                        cur_dir[segment] = {}
                    cur_dir = cur_dir[segment]
            cur_dir[segments[seg_no-1]] = {}
        elif seg_no == 1: # File in root directory
            if segments[0] != "":
                cur_dir[segments[0]] = {}
        else:
            pass

    def add_files(self, paths):
        for path in paths:
            self.add_file(path)

    def get_hierarchy(self):
        return self.root_dir

# test 
fs = FileSystemStore('/')

fs.add_files([
    'dir1/dir2/xyz.xls', 
    'dir2/dir1/abc.csv',
    'dir-a/dir/file.jpeg',
    'dir-b/',
    'dir-x/dir-y/dir-z/abc.csv',
])

print(fs.get_hierarchy())
#   {
#       'dir1': {
#           'dir2': {
#               'xyz.xls': {}
#           }
#       }, 
#       'dir2': {
#           'dir1': {
#               'abc.csv': {}
#           }
#       }, 
#       'dir-a': {
#           'dir': {
#               'file.jpeg': {}
#           }
#       }, 
#       'dir-b': {}, 
#       'dir-x': {
#           'dir-y': {
#               'dir-z': {
#                   'abc.csv': {}
#               }
#           }
#       }
#  }
