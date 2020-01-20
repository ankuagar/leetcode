package com.ankur.javacode;

import java.util.HashMap;
import java.util.Map;

public class HashMapTest {

    public static void  main(String[] args) {

        HashMap<Integer, Integer> h = new HashMap<Integer, Integer>();


        for(int i = 0; i < 10; i++) {
            h.put(i, i*i);
        }

        for(Map.Entry<Integer, Integer> e: h.entrySet()) {
            System.out.println(e.getKey() + " " + e.getValue());
        }

    }
}
