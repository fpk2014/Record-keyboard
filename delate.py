#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

#如果key是Back，删除前一个字母
path = os.getcwd()
key_path = os.path.join(path,'key.txt')

def back(file_name):
    """file_name是文件路径
        用法：back(路径)
    """
    file_open = open(file_name,'r')
    fobj=file_open.readlines()
    key = []
    for k in fobj:
        key.append(k.strip('\n'))
    result = []
    for i in key:
        num = len(result)
        if i == 'Back':
            try:
                del result[num-1]
            except:
                del i
        else:
            result.append(i)
            
    print result
    file_open.close()

if __name__ == "__main__":
    back(key_path)
