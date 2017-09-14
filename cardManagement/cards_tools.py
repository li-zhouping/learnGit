# 记录所有名片的列表
card_list = []

def show_menu():
    """显示系统菜单"""
    print("*" * 50)
    print("欢迎使用名片管理系统V1.0")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("0.退出系统")
    print("*" * 50)

def new_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片")

    # 1.提示用户输入名片的详细信息
    name_str = input("请输入用户的名字：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入QQ：")
    email_str = input("请输入Email：")

    # 2.使用用户输入的信息建立一个名片字典
    card_dict = {"name":name_str,
                 "phone":phone_str,
                 "qq":qq_str,
                 "email":email_str}
    # 3.将名片字典增加到列表中
    card_list.append(card_dict)
    # 4.提示用户增添成功
    print("添加%s的名片成功！" % name_str)

def show_all():
    """显示全部"""
    # 判断是否有名片记录，如果没有，提示用户新增
    if  len(card_list) == 0:
        print("当前没有名片记录，请增加名片")
        return #return以后，下方代码不再执行，回到调用函数的位置

    print("-" * 50)
    print("显示所有名片")
    #打印表头
    for name in ["姓名","电话","QQ","邮箱"]:
        print(name, end="\t\t")
    print("") #换行
    print("=" * 50)
    #遍历名片列表依次输出字典信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))

def search_card():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")

    # 1.提示用户输入要搜索的姓名
    find_name = input("请输入要搜索的姓名：")
    # 2.查询
    show_card(find_name)

def show_card(name):
    """
    显示查找的名片
    :param name:要查找的名字
    :return:
    """
    for card_dict in card_list:
        if card_dict["name"] == name:
            for title in ["姓名", "电话", "QQ", "邮箱"]:
                print(title, end="\t\t")
            print("")  # 换行
            print("=" * 50)
            # 遍历名片列表依次输出字典信息
            for card_dict in card_list:
                print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["name"],
                                                    card_dict["phone"],
                                                    card_dict["qq"],
                                                    card_dict["email"]))
            # 针对找到名片记录执行修改/删除的操作
            deal_card(card_dict)
            break
            # 如果没有找到，需要提示用户
        print("抱歉，没有找到%s的名片" % name)
    else:
        pass

def deal_card(find_dict):
    action = int(input("请选择要执行的操作："
                       "[1]修改 [2]删除 [0]返回上级菜单"))
    #修改名片
    if action == 1:
        find_dict["name"] = edit_card_info(find_dict["name"],
                                           "要修改的姓名(回车不修改)")
        find_dict["phone"] = edit_card_info(find_dict["phone"],
                                           "要修改的电话(回车不修改)")
        find_dict["qq"] = edit_card_info(find_dict["qq"],
                                           "要修改的qq(回车不修改)")
        find_dict["email"] = edit_card_info(find_dict["email"],
                                           "要修改的email(回车不修改)")
        print("修改成功!")
        show_card(find_dict["name"])

    #删除名片
    elif action == 2:
        card_list.remove(find_dict)
        print("%s的名片已删除" % find_dict["name"])

def edit_card_info(dict_value, tip_message):
    """
    修改名片信息
    :param dict_value:字典中原有的值
    :param tip_message: 提示的文字
    :return: 如果用户输入内容,返回内容,否则返回原有的值
    """
    # 1.提示用户输入内容
    result_str = input(tip_message)
    # 2.针对用户的输入进行判断,如果用户输入了内容,直接返回结果
    if len(result_str) > 0:
        return result_str
    # 3.如果用户没有输入,返回'字典原有的值'
    else:
        return dict_value