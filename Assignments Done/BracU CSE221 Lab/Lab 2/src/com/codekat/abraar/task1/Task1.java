package com.codekat.abraar.task1;

import java.util.*;
import java.io.*;

public class Task1 {

    public static void main() throws Exception {

        File file1 = new File("src/com/codekat/abraar/task1/input1.txt");
        Scanner sc = new Scanner(file1);
        int[] numbersToSort = new int[sc.nextInt()];
        int i = 0;
        while(sc.hasNextInt()) {
            numbersToSort[i] = sc.nextInt();
            i++;
        }
        new Task1(numbersToSort);
        sc.close();

    }

    Task1(int[] Array) {

        bubbleSort(Array);
        printArrayToFile(Array);

    }

    // Bubble Sort Time Complexity : Best O(n), Worst O(n^2), Average O(n^2)
    // Bubble Sort Space Complexity : O(1); StableSort = Yes;
    void bubbleSort(int[] Array) {

        int n = Array.length;
        boolean swapped;
        for (int i = 0; i < n - 1; i++) {
            swapped = false;
            for (int j = 0; j < n - i - 1; j++) {
                if (Array[j] > Array[j + 1]) {
                    int temp = Array[j];
                    Array[j] = Array[j + 1];
                    Array[j + 1] = temp;
                    swapped = true;
                }
            }
            // if not swapped, then the array is already sorted;
            // this makes the algorithm optimized, ie best case O(n) complexity.
            if (!swapped) {
                break;
            }
        }
    }

    void printArray(int[] Array) {
        for (int j : Array) {
            System.out.print(j + " ");
        }
        System.out.println();
    }

    void printArrayToFile(int[] Array) {
        try {
            FileWriter Writer = new FileWriter("src/com/codekat/abraar/task1/output1.txt");

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
