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
12. 此时如果配置好了，应该会看到一个输出：`Hi xxx! You've successfully authenticated, but GitHub does not provide shell access.` 这代表你完成了这一步。

## 第二步：克隆仓库

1. 在网络学堂点击 GitHub Classroom 的作业链接之后，你应该会看到新建的一个仓库，叫做 `self-intro-你的GitHub用户名` 。你可以通过 `https://github.com/physics-data/self-intro-你的GitHub用户名`来访问它。点击右侧的绿色按钮 Clone or Download，下面应该会显示 Clone with SSH 和一个文本框，点击右边的按钮进行复制，得到的应该是形如 `git@github.com:physics-data/self-intro-你的GitHub用户名.git`的内容。如果显示的是 https 开头的内容，请点击蓝色的 Use SSH 再进行以上步骤。
2. 回到 Linux，输入 `git clone 刚才复制的内容`（在 WSL 中，可以右键点击窗口标题，选择编辑-粘贴），这时候应该能看到形如 `git clone git@github.com:physics-data/self-intro-你的GitHub用户名.git` 的内容，回车以执行。
3. 这时候，你可以输入 `ls` 来列出当前目录的内容，应该可以看到一个新的目录，名字为 `self-intro-你的GitHub用户名`。你可以输入 `cd self-intro-你的GitHub用户名`来进入这个目录。
4. 再次输入 `ls` ，应该可以看到几个文件：`README.md` `introduction.txt` 和 `grade.py` 。这就是这个仓库里的文件了。你马上需要更改的就是 `introduction.txt` 的内容。

## 第三步：获取 Python3 版本信息

0. **此步由于课程进度原因，可以忽略，如果你的环境中有python，可以将信息填入introduction.txt中，不填入该项依然可以得分（introduction中有dummy的版本号）**
1. 接下来，需要验证你的 Linux 环境下确实有一个正常运行的 Python 3  。首先输入 `python3`，你这个时候应该可以看到它一些输出。
2. 记下 `Python 3.x.x` ，你也可以复制下来，留到下一步使用。
3. 输入 `quit()` 回车以退出 Python 3 。

## 第四步：编辑 introduction.txt

1. 已经知道 Python3 版本后，我们接着进行 `introduction.txt` 的编辑。这里提供两种编辑器的使用方法：
   1. nano：输入 `nano introduction.txt` ，这个时候会显示文件内容，下面是一些快捷键的显示，`^` 表示 Ctrl 键，即 `^O Write Out` 表示按下 Ctrl-O 对应的是 Write Out 也就是写出文件，`^X Exit` 表示按下 Ctrl-X 对应的就是退出。编辑文本直接采用上下左右即可，退出前如果没有保存，它会提示你保存当前文件的路径，直接回车即可。
   2. vim：输入 `vim introduction.txt` ，这个时候会显示文件的内容，但还不能立即更改文件的内容，注意不要随便按下键盘。这个时候，按下 `i` 键，左下角会显示 `--INSERT--` 的字样，这个时候就可以正常使用上下左右编辑文本。编辑结束后，可以按下 `ESC` 键，此时左下角的 `--INSERT--` 消失，此时输入 `:wq!` 回车即可保存文件并且推出 vim。
2. 这个时候，输入 `git diff` 回车，应该可以看到你刚才进行的更改。删去的行和添加的行会有不同的颜色和符号进行区分。你可以多次修改直到符合要求为止。
3. 你可以在本地运行 `python3 grade.py` 来进行一次模拟的评分。注意，这个评分对格式要求比较严格，仅供参考，实际评分的时候要求可能会有细微的变化。

## 第五步：完成 Git 提交

1. 输入 `git status` 回车，可以看到 `modified` 字样，表示你在本地进行了修更改。输入 `git add . ` 表示把当前目录下所有更改移到暂存区，此时如果再次输入 `git status` 回车会看到稍微不同的输出。
2. 输入 `git commit` 回车，表示把当前的修改形成一个完整的提交。在一些环境下，它会提示你设置 EMail 和名字，按照要求输入 `git config --global user.name "Blah Blah"` 和 `git config --global user.email "john@apple.com"` ，然后再次输入 `git commit` 回车。这个时候，你会进入到编辑界面，可能是 nano 也可能是 vim ，类似上面的方法，在第一行输入一些内容，这就是这个提交的信息。
3. 退出编辑器后，新的提交就完成了，`git status` 会显示当前没有新的更改。
4. 输入 `git push` ，等待命令完成后，回到 GitHub 上之前打开的仓库页面，刷新就可以看到你刚刚编写的新的 commit 。
5. 在你的commit附近，你可以看到一个小红叉或者一个小绿勾，这是提交上来的评测情况，你可以点开Actions相关页面，查看自己作业的评分情况，这次评分一共有四个评分点，分别对应 introduction.txt 的四行。这个评测只用于自测，不用于最终评分。以后的作业中可能会有自动评测部分，也可能没有。
6. 接下来你就可以自由地探索上面用到的这些工具了。

# 评分

最终分数构成为：

* 黑盒 80 分：助教clone repo并运行grade.py，并将最终得到的100分折算为80分。
* 白盒 20 分：Git 使用 20 分，主要参照提交记录（commit message），实际提交及其关系。

助教以 deadline 前 GitHub 上最后一次提交为准进行评测。
