##### python_work 一个简单的 Python 文件
- 在window 上安装Python https://www.python.org/downloads/ 官网地址
- 安装完成之后  右键 '在此打开命令窗口' 输入python(小写) 如果出现了 >>> (提示符)  代表安装成功
##### 安装 Sublime Text
- 推荐 Python 文件编译器 Sublime Text 
- 'Sublime Text' 是一款简单的文本编译器, 可以在现在任何操作系统中安装(Linux, window, mac) Sublime Text 几乎可以执行所有程序(脚本)
- 下载安装 Sublime Text http://www.sublimetext.com/download_thanks?target=win-x64
##### 配置Sublime Text 来执行Python 程序
- 如果在你的系统执行命令 Python 时 启动的就是 python3 就不需要做任何配置
- 如果需要执行 python3 来启动 Python 就需要配置 Sublime Text 使其使用正确的 Python 版本来运行编写的程序
- 安装完成 Sublime Text 之后 打开启动它 选择菜单 Tools > Build > System > New Build System, 新建一个配置文件, 删除该文件的全部内容
- 在输入以下内容进行 配置运行 python3 的Python 代码
``` 
 {
  "cmd" : ["python3", "-u", "$file"],
 }
 ``` 
 -  这段代码让 Sublime Text 使用python3 来运行 Python程序 将文件保存到 Sublime Text 默认打开的文件夹中  命名为 Python3.sublime-build
 
 ##### 运行python程序
 
 -  创建新的文件夹 启动 Sublime Text 选择菜单 File > Save As 将创建的文件保存到新的文件夹中 
 -  并以.py 结尾 告诉 Sublime Text 文件中的代码是使用 Python 编写的
