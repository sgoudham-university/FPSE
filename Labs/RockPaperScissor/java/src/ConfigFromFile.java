import java.io.File;  // Import the File class
import java.io.IOException;
import java.util.Scanner; // Import the Scanner class to read text files
import java.util.List;
import java.util.ArrayList;


public class ConfigFromFile implements Config{
    final String configPath = "resource/Config/properties.cfg";
    List<String> propertyData = new ArrayList<String>();

    private void populatePropertyData(){
        try {
            File propertyFile = new File(this.configPath);
            Scanner propertyReader = new Scanner(propertyFile);
            while (propertyReader.hasNextLine()) {
                String propertyRow = propertyReader.nextLine();
                this.propertyData.add(propertyRow);
            }
            propertyReader.close();
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }

    public List<String> getConfig(){
        if (this.propertyData.isEmpty()) {
            populatePropertyData();
        }
        return propertyData;
    }
}
