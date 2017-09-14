#! /usr/bin/python3

import cards_tools
# 这是名片管理系统的主程序
# 程序的入口
# 每一次启动名片管理系统都通过main这个文件启动

# 无限循环，由用户决定什么时候退出循环
while True:
    # 显示系统菜单
    cards_tools.show_menu()

    action = int(input("请选择操作的功能："))

    # 根据用户输入决定后续的操作
    if action in [1,2,3]:
        # 1.新增名片
        if action == 1:
            cards_tools.new_card()
        # 2.显示全部
        if action == 2:
            cards_tools.show_all()
        # 3.查询名片
        if action == 3:
            cards_tools.search_card()

    # 3>用户输入0,退出循环
    elif action == 0:
        print("欢迎再次使用名片管理系统")
        break
    # 4>用户输入其他，返回错误信息
    else:
        print("您输出入的不正确，请重新选择")