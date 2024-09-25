import os
from filesplit.merge import Merge


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LAMA_MODEL_PATH = os.path.join(BASE_DIR, 'models', 'big-lama')

# 查看该路径下是否有模型完整文件，没有的话合并小文件生成完整文件
if 'big-lama.pt' not in (os.listdir(LAMA_MODEL_PATH)):
    merge = Merge(LAMA_MODEL_PATH, LAMA_MODEL_PATH, "big-lama.pt")
    merge.manfilename = 'fs_manifest.csv'
    merge.merge()
