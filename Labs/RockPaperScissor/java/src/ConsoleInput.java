import java.util.Scanner;

public class ConsoleInput implements Input{
    private Scanner userInput = new Scanner(System.in);
    public String getInputString(){
        String result = userInput.nextLine();
        return result;
    }
    public int getInputInt(){
        int result;
        result = -1;
        do {
            try {
                result = userInput.nextInt();
            } catch (NumberFormatException exception) {
                // Output expected NumberFormatException.
                System.out.println("Please enter a integer");
            }
        } while (result < 0);

        return result;
    }
}
