import java.util.ArrayList;
import java.util.Scanner;
//import java.util.io.*;
import java.util.Random;
import java.util.List;

class RockPaperScissor {

    private Input userInput;
    private Input computerInput;
    private Output userOutput;
    private Config config;
    private ErrorLevel errorLevel = ErrorLevel.WARNING;
    private ErrorLog errorLog;
    private String className = "RockPaperScissor";
    private List<String> property;

    public void setErrorLevel(ErrorLevel errorLevel) {
        this.errorLevel = errorLevel;
    }

    public void setUserInput(Input inputType){
        userInput = inputType;
    }

    public void setUserOutput(Output outputType){
        userOutput = outputType;
    }

    public void setComputerInput(Input inputType){
        computerInput = inputType;
    }

    public void setConfig(Config configType){
        this.config = configType;
    }


    RockPaperScissor(){

        userInput = new ConsoleInput();
        userOutput = new ConsoleOutput();
        computerInput = new RandInput();
        config = new ConfigFromFile();
        errorLog = ErrorLog.getInstance();
        property = new ArrayList<String>();

    }

    private void writeError(String method, String message, ErrorLevel errorLevel){

        errorLog.writeMessage(className,method, message,errorLevel, this.errorLevel);
    }

    public static String generateRequest(String[] weapons){
        String display = "Please select";
        /*for (int i=0;i<weapons.length;i++){*/
        int i=0;
        for (String weapon: weapons){
            display += " " + i + " " + weapon;
            i++;
        };
        return display;
    }

    private int requestPlay(String[] weapons)
    {
        String request;
        request = generateRequest(weapons);
        userOutput.output(request);

        int userWeapon = userInput.getInputInt();
        if (userWeapon > 23){
            writeError("requestPlay","userWeapon greater than 3", ErrorLevel.ERROR );
        }

        return userWeapon;
    }



    public static String determineWinner(String[] weaponList, int userWeapon, int computerWeapon)
    {
        String winner;
        if (userWeapon == computerWeapon)
        {
            winner = "Draw both selected " + weaponList[computerWeapon];
        }
        else if ((userWeapon + 1) % 3 == computerWeapon)
        {
            winner = "You win and beat the computer's " + weaponList[computerWeapon];
        }
        else if ((computerWeapon + 1) % 3 == userWeapon)
        {
            winner = "Computer wins with " + weaponList[computerWeapon];
        }
        else {
            winner = "Please select 1. Rock, 2. Scissors or 3. Paper";
        }

        return winner;

    }

    private void displayWinner(String winner)
    {
        userOutput.output(winner);
    }

    public void playGame(String[] weaponList){
        int userWeapon;

        int computerWeapon;
        String winner;
        //Final declares
        userWeapon = requestPlay(weaponList);
        do{
            computerWeapon = computerInput.getInputInt();
            winner = determineWinner(weaponList, userWeapon, computerWeapon);
            displayWinner(winner);
            userWeapon = requestPlay(weaponList);
        } while (userWeapon< weaponList.length);

    }

    public void run(){
        //Final declares
        this.property = config.getConfig();
        String request = generateGamesListRequest();
        List<String[]> weaponLists = getWeaponLists(this.property);
        this.userOutput.output(request);
        int userGame = this.userInput.getInputInt();
        while (userGame < this.property.size())
        {
            String[] weaponlist = weaponLists.get(userGame);
            playGame(weaponlist);
            this.userOutput.output(request);
            userGame = this.userInput.getInputInt();
        } ;
    }

    public String generateGamesListRequest(){
        List<String> listOfGames = getListOfGames();
        String request = getGamesRequest(listOfGames);
        return request;
    }

    public List<String[]> getWeaponLists(List<String> property){
        List<String[]> weaponLists = new ArrayList<String[]>();
        if (this.property.isEmpty()) {
            this.property = config.getConfig();
        }
        for (int counter = 1; counter < property.size(); counter++){
            weaponLists.add(property.get(counter).split(":")[1].split(","));
        }
        return weaponLists;
    }

    public List<String> getListOfGames(){
        List<String> listOfGames = new ArrayList<String>();
        if (this.property.isEmpty()) {
            this.property = config.getConfig();
        }
        for (int counter = 1; counter < this.property.size(); counter++){
            listOfGames.add(this.property.get(counter).split(":")[0]);
        }
        return listOfGames;
    }


    private String getGamesRequest(List<String> listOfGames){
        String request = "Please select";
        for (int counter = 0; counter < listOfGames.size(); counter++){
            request += " " + String.valueOf(counter) + " - " + listOfGames.get(counter);
        }
        return request;
    }

    public static void main(String[ ] args){
        RockPaperScissor rockPaperScissor = new RockPaperScissor();
        rockPaperScissor.run();
    }

}
