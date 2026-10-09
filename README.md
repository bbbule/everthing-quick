# Everything 搜索快捷方式生成器

一款基于 Python 和 Tkinter 开发的 Windows 小工具，用于快速生成 Everything 搜索脚本和自定义图标快捷方式。

## 功能特点

* 自定义 VBS 文件名
* 自定义 Everything 搜索条件
* 自动生成 VBS 搜索脚本
* 自动创建 Windows 快捷方式（LNK）
* 支持 ICO 图标
* 支持将 JPG、JPEG、PNG 图片转换为 ICO 图标
* 使用相对目录定位 Everything.exe，方便移动和管理

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

1. 运行 `1.py`。
2. 输入快捷方式名称。
3. 输入 Everything 搜索语句。
4. 选择需要使用的图标。
5. 点击生成按钮。
6. 双击生成的快捷方式，即可执行对应的搜索。

## 示例搜索语句

搜索大于 800 KB 的 JPG 图片：

```text
*.jpg size:>800kb
```

搜索大于 800 KB 的 PNG 图片：

```text
*.png size:>800kb
```

## 注意事项

请根据实际目录结构放置 Everything.exe 和生成的 VBS 文件。使用前请确认脚本中查找 Everything.exe 的相对路径符合你的目录结构。

## 许可证

许可证信息请参阅项目中的 LICENSE 文件。
