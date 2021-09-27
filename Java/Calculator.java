import java.util.*;

public class Calculator {
  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);
    String options = "1. Addition \n2. Subtraction \n3. Multiplication \n4. Division";

    System.out.println("Welcome to my calculator!");
    System.out.println("Which operation do you want to do: ");
    System.out.println(options);

    int selcetion = in.nextInt();
    System.out.printf("\nYou have selected: %d\n", selcetion);
  }


}
