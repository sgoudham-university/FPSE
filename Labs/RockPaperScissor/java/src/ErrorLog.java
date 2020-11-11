import java.io.PrintWriter;

public class ErrorLog {
    private String fileName;
    private String filePreFix;
    static ErrorLog uniqueErrorLog;
    private ErrorLevel errorLevel = ErrorLevel.ERROR;
    private int fileNumber = 0;
    private int fileLineCounter = 0;

    final private int maxLineCount = 10;

    private ErrorLog(){}

    public static ErrorLog getInstance(){
        if (uniqueErrorLog == null){
            uniqueErrorLog = new ErrorLog();
        }
        return uniqueErrorLog;
    }

    private void setFileName(){
        fileNumber ++;
        fileName = filePreFix + fileNumber;
    }

    private boolean isSufficientErrorLevel(ErrorLevel messageErrorLevel, ErrorLevel classErrorLevel){
        boolean result = false;
        if (classErrorLevel == null){
            classErrorLevel = this.errorLevel;
        }
        if (messageErrorLevel.getLevel() >= classErrorLevel.getLevel()){
            result = true;
        }
        return result;
    }

    public void writeMessage(String className, String method, String message, ErrorLevel messageErrorLevel, ErrorLevel classErrorLevel){
        if (isSufficientErrorLevel(messageErrorLevel,classErrorLevel)){
            if (fileLineCounter >= maxLineCount || fileName == null){
                setFileName();
                fileLineCounter = 0;
            }
            try {
                PrintWriter writer = new PrintWriter(fileName, "UTF-8");
                writer.println(fileLineCounter + "|" + className + "|" + method + "|" + message );
                writer.close();
            }
            catch (Exception exception) {
                System.out.println("Failure to write to " + fileName);
            }
            fileLineCounter ++;
        }
    }
}