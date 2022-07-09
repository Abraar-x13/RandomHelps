package com.codekat.abraar.task5;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Task5a {

    public static void main() throws FileNotFoundException {
        File file1 = new File("src/com/codekat/abraar/task5/input5a.txt");
        Scanner sc = new Scanner(file1);
        int[] numbersToSort = new int[sc.nextInt()];
        int i = 0;
        while(sc.hasNextInt()) {
            numbersToSort[i] = sc.nextInt();
            i++;
        }
        sc.close();
        new Task5a(numbersToSort);
    }

    Task5a(int[] Array) {

        printStringToFile("Array before sorting : ");
        printArrayToFile(Array);
        long start1 = System.nanoTime();
        quickSort(Array);
        printStringToFile("Array after sorting : ");
        printArrayToFile(Array);
        long end1 = System.nanoTime();
        printStringToFile("Elapsed Time in nano seconds: " + (end1 - start1));

    }


    int partition(int[] Array, int low, int high) {

        int pivot = Array[high];
        int i = (low - 1);

        for (int j = low; j <= high - 1; j++) {
            if (Array[j] < pivot) {
                i++;
                int temp = Array[i];
                Array[i] = Array[j];
                Array[j] = temp;
            }
        }
        int temp = Array[i + 1];
        Array[i + 1] = Array[high];
        Array[high] = temp;
        return (i + 1);
    }

    void quickSort(int[] Array) {
        quickSort(Array, 0, Array.length - 1);
    }

    void quickSort(int[] Array, int low, int high) {
        if (low < high) {
            int pi = partition(Array, low, high);
            quickSort(Array, low, pi - 1);
            quickSort(Array, pi + 1, high);
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
            FileWriter Writer = new FileWriter("src/com/codekat/abraar/task5/output5a.txt", true);

            for (int j : Array) {
                Writer.append(String.valueOf(j)).append(" ");
            }
            Writer.append("\n");
            Writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    void printStringToFile(String s) {
        try {
            FileWriter Writer = new FileWriter("src/com/codekat/abraar/task5/output5a.txt", true);
            Writer.append(s);
            Writer.append("\n");
            Writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}

