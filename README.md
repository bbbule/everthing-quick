# Everything-quick 搜索快捷方式生成器

一款基于 Python 和 Tkinter 开发的 Windows 小工具，用于快速生成 Everything 搜索脚本和自定义图标快捷方式。

## 功能特点

* 自定义 VBS 文件名
* 自定义 Everything 搜索条件
* 自动生成 VBS 搜索脚本
* 自动创建 Windows 快捷方式（LNK）
* 支持 ICO 图标
* 支持将 JPG、JPEG、PNG 图片转换为 ICO 图标
* 使用相对目录定位 Everything.exe，方便移动和管理
* 可创建各种文件库，如相册库，文档库，影视等，方便查找

## 环境要求

* Windows
* Python 3
* Everything
* Pillow
* pywin32

## 安装依赖

```bash
python -m pip install Pillow pywin32
```

## 使用方法

1. 运行 `everthing-quick`。
2. 输入快捷方式名称。
3. 输入 Everything 搜索语句。
4. 选择需要使用的图标。
5. 点击生成按钮。
6. 双击生成的快捷方式，即可执行对应的搜索。
7. 生成创建的ink快捷方式可直接移动到桌面或其他位置
8. 该程序需放置到Everthing安装目录中的子文件夹中

## 示例搜索语句

搜索大于 800 KB 的 JPG 图片：

```text
*.jpg size:>800kb
```

搜索大于 200 KB 的 mp4、avi、mov、flv、jpg、png、的所有文件

其中常用通配符含义，
“ * ”，代表任意长度的任意字符
“ | ”是逻辑运算符，通常代表 “或”。
更多通配符可咨询各种ai工具

```text
*.mp4| *.avi| *.mov| *.mkv| *.flv |*.jpg| *.png size:>200kb 
```
## 注意事项

为了更好的搜索体验，可在“everything”按照如下设置，方便更好查找文件

<img width="755" height="636" alt="PixPin_2026-03-04_20-01-27" src="https://github.com/user-attachments/assets/59691516-5445-407c-8db1-fce1ae3ee774" />




## 注意事项

请根据实际目录结构放置 Everything.exe 和生成的 VBS 文件。使用前请确认脚本中查找 Everything.exe 的相对路径符合你的目录结构。

## 许可证

许可证信息请参阅项目中的 LICENSE 文件。
