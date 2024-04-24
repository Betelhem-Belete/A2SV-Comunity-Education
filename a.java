import java.io.File;
import java.io.IOException;

public class A{
    public static void main(String args[]){
        //create flie object to a directory
        File directoryPath = new File("D:/");
        //listinfg files 
        File filesList[] = directoryPath.listFiles();
        System.out.prinln("List of Files");
        for(File file: filesList){
            System.out.prinln("File name" + file.getName());
            System.out.prinln("Path name" + file.getAbsolutePath());            
            System.out.prinln("File size" + file.getTotalSpace());
            System.out.prinln(" ");
        }
    }
}