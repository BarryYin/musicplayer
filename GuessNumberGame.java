我import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;
import java.util.Scanner;

public class GuessNumberGame {
    public static void main(String[] args) {
        Random random = new Random();
        int numberToGuess = random.nextInt(100) + 1;
        Scanner scanner = new Scanner(System.in);
        int numberOfTries = 0;
        boolean hasGuessedCorrectly = false;

        System.out.println("欢迎来到猜数字游戏！");
        System.out.println("我已经想好了一个1到100之间的数字。");

        while (!hasGuessedCorrectly) {
            System.out.print("请输入你的猜测: ");
            int guess = scanner.nextInt();
            numberOfTries++;

            if (guess < numberToGuess) {
                System.out.println("太小了，再试一次！");
            } else if (guess > numberToGuess) {
                System.out.println("太大了，再试一次！");
            } else {
                hasGuessedCorrectly = true;
                System.out.println("恭喜你，猜对了！你总共猜了 " + numberOfTries + " 次。");
            }
        }

        scanner.close();

        // 将猜测次数保存到文件
        try (FileWriter writer = new FileWriter("guess_results.txt", true)) {
            writer.write("用户猜对数字 " + numberToGuess + " 共尝试了 " + numberOfTries + " 次。\n");
        } catch (IOException e) {
            System.out.println("保存文件时发生错误: " + e.getMessage());
        }
    }
}