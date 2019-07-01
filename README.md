# tpl_self-introduction
Template for the self introduction homework

请填写 introduction.txt.

你可以在本地运行 `python3 grade.py` 来进行一次本地的评分，以验证你代码的正确性。请不要修改它的内容。得分仅供参考，实际评分使用的数据和方法可能不同。

# 如何完成这个作业

## 第一步：配置 GitHub 的 SSH Key

1. 进入 Linux 环境
2. 运行 `ssh-keygen`，生成一个 SSH Key，一路按照默认回车即可
3. 打开 GitHub，登录自己的帐号
4. 点击右上角的头像，在下拉菜单中选择 Settings
5. 在左边的列表中选择 SSH and GPG keys
6. 点击 SSH Keys 右边的 New SSH Key 绿色按钮
7. 回到 Linux ，紧接着刚才运行的 `ssh-keygen` ，运行 `cat ~/.ssh/id_rsa.pub`
8. 把输出的内容（应该是 ssh-rsa 开头）复制并粘贴到浏览器里 Key 下面的文本框，
9. 点击 Add SSH Key 按钮完成 SSH Key 的配置
10. 回到 Linux ，输入 `ssh -T git@github.com`
11. 如果出现了一个 yes/no 的提示，输入 yes 然后回车
12. 此时如果配置好了，应该会看到一个输出：`Hi xxx! You've successfully authenticated, but GitHub does not provide shell access.`
13. 这代表你完成了这一步。

## 第二步：克隆仓库

## 第三步：获取 Python3 版本信息

## 第四步：编辑 introduction.txt

## 第五步：完成 Git 提交