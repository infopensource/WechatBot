# WechatBot
    API文档
    https://zhuanlan.zhihu.com/p/114214846

## 声明
    本软件只用于技术交流，不用于商业以及其他用途，不针对任何第三方，谢谢

## 一、必备
    1、确认本机是否可以运行 python3 环境
    2、确认本机可以运行 sqlite3 数据库
    3、有一定的代码阅读、修改能力


## 二、项目介绍
    exchange.db  数据库文件
    msgDB.py     python操作数据库
    start.bat    系统批处理文件=》确保python脚本运行
    wxRobot.py   运行的python脚本
    demo.exe     可执行文件


## 三、使用说明
    确保安装对应版本的微信客户端，先启动 demo.exe ，然后启动 微信客户端 并登录 （新版本修改为一键启动），然后双击 start.bat 即可观察到对应的日志信息


## 四、开发简单说明
    现在默认的软件入口文件为 wxRobot.py 可以根据自己需要重写新建或者修改，但是建议引入 exchange.db 文件， exchange.db 文件用于接收、发送wechat的消息，也可以自己 根据这个文件创建其他数据库版本的消息处理文件，然后将对应的文件引入即可。msgDB.py 是该项目于数据库交互的连接，目前仅支持sqlite数据库，如果有需要可以自己新建其他数据库连接，或者后期版本更新其他版本数据库

## 五、现有功能
    目前只是文本消息可以收发，其他（如图片、文件、视频等）功能还在开发中

## 六、捐赠
![image](https://github.com/infopensource/WechatBot/blob/master/039ad7bed4bae4c80baf12d05259c2a.jpg)
![image](https://github.com/infopensource/WechatBot/blob/master/87ce20c06a594815a618ab4c501d58b.png)
