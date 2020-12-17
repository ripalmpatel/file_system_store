# FileSystemStore keeps track of added files and generated hierarchical directory structure
class FileSystemStore:
    def __init__(self, separator):
        self.separator = separator
        self.paths = []
        self.root_dir = {}

    def add_file(self, path):
        cur_dir = self.root_dir
        segments = path.split(self.separator)
        seg_no = len(segments)
        if seg_no > 1: 
            for i in range(0, seg_no-1):
                segment = segments[i]
                if segment != "":
                    if segment not in cur_dir.keys():
                        cur_dir[segment] = {}
                    cur_dir = cur_dir[segment]
        elif seg_no == 1:
            if segments[0] != "":
                cur_dir[segments[0]] = {}
        else:
            pass

    def add_files(self, paths):
        for path in paths:
            self.add_file(path)

    def get_hierarchy(self):
        #        
        #for path in self.paths:
        #    curDir = self.rootDir
        #    segments = path.split(self.separator)
        #    segNum = len(segments)
        #    if segNum > 1: 
        #        for i in range(0, segNum-1):
        #            segment = segments[i]
        #            if segment != "":
        #                if segment not in curDir.keys():
        #                    curDir[segment] = {}
        #                curDir = curDir[segment]
        #    elif segNum == 1:
        #        curDir[segments[0]] = {}
        #    else:
        #        pass        
        #
        return self.root_dir
        

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
