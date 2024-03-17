"""
/:  文件系统根

bin: binary 存储了一些基本的系统命令和可执行文件。

boot: 启动 包含了与系统引导和内核相关的文件，这个文件夹非常重要，如果删除了系统将无法启动

cdrom: 用来做光盘的挂载点

dev: device(设备) 包含设备文件(在Linux操作系统上面一切皆文件)

etc: 配置文件目录

home:这是是用户主目录的基础目录，每一个用户都会在这个目录下面有一个子目录

lib： 用于存储共享库，共享库是一组程序代码和数据。

lib64:专门用来存储64位系统特有的库文件。

lost+found:通常都是空目录，当系统非法关机之后，这里会存放一些日志文件

media:通常用于挂载可移动设备，例如像USB驱动器，当系统自动识别之后，自动挂载到该目录下。

mnt:通常用于手动挂载设备。

opt:用于存放可选软件包或者应用程序。

proc:process该目录提供了一个动态的、实时更新的接口，使用户和系统工具能够访问有关运行中进程、内核状态和硬件的信息。

root: 超级管理员的家目录

run:通常用于存储运行时数据和临时文件

sbin:super binary 用于存储超级管理员使用的命令

tmp:临时  用于存储临时文件

usr:用户的很多应用程序和文件都放在这个目录下

var:通常用于存放不断扩展的东西，比如日志文件





"""