import java.util.ArrayList;

public class TestInput implements Input{

    private ArrayList<String> testInputs;

    public void setTestInputs(ArrayList<String> inputs){
        testInputs = inputs;
    }

    public String getInputString(){

        String result = testInputs.remove(0);
        return result;
    }

    public int getInputInt(){
        String result = getInputString();
        return Integer.parseInt(result);
    }
}
