import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.FileWriter;


public class Time {


    public String readInputText() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter String\n");
        return br.readLine();
    }

    public String timePattern(String inputText) {
        Pattern p = Pattern.compile("(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9][-](0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]");
        Matcher m = p.matcher(inputText);
        StringBuilder finalStr = new StringBuilder("");

        while (m.find()) {
            String temp = inputText.substring(m.start(), m.end());

            finalStr.append(temp).append(", ");
        }

        return finalStr.toString();
    }

    public static void newFile() throws Exception {
        FileWriter nFile = new FileWriter("fileWriter.txt");

        nFile.close();
    }
}
