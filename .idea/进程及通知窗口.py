import win32api  # win32api函数模块

import win32con  # 常量

import win32gui  # win32界面模块

import win32process  # win32进程模块  以上模块请先安装pywin32

import ctypes  # C C++语言调用 dll

while True:
    # 窗口句柄的获取：用循环的方式判断是否有进程后取得句柄(None：类名未知)
    if win32gui.FindWindow(None, "扫雷") != 0:
        window_handle = win32gui.FindWindow(None, "扫雷")
        break

# 进程ID的获取：根据窗口句柄获取进程ID
process_id = win32process.GetWindowThreadProcessId(window_handle)[1]

# 弹窗message_box提示取得的窗口句柄和进程ID
win32api.MessageBox(win32con.NULL, '窗口句柄：'+ str(window_handle)+'\n' + '窗口进程ID：' + str(process_id), 'Hello', win32con.MB_OKCANCEL)

# 打开进程：遍历进程打开process_id(False：子进程不能继承父进程句柄)
process_handle = win32api.OpenProcess(0x1F0FFF, False, process_id)
print(process_handle)
# 打开进程后才能读内存，需要载入win32内核
kernel32 = ctypes.windll.LoadLibrary(r"C:\Windows\system32\kernel32")
# 读
data1 = ctypes.c_long()
kernel32.ReadProcessMemory(int(process_handle), 0x00000000, ctypes.byref(data1), 4, None)
print(data1, value)
