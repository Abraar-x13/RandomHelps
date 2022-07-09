package com.codekat.abraar.task3;

import java.io.FileNotFoundException;
import java.util.*;

public class Task3 {

    public static void main() throws FileNotFoundException {

//        File file1 = new File("src/com/codekat/abraar/task3/input3.txt");
//        Scanner sc = new Scanner(file1);
//        int len = sc.nextInt();
//        int[] id = new int[len];
//        int[] marks = new int[len];
//        int i = 0;
//        while(sc.hasNextInt()) {
//            if (i == len) break;
//            id[i] = sc.nextInt();
//            i++;
//        }
//        int j = 0;
//        while(sc.hasNextInt()) {
//            if (j == len) break;
//            marks[i] = sc.nextInt();
//            j++;
//        }
//        new Task3(len, id, marks);
//        sc.close();
    }

    Task3(int N, int[] id, int[] marks) {
//        for (int x : id) {
//            System.out.println(x);
//        }
//        for(int x : marks) {
//            System.out.println(x);
//        }
        sortByValueJava8Stream(N, id, marks);
    }

    private static void sortByValueJava8Stream(int N, int[] id, int[] marks)
    {
        Map<Integer, Integer> unSortedMap = getUnSortedMap(id, marks, N);

        LinkedHashMap<String, Integer> reverseSortedMap = new LinkedHashMap<>();
        unSortedMap.entrySet().stream().sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
                .forEachOrdered(x -> reverseSortedMap.put(String.valueOf(x.getKey()), x.getValue()));

        System.out.println("Reverse Sorted Map   : " + reverseSortedMap);
    }

    private static Map<Integer, Integer> getUnSortedMap(int[] aa, int[] bb, int ll) {
        Map<Integer, Integer> unsortMap = new HashMap<>();
        for (int i = 0; i < ll; i++) {
            unsortMap.put(aa[i], bb[i]);
        }
        return unsortMap;
    }

}
