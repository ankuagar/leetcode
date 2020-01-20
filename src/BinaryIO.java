package com.ankur.javacode;
import java.io.*;
public class BinaryIO {

    public static void main(String[] args) throws FileNotFoundException, IOException{

        File products = new File("products.dat");
        DataOutputStream out = new DataOutputStream(new BufferedOutputStream(new FileOutputStream(products)));
//        out.writeBoolean(true);
//        out.writeBoolean(false);
        //out.writeInt(12);
        out.writeChar(300);
        //out.writeChars("This\n");
        //out.writeUTF("AABC");

//        out.writeUTF("This is.\n");
//        System.out.println(out.size());
//        out.writeChars("This is.\n");
//        System.out.println(out.size());

        out.close();

    }
}
