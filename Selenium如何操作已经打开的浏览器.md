# Selenium如何操作已经打开的浏览器

[冲啊咸鱼 ](https://juejin.cn/user/1077939864886456/posts)

2022-03-10

正常情况下，这种适合加入手工+自动化结合操作，更多的是把selenium当成一个工具，便于测试工作。

## 场景：

![image.png](https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/078d6e951d3c49d1af8d10da1917582f~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp)

因为公司是支付业务，所有密码这一块，就有一个插件，不能进行复制粘贴，selenium的input也不能进行输入，这个适合我们就可以写一个登录测试用例，不写输入密码与登录按钮，手动输入。

登录之后呢，就是我们的用户界面，这个时候浏览器就相当于有了我们的用户信息了，我们可以直接使用selenium的get方法，去打开系统的其他页面。

## 接管chrome

通过命令

```
chrome [--headless] --remote-debugging-port=9222 --user-data-dir="目标路径"
# -remote-debugging-port值，可以指定任何打开的端口
# -user-data-dir标记，指定创建新Chrome配置文件的目录。它是为了确保在单独的配置文件中启动chrome，不会污染你的默认配置文件
# --headless无头模式
```

在cmd命令中打开一个端口9222的谷歌浏览器

```
cd /Applications/Google\ Chrome.app/Contents/MacOS/
./Google\ Chrome --remote-debugging-port=9222
```

```
./Google\ Chrome --remote-debugging-port=9222
```



***值得注意的是，需要在cmd打开浏览器，否则pycharm中直接运行代码会显示链接不到目标端口***

步骤如下：

1. 找到谷歌浏览器的安装位置，找到chrome.exe的位置

```
./chrome.exe [--headless] --remote-debugging-port=9222 --user-data-dir="目标路径"
```

这里的目标路径随意，主要用于存放打开浏览器的配置缓存的 2. 也可以使用win+r 输入cmd 输入，该方法需要将chrome加入环境便利path，

```
chrome.exe [--headless] --remote-debugging-port=9222 --user-data-dir="目标路径"
```

1. 代码部分需要设置

```
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9988")
driver = webdriver.Chrome(options=options)
```

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e82a6f0b9dc411da466b180c3665c70~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp)

### 代码部分

这里只写了chrome的，其他浏览器不知道，后面可以放进配置文件config去配置浏览器是否需要打开指定浏览器。这个可以参考前面的框架，将该代码放进浏览器的初始化部分。

值得注意的是，需要将浏览器最小化，否则不能输入，直接切换程序，能定位元素，但是不能对浏览器进行操作

![image.png](https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81175359484943a3a81058f32597d665~tplv-k3u1fbpfcp-jj-mark:3024:0:0:0:q75.awebp)

```
# -*- coding: utf-8 -*-
"""
初始化浏览器
"""
from selenium import webdriver


from libs.utils.yaml_util import read_yaml


def browser_init():
    web_config_data = read_yaml(r'\config\config.yaml')['browser']
    
    options = webdriver.ChromeOptions()

    # cmd打开指定端口浏览器
    # 操作同一浏览器，如果不需要，则把下面注释
    # options.add_experimental_option("debuggerAddress", "127.0.0.1:9988")
    driver = webdriver.Chrome(options=options)
    
    # 浏览器最大化
    try:
        driver.maximize_window()
    except:
        pass
    

    return driver

if __name__ == '__main__':
    global driver
    driver = browser_init()

    # chrome_driver = chromedriver.exe的地址  # 如果将chrome驱动放到Python目录，这句可以不要
    # 设置浏览器
    # cmd 输入 chrome.exe在文件中的位置或者将chrome添加到path 中   chrome.exe地址 [--headless] --remote-debugging-port=9222 --user-data-dir="目标路径"

    # -remote-debugging-port值，可以指定任何打开的端口
    # -user-data-dir标记，指定创建新Chrome配置文件的目录。它是为了确保在单独的配置文件中启动chrome，不会污染你的默认配置文件
    # --headless无头模式
```