import java.util.Scanner;

public class Task {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int secretNumber = 5;
        int guess = 0;
        while (guess != secretNumber) {
            System.out.print("Guess the number (1-10): ");
            guess = input.nextInt();
            if (guess < secretNumber) {
                System.out.println("Too low!");
            } else if (guess > secretNumber) {
                System.out.println("Too high!");
            } else {
                System.out.println("Correct! You've guessed the number.");
            }
        }
    }
}