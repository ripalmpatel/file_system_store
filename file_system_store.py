# FileSystemStore keeps track of added files and generated hierarchical directory structure
import pprint

class FileSystemStore:
    def __init__(self, separator, root_dir_path):
        self.separator = separator
        self.root_dir = {
            "_type": "dir",
            "_path": root_dir_path
        }

    def add_file(self, path):
        cur_dir = self.root_dir
        cur_path = self.root_dir["_path"]
        segments = path.split(self.separator)
        seg_no = len(segments)
        if seg_no > 1:   # File with directory in path
            for i in range(0, seg_no-1):
                segment = segments[i]
                # Create Dir
                if segment != "":
                    cur_path = cur_path + segment + self.separator
                    if segment not in cur_dir.keys():
                        cur_dir[segment] = {
                            "_type": "dir",
                            "_path": cur_path                            
                        }
                    cur_dir = cur_dir[segment]
            # Create File in Dir
            cur_path = cur_path + segments[seg_no-1]
            cur_dir[segments[seg_no-1]] = {
                "_type": "file",
                "_path": cur_path
            }
        elif seg_no == 1: # File in root directory
            # Create File in Root
            if segments[0] != "":
                cur_dir[segments[0]] = {
                    "_type": "file",
                    "_path": cur_path + segments[0]
                }
        else:
            pass

    def add_files(self, paths):
        for path in paths:
            self.add_file(path)

    def get_hierarchy(self):
        return self.root_dir

# test example
fs = FileSystemStore("/", "/path/to/root_dir/")

fs.add_files([
    "dir1/dir2/xyz.xls",
    "dir1/dir1-file.xls", 
    "dir2/dir1/abc.csv",
    "dir-a/dir/file.jpeg",
    "dir-b/",
    "dir-x/dir-y/dir-z/abc.csv",
    "dir-x/dir-y/dir-z/xyz.csv",
])

pprint.pprint(fs.get_hierarchy())