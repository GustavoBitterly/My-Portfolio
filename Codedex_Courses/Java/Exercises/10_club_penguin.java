
import java.util.Scanner;

public class HelloWorld {

    public static void main(String[] args) {
        // Write your code here 💖
        Scanner scanner = new Scanner(System.in);

        double usdValue = 0.0045;
        String clubPenguinCoin = "";
        double conversionResult = 0;

        System.out.println("Welcome to Club Penguin Conversion Calculator");
        System.out.println("Currency: 1 Coin = $0.0045 USD");

        System.out.print("How many Club Penguin Coins do yo have?");

        clubPenguinCoin = scanner.nextLine(); // int values

        System.out.print("Calculating.....");
        int coinValue = Integer.parseInt(clubPenguinCoin);
        conversionResult = (coinValue * usdValue);

        System.out.print("You have: $" + conversionResult + " USD in value");

    }
}
