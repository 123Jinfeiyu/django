"""
ls: list directory contents 显示此目录下的内容

用法：ls [option].....[file]  q 退出 命令文档

-l : 长数据串列出，包含文件的属性与权限等数据；
-d : 仅列出目录本身，而不是列出目录里面的内容。
-a : all 全部文件，连同隐藏的文件一起列出来。


cd : change directory 变换工作目录
用法：cd 绝对路径或者相对路径

绝对路径：从根目录开始写的路径
相对路径：从参照开始写的路径

.  : 代表当前目录
.. : 父级目录

cd ~ : 快速切到家目录

cd .. : 快速切到父级目录


pwd: print working directory  显示当前目录

mkdir: make directory 创建目录

使用方法：mkdir 目录名称

-p: 递归创建目录

rmdir : remove directory 删除目录

-p: 递归删除目录

cp: copy 复制文件或者目录

使用方式：cp source(源文件) destination(目的地)

-r: 递归复制，用于目录复制

-i:  目标文件存在，在覆盖时会先询问



rm: remove 移除文件或者目录

-i: 在删除前会询问是否删除
-r: 递归删除，会把目录下的所有内容全部删除！这是一个非常危险的操作。
-f: force 强制 不会出现任何的警告信息


mv: move 移动文件与目录

-i: 当目标文件已经存在这个文件的时候，询问是否覆盖
-f: force 强制覆盖



















"""