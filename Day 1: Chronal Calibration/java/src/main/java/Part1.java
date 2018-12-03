import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;


public class Part1 {
    public static void main(String[] args) {
        Path inputPath = Paths.get("input.txt");
        try {
            List<String> input = Files.readAllLines(inputPath, Charset.forName("UTF-8"));

            for (String line : input) {
                System.out.println(line);
            }
        } catch (IOException e) {
            System.out.println(e);
        }

    }
}

