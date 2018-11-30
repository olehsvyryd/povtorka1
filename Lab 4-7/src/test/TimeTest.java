import org.junit.Test;

import java.io.FileWriter;
import java.io.IOException;

import static org.junit.Assert.*;

public class TimeTest {

    @Test
    public void processText() throws IOException {
        Time processor = new Time();

        // first test
        assertEquals(processor.timePattern("shop1 14:45-14:46 shop2 11:00-14:30"), "14:45-14:46, 11:00-14:30, ");
        // second test
        assertEquals(processor.timePattern("14:45-14:46 11:00-14:30"), "14:45-14:46, 11:00-14:30, ");
        // third test
        assertEquals(processor.timePattern("14:45-14:46 shop1"), "14:45-14:46, ");


        FileWriter nFile = new FileWriter("fileWriter.txt");

        nFile.write(processor.timePattern("14:45-14:46 11:00-14:30"));

        nFile.close();
    }
}