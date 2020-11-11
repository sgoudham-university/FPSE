public enum
ErrorLevel {
    ERROR( 300 ),
    WARNING(200),
    INFO(100);

    private int level;

    ErrorLevel(int level){
        this.level = level;
    }

    public int getLevel() {
        return level;
    }
}
