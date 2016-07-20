### TransME
基于pyqt的划词翻译工具,开启后，鼠标选中单词进行翻译，自动忽略选中的标点符号，程序运行在系统托盘，消耗资源极低。可以自己编写python脚本选择翻译的词典，默认使用有道。
<table><tr>
<td><img src="http://7xl4a3.com1.z0.glb.clouddn.com/transme-1.png" width="465" height="425" alt="TransMe" border=0></td>
<td><img src="http://7xl4a3.com1.z0.glb.clouddn.com/transme-2.png" width="426" height="425" alt="trayIcon" border=0></td>
</tr></table>
    
### Motivation
goldendict太慢(丑)，而且CPU经常占用20%。

### Requirement
- python 2.7
- pyqt 4.8+

### Usage
python transMe.py &
或者把他写到alias里

### Disadvantages
1. 不能响应全局按键，所以开关划词需要手动操作
2. 使用中文输入法时不能开启划词
3. 有道API比较慢，有时候会卡
