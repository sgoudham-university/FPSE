import java.util.ArrayList;

public class TestOutput implements Output{
    private ArrayList<String> testOutputs;

    TestOutput(){
        ArrayList<String> temp = new ArrayList<String>(10);
        testOutputs = temp;
    }

    public void setTestOutputs(ArrayList<String> outputs){
        testOutputs = outputs;
    }

    public ArrayList<String> getTestOutputs(){
        return testOutputs;
    }


    public void clear(){
        testOutputs.clear();
    }
    public void output(String display){
        testOutputs.add(display);
    }
    public void output(ArrayList<String> displayOutput){
        for (String display : displayOutput){
            testOutputs.add(display);
        }
    }
}
