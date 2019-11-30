'''
作者:lg
日期:2019/11/3
文件描述:
缺陷：
'''

import sys
import os

StartName = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, StartName)

from core import Main

if __name__ == '__main__':
    Main.main()
