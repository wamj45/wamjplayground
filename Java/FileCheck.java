import java.io.File;
import java.util.*;

public class FileCheck{
  public static void main(String[] args) {

    String filePath = "/Users/wamj45/wamjplaygro";

    System.out.printf("\nWe are looking for: %s", filePath);

    try {
      File file = new File(filePath);
      file.createNewFile();
      boolean check = file.exists();
      if ( check == true)
        System.out.println("\nYea the path exists vato");
      else
        System.out.println("\nNah we didn't find the file");

    }
    catch (Exception e) {
      e.printStackTrace();
    }
  }
}
