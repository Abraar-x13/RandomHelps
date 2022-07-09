package com.codekat.abraar.task5;

import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;
import java.util.*;
import java.io.*;

public class Task5b {

    /*
     * I was confused about the question. If I make an assumption that there
     * are no repeating elements, I can code it. But the given input has
     * element 10, twice.
     * So I took help from this source :
     * https://stackoverflow.com/questions/5011177/how-to-find-kth-smallest-integer-in-an-unsorted-array-without-sorting-the-array
     */

    public static void main() throws FileNotFoundException {

        /*
        input file format :
        7 (Number of elements)
        1 3 4 5 9 10 10 (The elements)
        3 (number of queries)
        5 7 2 (each query (k))
         */

        File file1 = new File("src/com/codekat/abraar/task5/input5b.txt");
        Scanner sc = new Scanner(file1);
        int len = sc.nextInt();
        int[] numbersToSort = new int[len];
        int i = 0;
        while(sc.hasNextInt()) {
            if( i == len ) break;
            numbersToSort[i] = sc.nextInt();
            i++;
        }
        int p = sc.nextInt();
        int kk;
        while(p-- != 0) {
            kk = sc.nextInt();
            findK(numbersToSort, 0, len - 1, kk - 1);
            printToFile(numbersToSort[kk - 1]);
        }
        sc.close();
    }

    private static void printToFile(int k) {
        try {
            Files.write(Paths.get("src/com/codekat/abraar/task5/output5b.txt"), (String.valueOf(k) + "\n").getBytes(), StandardOpenOption.APPEND);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }


    static int findPivot(int a, int b, int c) {
        if (a > b) {
            if (c > a) {
                return a;
            } else return Math.max(c, b);
        } else {
            if (c > b) {
                return b;
            } else return Math.max(c, a);
        }
    }

    static void findK(int[] Array, int l, int r, int target) {

        if (l >= r) {
            return;
        }

        int mid = (l + r) / 2;
        int pivot = findPivot(Array[mid], Array[l], Array[r]);
        int i = l; int j = r;
        while (i <= j) {
            while (Array[i] < pivot) {
                i++;
            }
            while (Array[j] > pivot) {
                j--;
            }
            if (i <= j) {
                int temp = Array[i];
                Array[i] = Array[j];
                Array[j] = temp;
                i++; j--;
            }
        }
        if (target <= (i - 1)) {
            findK(Array, 0, i - 1, target);
        } else {
            findK(Array, i, r, target);
        }

    }


}
