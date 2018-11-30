import java.io.FileWriter;
import java.io.IOException;

public class Main {

    public static void main(String[] args) throws IOException {

        Time processor = new Time();
        String str = "";

        try {
            str = processor.readInputText();
        } catch (Exception e) {
            e.printStackTrace();
        }


        FileWriter nFile = new FileWriter("fileWriter.txt");

        nFile.write(processor.timePattern(str));

        nFile.close();
    }
}
//shop1 - 09:00-22:00 shop - 08:00-19:00 shop3 - 12:00-03:00