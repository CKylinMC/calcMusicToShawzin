# calcMusicToShawzin

一个简单的用于将计算器音乐的谱子转换为warframe三线琴的python3脚本。

## 用法

### 使用命令行调用

```batch
python calcMusicToShawzin [options]
```

**Options**

* `-h, --help` 显示帮助信息
* `-f FILE, --file=FILE` 设置用于输入的文件。使用此选项可以直接将存储计算器音乐曲谱的txt文本。
  * 不设置此选项，则默认从命令行接收输入。
  * 命令行输入暂时只支持单行输入。
* `-o OUTPUT, --output=OUTPUT` 设置用于输出的文件。使用此选项可以讲结果重定向到文件。
  * 不设置此选项，则会显示到命令行界面。
* `-s SPACE, --space=SPACE` 设置默认音符间隔。你可以将这个选项理解为调整播放速度的选项。
  * 默认值为3。
  * 此值与格数有关。

### 作为模块调用

```python
from calcMusicToShawzin import calcMusicToShawzin
CMS = calcMusicToShawzin(space=3)
CMS.convert('123456789+-*/=') # 直接转换，或
CMS.convertFromFile('path/to/your/file.txt') # 从文件获取
print(CMS.getShawzinScores())
```

## 支持引入的符号列表

|  计算器音符   | Warframe音符 |
| :--: | :----------: |
|  1   |      B       |
|  2   |      C       |
|  3   |      E       |
|  4   |      J       |
|  5   |      K       |
|  6   |      M       |
|  7   |      R       |
|  8   |      S       |
|  9   |      U       |
|  +   |      h       |
|  -   |      i       |
|  *   |      k       |
|  /   |      B       |
|  =   |      C       |
|  [   | (开启强制短间隔模式) |
|  ]   | (关闭强制短间隔模式) |

### 短间隔模式

短间隔模式是为了方便一些谱子有快节奏的音符而设计，短间隔模式开启标记到短间隔模式关闭标记中间的每一个音符的间隔强制设置为1且无视间隔设置。可以通过空格来调节短间隔模式中音符的间隔。

* **已知问题**
  * 在短间隔标记前后同时存在空格时可能出现问题，导致输出的三线琴乐谱不被识别。

## 示范

#### BadApple

* badapple.txt:

```
23456 986 2 654323456 5432343213
23456 986 2 654323456 543 4 5 6
23456 986 2 654323456 5432343213
23456 986 2 654323456 543 4 5 6
89656 5689656 5654312 1234562
5689656 5689656 5654312 1234562
5689656 5689656 5654312 1234562
5689656 5689656 9+-+986 5654312
```

```
python calcMusicToShawzin.py -f badapple.txt -o badapple_converted.txt
```

* badapple_converted.txt:

```
5CABEAEJAHKAKMANUATSAWMAZCAfMAlKAoJArEAuCAxEA0JA3KA6MA9KBDJBGEBJCBMEBPJBSEBVCBYBBbEBeCBkEBnJBqKBtMBwUB2SB5MB8CCCMCIKCLJCOECRCCUECXJCaKCdMCgKCmJCpECsJCyKC4MC+CDEEDHJDKKDNMDQUDWSDZMDcCDiMDoKDrJDuEDxCD0ED3JD6KD9MEAKEGJEJEEMCEPEESJEVEEYCEbBEeEEhCEnEEqJEtKEwMEzUE5SE8ME/CFFMFLKFOJFREFUCFXEFaJFdKFgMFjKFpJFsEFvJF1KF7MGBSGHUGKMGNKGQMGTKGZMGcSGfUGiMGlKGoMGrKGxMG0KG3JG6EG9BHACHDBHJCHMEHPJHSKHVMHYCHbKHhMHkSHnUHqMHtKHwMHzKH5MH8SH/UICMIFKIIMILKIRMIUKIXJIaEIdBIgCIjBIpCIsEIvJIyKI1MI4CI7KJBMJESJHUJKMJNKJQMJTKJZMJcSJfUJiMJlKJoMJrKJxMJ0KJ3JJ6EJ9BKACKDBKJCKMEKPJKSKKVMKYCKbKKhMKkSKnUKqMKtKKwMKzKK5MK8SK/ULCMLFKLIMLLULRhLUiLXhLaULdSLgMLjKLpMLsKLvJLyEL1BL4CL7
```

# 参考

* [WF-Shawzin-music-maker](https://github.com/RainMeoCat/WF-Shawzin-music-maker)
* [三线琴，代码规律详解【warframe吧】- 百度贴吧](https://tieba.baidu.com/p/6242257023?red_tag=2810181628)

