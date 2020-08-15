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

with open('introduction.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()
    if len(content) >= 1:
        m = re.search(r'我的姓名：(.+)', content[0])
        if m:
            grade += 25
            data['name'] = m.group(1)
        elif len(sys.argv) > 1 and sys.argv[1] == '0':
            exit(1)
    if len(content) >= 2:
        m = re.search(r'我的学号：(.+)', content[1])
        if m:
            grade += 25
            data['id'] = m.group(1)
        elif len(sys.argv) > 1 and sys.argv[1] == '1':
            exit(1)
    if len(content) >= 3:
        m = re.search(r'我的 Python 版本信息：(.+)', content[2])
        if m:
            grade += 25
            data['python'] = m.group(1)
        elif len(sys.argv) > 1 and sys.argv[1] == '2':
            exit(1)
    if len(content) >= 4:
        m = re.search(r'课程感言：(.+)', '\n'.join(content[3:]))
        if m:
            grade += 25
            data['feeling'] = m.group(1)
        elif len(sys.argv) > 1 and sys.argv[1] == '3':
            exit(1)

data['grade'] = grade
if os.isatty(1):
    print('得分：%d/100' % grade)
else:
    print(json.dumps(data))
