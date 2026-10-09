import tkinter as tk
from tkinter import filedialog, messagebox
import os
import winshell
from win32com.client import Dispatch
from PIL import Image

def generate_vbs():
    file_name = file_entry.get().strip()
    search_query = search_entry.get().strip()
    icon_path = icon_entry.get().strip()

    if not file_name:
        messagebox.showerror("错误", "文件名不能为空！")
        return

    if not search_query:
        messagebox.showerror("错误", "搜索内容不能为空！")
        return

    # 确保文件名合法，去掉特殊字符
    invalid_chars = r'\/:*?"<>|'
    for char in invalid_chars:
        file_name = file_name.replace(char, "_")

    # 生成 VBS 文件名
    vbs_file_name = file_name + ".vbs"

    # 生成 VBS 文件内容
    vbs_content = f'''Set objShell = CreateObject("WScript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")

' 获取当前 VBS 文件所在目录
currentDir = objFSO.GetParentFolderName(WScript.ScriptFullName)

' 获取上一级目录
parentDir = objFSO.GetParentFolderName(currentDir)

' 构造 Everything.exe 在上一级目录的完整路径
everythingPath = """" & parentDir & "\\Everything.exe" & """"

' 检查 Everything.exe 是否存在
If objFSO.FileExists(parentDir & "\\Everything.exe") Then
    ' 运行 Everything 并执行搜索
    objShell.Run everythingPath & " -search ""{search_query}""", 1, False
Else
    MsgBox "Everything.exe 未找到，请检查文件路径！", 16, "错误"
End If

Set objShell = Nothing
Set objFSO = Nothing
'''

    # 保存 VBS 文件
    with open(vbs_file_name, "w", encoding="utf-8") as vbs_file:
        vbs_file.write(vbs_content)

    # 处理图标转换
    if icon_path:
        if icon_path.lower().endswith((".jpg", ".jpeg", ".png")):
            icon_path = convert_to_ico(icon_path, file_name)

    # 创建快捷方式
    shortcut_path = os.path.join(os.getcwd(), file_name + ".lnk")
    shell = Dispatch("WScript.Shell")
    shortcut = shell.CreateShortcut(shortcut_path)
    shortcut.TargetPath = os.path.abspath(vbs_file_name)
    shortcut.WorkingDirectory = os.getcwd()
    
    # 设置快捷方式图标
    if icon_path and os.path.exists(icon_path):
        shortcut.IconLocation = icon_path
    else:
        # 默认使用 Everything.exe 作为图标
        everything_exe = os.path.join(os.path.dirname(os.getcwd()), "Everything.exe")
        if os.path.exists(everything_exe):
            shortcut.IconLocation = everything_exe
    
    shortcut.Save()

    messagebox.showinfo("成功", f"VBS 文件和快捷方式已生成！\n\nVBS 文件：{vbs_file_name}\n快捷方式：{shortcut_path}")

def convert_to_ico(image_path, file_name):
    try:
        img = Image.open(image_path)
        ico_path = os.path.join(os.getcwd(), file_name + ".ico")
        img.save(ico_path, format="ICO", sizes=[(256, 256)])
        return ico_path
    except Exception as e:
        messagebox.showerror("图标转换失败", f"无法将 {image_path} 转换为 ICO 格式。\n错误信息：{e}")
        return None

def choose_icon():
    icon_path = filedialog.askopenfilename(filetypes=[("图片文件", "*.ico;*.jpg;*.jpeg;*.png"), ("所有文件", "*.*")])
    if icon_path:
        icon_entry.delete(0, tk.END)
        icon_entry.insert(0, icon_path)

# 创建主窗口
root = tk.Tk()
root.title("VBS 生成器")
root.geometry("450x320")

# 文件名输入
tk.Label(root, text="请输入 VBS 文件名：", font=("Arial", 12)).pack(pady=5)
file_entry = tk.Entry(root, width=50)
file_entry.pack(pady=5)

# 搜索内容输入
tk.Label(root, text="请输入 Everything 搜索内容：", font=("Arial", 12)).pack(pady=5)
search_entry = tk.Entry(root, width=50)
search_entry.pack(pady=5)

# 选择图标
tk.Label(root, text="选择图标文件（.ico, .jpg, .png）：", font=("Arial", 12)).pack(pady=5)
icon_entry = tk.Entry(root, width=40)
icon_entry.pack(pady=5)
tk.Button(root, text="浏览", command=choose_icon, font=("Arial", 10)).pack(pady=2)

# 生成按钮
tk.Button(root, text="生成 VBS & 快捷方式", command=generate_vbs, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=10)

# 运行窗口
root.mainloop()
