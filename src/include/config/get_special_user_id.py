# -*- coding: utf-8 -*-
"""
@Time    : 2024/10/29 下午4:41
@Author  : Gie
@File    : 11.py
@Desc    :
"""
import copy
import sys
import json
from pathlib import Path
from pymongo import MongoClient

uri = 'mongodb://xinyu_read:7inv8hwDly5yeAlE@dds-uf61cedad15179242978-pub.mongodb.rds.aliyuncs.com:3717,dds-uf61cedad15179241223-pub.mongodb.rds.aliyuncs.com:3717/admin?replicaSet=mgset-81098053'
conn = MongoClient(uri)


def get_special_user_ids():
    pass
    # docs = conn.xinyu_back.user.find(filter={}, projection=['_id'])
    # my_user_info = list()
    # for doc in docs:
    #     doc = conn.xinyu_back.user.find_one({'_id': doc['_id']})
    #     my_user_info.append(copy.deepcopy(doc))
    # # 写入文件
    # with open('special_user_ids.json', 'w', encoding='utf-8') as f:
    #     json.dump(my_user_info, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    print("finished")
