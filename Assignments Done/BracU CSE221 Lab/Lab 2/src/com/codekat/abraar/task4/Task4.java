package com.codekat.abraar.task4;

import java.util.*;
import java.io.*;

public class Task4 {

    public static void main() throws FileNotFoundException {
        File file1 = new File("src/com/codekat/abraar/task4/input4.txt");
        Scanner sc = new Scanner(file1);
        int[] numbersToSort = new int[sc.nextInt()];
        int i = 0;
        while(sc.hasNextInt()) {
            numbersToSort[i] = sc.nextInt();
            i++;
        }
        new Task4(numbersToSort);
        sc.close();
    }

    Task4(int[] Array) {

        mergeSort(Array);
        printArrayToFile(Array);

    }


    // Merges two sorted sub-arrays
    void merge(int[] Array, int l, int m, int r) {

        int n1 = m - l + 1;
        int n2 = r - m;

        int[] L = new int[n1];
        int[] R = new int[n2];

        System.arraycopy(Array, l, L, 0, n1);
        for (int j = 0; j < n2; ++j) {
            R[j] = Array[m + 1 + j];
        }

        int i = 0, j = 0;
        int k = l;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                Array[k] = L[i]; i++;
            } else {
                Array[k] = R[j]; j++;
            }
            k++;
        }

        while (i < n1) {
            Array[k] = L[i]; i++; k++;
        }

        while (j < n2) {
            Array[k] = R[j]; j++; k++;
        }
    }

    void mergeSort(int[] Array) {
        mergeSort(Array, 0, Array.length - 1);
    }

    void mergeSort(int[] Array, int l, int r) {
        if (l < r) {
            int m = l + (r - l) / 2;

            mergeSort(Array, l, m);
            mergeSort(Array, m + 1, r);

            merge(Array, l, m, r);
        }
    }

    void printArray(int[] Array) {
        int n = Array.length;
        for (int j : Array) {
            System.out.print(j + " ");
        }
        System.out.println();
    }

    private void printArrayToFile(int[] Array) {
        try {
            FileWriter Writer = new FileWriter("src/com/codekat/abraar/task4/output4.txt");

            for (int j : Array) {
                Writer.append(String.valueOf(j)).append(" ");
            }
            Writer.append("\n");
            Writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
