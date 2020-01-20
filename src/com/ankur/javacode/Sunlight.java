package com.ankur.javacode;
import java.util.ArrayList;

public class Sunlight {

    public static void main(String[] args) {
         int kmFromSun = 150000000;
        int lightSpeed = 299792458;
        long mFromSun = kmFromSun * 1000L;
        double seconds = (double)mFromSun/lightSpeed;
        System.out.print("Light will use ");
        printTime(seconds);
        System.out.println(" to travel from the sun to the earth.");

    }

    public static void printTime(double sec) {
        int min = (int) (sec/60);
        sec = sec - min * 60;
        System.out.print(min + " minutes(s) and " + sec + " second(s)");
    }
}
