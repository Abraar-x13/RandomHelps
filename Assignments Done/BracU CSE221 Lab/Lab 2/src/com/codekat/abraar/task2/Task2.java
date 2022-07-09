package com.codekat.abraar.task2;

import java.util.*;
import java.io.*;

public class Task2 {

    public static void main() throws FileNotFoundException {
        File file1 = new File("src/com/codekat/abraar/task2/input2.txt");
        Scanner sc = new Scanner(file1);
        int[] numbersToSort = new int[sc.nextInt()];
        int m = sc.nextInt();
        int i = 0;
        while(sc.hasNextInt()) {
            numbersToSort[i] = sc.nextInt();
            i++;
        }
        new Task2(numbersToSort, m);
        sc.close();
    }
    Task2(int[] Array, int M) {

        selectionSort(Array);
        printFirstMToFIle(Array, M);

    }

    void selectionSort(int[] Array) {
        int n = Array.length;
        for (int i = 0; i < n - 1; i++) {
            // minIndex = argminj (A[i], A[i+1], ....... A[n-1])
            int minIndex = i;
            for (int j = i + 1; j < n; j++) {
                if (Array[j] < Array[minIndex]) {
                    minIndex = j;
                }
            }
            // swap A[i] and A[minIndex]
            int temp = Array[minIndex];
            Array[minIndex] = Array[i];
            Array[i] = temp;
        }
    }

    void printFirstM(int[] Array, int M) {
        for (int i = 0; i < M; ++i) {
            System.out.print(Array[i] + " ");
        }
        System.out.println();
    }

    void printFirstMToFIle(int[] Array, int M) {
        try {
            FileWriter Writer = new FileWriter("src/com/codekat/abraar/task2/output2.txt");

            for (int i = 0; i < M; ++i) {
                Writer.append(String.valueOf(Array[i])).append(" ");
            }
            Writer.append("\n");
            Writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
