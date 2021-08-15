# [Linux中记录终端输出到文本文件](https://www.cnblogs.com/jdksummer/articles/2532259.html)

原文地址：http://www.eetop.cn/blog/html/03/6503-25123.html

一，把命令运行的结果保存到文件当中：用 > 把输出转向就可以了
　　例子:
　　$ ls > ls.txt   ＃或者 ls-->ls.txt   ＃把ls命令的运行结果保存到文件ls.txt中
　　
　　说明: > 是把输出转向到指定的文件，如文件已存在的话也会重新写入，文件原内容不会保留
　　   >> 是把输出附向到文件的后面，文件原内容会保留下来

二，在输出信息的同时把信息记录到文件中： tee 命令　　
　　解释一下tee的作用:
 　“read from standard input and write to standard output and files”，它从标准输入读取内容并将其写到标准输出和文件中

​    参数： -a, --append，“append to the given FILEs, do not overwrite“，附加至给出的文件，而不是覆盖它

　　例子:
　　$ ls | tee ls.txt  ＃将会在终端上显示ls命令的执行结果，并把执行结果输出到ls.txt 文件中  
　　$ls | tee -a ls.txt  #保留ls.txt文件中原来的内容，并把ls命令的执行结果添加到ls.txt文件的后面。

三，多个命令的输出都需要记录： script 命令
　　script这个命令很强大，可以记录终端的所有输出到相应的文件中
　　例子:
　　1.$ script
　　Script. started, file is typescript
　　2.$ ls
　　…… 内容省略
　　3.$ exit
　　exit
　　Script. done, file is typescript
　　4. $cat typescript  ＃就会把上面绿色的部分再显示一次：　　

　　说明:
　　1,我们在启动script时没有指定文件名，它会自动记录到当前目录下一个名为 typescript的文件中。也可以用 -a参数 指定文件名
　　例子:
　　$script. -a example.txt ＃终端的输出内容被记录到 example.txt这个文件中
　　2,退出script时，用exit，事实上script就是启动了一个shell

　**四，用script录制并播放session的内容**
　　我们可以用 script把整个终端会话的所有操作和输出录制下来，然后再用scriptreplay进行播放。
　　如果录制时记录下来了操作时的时间数据，那么播放时和操作时的使用时间完全相同。
　　这个很有用吧，比如：我们可以把安装软件时编译的过程记录下来，然后给别人进行演示
　　看例子:
　　[lhd@hongdi ~]$ 

```
script -t 2>example.time -a example.txt
```

　　Script. started, file is example.txt
　　[lhd@hongdi ~]$ ls
　　说明: -t 2>example.time -t是把时间数据输出到标准错误(standard error)，所以我们使用 2>example.time 把数据转向到 example.time这个文件当中
　　如何播放所记录的内容?
　　第一步：安装scriptreplay
　　下载
　　wget linux/utils/util-linux/util-linux-2.12r.tar.bz2">ftp://ftp.kernel.org/pub/linux/utils/util-linux/util-linux-2.12r.tar.bz2
　　解压
　　tar -jxvf util-linux-2.12r.tar.bz2
　　之后复制文件到系统的命令目录中即可
　　[root@hongdi 下载]# cp util-linux-2.12r/misc-utils/scriptreplay.pl /usr/bin/scriptreplay
　　[root@hongdi 下载]# chmod 755 /usr/bin/scriptreplay
　　备注: fedora 10的util-linux-ng-2.14.1-3.2.fc10.i386.rpm 此包中已包含 scriptreplay,已无需另行安装
　　第二步：播放所录制的session内容
　　[lhd@hongdi ~]$ scriptreplay example1.time example1.txt
　　[lhd@hongdi ~]$ ls
　　1.gtkrc-2.0 c.tar jeffray_lee@hotm[AI](http://bbs.eetop.cn/forum-318-1.html)l.com pass
　　[lhd@hongdi ~]$ abcd
　　bash: abcd: command not found

　　[lhd@hongdi ~]$ exit