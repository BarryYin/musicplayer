import random
import sys
import tkinter as tk
from tkinter import messagebox

def main():
    number_to_guess = random.randint(1, 100)
    number_of_tries = 0

    def check_guess():
        nonlocal number_of_tries
        try:
            guess = int(entry.get())
        except ValueError:
            messagebox.showerror("输入错误", "请输入一个有效的数字。")
            return
        number_of_tries += 1

        if guess < number_to_guess:
            label.config(text="太小了，再试一次！")
        elif guess > number_to_guess:
            label.config(text="太大了，再试一次！")
        else:
            label.config(text=f"恭喜你，猜对了！你总共猜了 {number_of_tries} 次。")
            # 将猜测次数保存到文件
            try:
                with open("guess_results.txt", "a") as writer:
                    writer.write(f"用户猜对数字 {number_to_guess} 共尝试了 {number_of_tries} 次。\n")
            except IOError as e:
                messagebox.showerror("文件错误", f"保存文件时发生错误: {e.strerror}")
            root.quit()

    root = tk.Tk()
    root.title("猜数字游戏")

    label = tk.Label(root, text="欢迎来到猜数字游戏！\n我已经想好了一个1到100之间的数字。")
    label.pack(pady=10)

    entry = tk.Entry(root, width=20)
    entry.pack(pady=5)

    button = tk.Button(root, text="猜一下", command=check_guess)
    button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()