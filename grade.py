#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys
import os
import json

if sys.version_info[0] != 3:
    print("Plz use python3")
    sys.exit()

grade = 0
data = dict()

with open('introduction.txt', 'r') as file:
    content = file.readlines()
    if len(content) > 1:
        m = re.search(r'我的姓名：(.+)', content[0])
        if m:
            grade += 25
            data['name'] = m.group(1)
    if len(content) > 2:
        m = re.search(r'我的学号：(.+)', content[1])
        if m:
            grade += 25
            data['id'] = m.group(1)
    if len(content) > 3:
        m = re.search(r'我的 Python 版本信息：(.+)', content[2])
        if m:
            grade += 25
            data['python'] = m.group(1)
    if len(content) > 5:
        m = re.search(r'课程感言：(.+)', '\n'.join(content[4:]))
        if m:
            grade += 25
            data['feeling'] = m.group(1)

data['grade'] = grade
if os.isatty(1):
    print('得分：%d/100' % grade)
else:
    print(json.dumps(data))
