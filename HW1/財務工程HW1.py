import tkinter as tk
from tkinter import ttk
font = ("微軟正黑體", 20)  # GUI字體
dx = 180  # GUI格子大小
dy = 50
window = tk.Tk()
window.title("本金平均攤還法試算利息")
window.geometry("350x300")
show = False

def push():  # 按了按鈕確認執行
    in1 = textInput[0].get()
    in2 = textInput[1].get()
    in3 = textInput[2].get()
    if not in1.isdigit() or not in2.isdigit() or not in3.isdecimal():
        print("請輸入正確數字！")
        return
    
    Capital = int(in1) * 10000
    Period = int(in2)
    if Period == 1:
        window.geometry("900x450")
    elif Period == 2:
        window.geometry("900x550")
    elif Period == 0:
        window.geometry("350x300")
        print("期數不得為0！")
        return
    else:
        window.geometry("350x300")
        print("介面僅能顯示1~2期")
        Interest = float(in3) / (12 * 100)  # 以月利率計算
        MoReCapital = round(Capital / (Period * 12))  # 每期攤還本金(四捨五入)
        ReCapital = 0  # 總攤還本金
        Accu = 0  # 本金利息累計
        for i in range(1, Period*12 + 1):
            MoReInterest = round(Capital * Interest)  # 每期攤還利息(四捨五入)
            if Capital >= MoReCapital:  # 前幾期
                Capital -= MoReCapital  # 還沒還的本金
                Total = MoReInterest + MoReCapital
                Accu += Total
                print(MoReCapital, MoReInterest, Accu)
            else:  # 最後一期
                Total = MoReInterest + Capital
                Accu += Total
                print(Capital, MoReInterest, Accu)
        return
    Interest = float(in3) / (12 * 100)  # 以月利率計算
    MoReCapital = round(Capital / (Period * 12))  # 每期攤還本金(四捨五入)
    ReCapital = 0  # 總攤還本金
    Accu = 0  # 本金利息累計
    
    
    global tree  # 建立表格
    tree.place(x=2 * dx, y=10)
    tree["columns"]=("本金", "利息", "本金利息總計")
    tree.column("本金", width = 100)
    tree.column("利息", width = 100)
    tree.column("本金利息總計", width = 100)
    tree["height"] = Period * 12
     
    tree.heading("本金", text = "本金(元)")
    tree.heading("利息", text = "利息(元)	")
    tree.heading("本金利息總計", text = "本金利息累計(元)")
    
    chineseNumber = ["零", "一", "二", "三", "四", "五", "六",
                     "七", "八", "九", "十", "十一", "十二",
                     "十三", "十四", "十五", "十六", "十七", "十八",
                     "十九", "二十", "二十一", "二十二", "二十三", "二十四"]
      
    AllInterest = 0  # 計算全部利息
    for i in range(1, Period*12 + 1):
        MoReInterest = round(Capital * Interest)  # 每期攤還利息(四捨五入)
        AllInterest += MoReInterest
        if Capital >= MoReCapital:  # 前幾期
            Capital -= MoReCapital  # 還沒還的本金
            Total = MoReInterest + MoReCapital
            Accu += Total
            tree.insert("",i - 1, text="第" + chineseNumber[i] + "期", values=(MoReCapital, MoReInterest, Accu))
        else:  # 最後一期
            Total = MoReInterest + Capital
            Accu += Total
            tree.insert("",i - 1, text="第" + chineseNumber[i] + "期", values=(MoReCapital, MoReInterest, Accu))

    tree1 = ttk.Treeview(window, columns=['1','2'], show="tree")  # 表格
    tree1.place(x = 10, y = 300)
    tree1["height"] = 2
    tree1.column("1", width=50)
    tree1.column("2", width=50)
    tree1.insert("", 0, text="平均每月攤還本金(元)", values = MoReCapital)
    tree1.insert("", 1, text="全部利息(元)", values = AllInterest)

tree = ttk.Treeview()

l = tk.Label()  # GUI顯示文字
l["text"] = "*四捨五入至整數位"
l["font"] = font
l.place(x=0, y = 0)
l = tk.Label()  # GUI顯示文字
l["text"] = "*每期為一個月"
l["font"] = font
l.place(x=0, y = dy)


text = tk.Label()  # GUI顯示文字
text["text"] = "本金(萬)："
text["font"] = font
text.place(x=0,y = dy * 2)

textInput = []  # GUI輸入文字
textInput.append(tk.Entry())
textInput[0]["width"] = 20
textInput[0].place(x = dx, y = dy*2 + 10, height = dy - 20)

text = tk.Label()  # GUI顯示文字
text["text"] = "期數(年)："
text["font"] = font
text.place(x = 0, y = dy * 3)

textInput.append(tk.Entry())
textInput[1]["width"] = 20
textInput[1].place(x = dx, y = dy*3 + 10, height = dy - 20)

text = tk.Label()  # GUI顯示文字
text["text"] = "年利率(%)："
text["font"] = font
text.place(x = 0, y = dy * 4)

textInput.append(tk.Entry())
textInput[2]["width"] = 20
textInput[2].place(x = dx, y = dy*4 + 10, height = dy - 20)

button = tk.Button()  # GUI確認按鈕
button["text"]="確認"
button["width"] =10
button["height"] = 2
button["command"] = push
button.place(x = 130, y = 5 * dy)

window.mainloop()
