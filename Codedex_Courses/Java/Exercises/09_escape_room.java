import java.util.Scanner;

public class Greetings {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        /*
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();

        System.out.println(name);
        */

        System.out.print("Welcome to the Java Escape Room");
        System.out.print("Answer thw next riddle: ");
        System.out.print("I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?");
        System.out.print("Answer: ");

        String riddleAnswer = scanner.nextLine(); // Echo

        System.out.print("Your answer is correct congratulation!!");

    }
}
