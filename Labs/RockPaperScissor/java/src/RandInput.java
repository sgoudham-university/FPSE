import java.util.Random;

public class RandInput implements Input{
    public String getInputString(){
        return String.valueOf(getInputInt());

    }

    @Override
    public int getInputInt() {
        Random rand = new Random();
        int result;
        result = rand.nextInt(3);
        return result;
    }
}
