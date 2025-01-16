import random
import sys

def main():
    number_to_guess = random.randint(1, 100)
    number_of_tries = 0
    has_guessed_correctly = False

    print("欢迎来到猜数字游戏！")
    print("我已经想好了一个1到100之间的数字。")

    while not has_guessed_correctly:
        try:
            guess = int(input("请输入你的猜测: "))
        except ValueError:
            print("请输入一个有效的数字。")
            continue
        number_of_tries += 1

        if guess < number_to_guess:
            print("太小了，再试一次！")
        elif guess > number_to_guess:
            print("太大了，再试一次！")
        else:
            has_guessed_correctly = True
            print(f"恭喜你，猜对了！你总共猜了 {number_of_tries} 次。")

    # 将猜测次数保存到文件
    try:
        with open("guess_results.txt", "a") as writer:
            writer.write(f"用户猜对数字 {number_to_guess} 共尝试了 {number_of_tries} 次。\n")
    except IOError as e:
        print(f"保存文件时发生错误: {e.strerror}")

if __name__ == "__main__":
    main()