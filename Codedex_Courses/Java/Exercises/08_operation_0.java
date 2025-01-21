public class HelloWorld {
    public static void main(String[] args) {
        // Write your code here 💖
        double result = 0; 

        result = 8 + 2;     // result is now 10
        result = 8 - 2;     // result is now 6
        result = 8 * 2;     // result is now 16
        result = 8 / 2;     // result is now 4
        result = 8 % 2;     // result is now 0

        System.out.println(result); // 0

        double originalPrice = 60.0;
        double discount = 20.0;              

        // Apply discount
        double finalPrice = originalPrice - (originalPrice * (discount / 100));

        System.out.println(finalPrice); // Output: 48

        //EXERCISE
        double chemicalA = 35.8;
        double chemicalB = 21.9;
        
        double reactionResult =  (chemicalA + chemicalB) / (chemicalA*chemicalB);
    }
}
