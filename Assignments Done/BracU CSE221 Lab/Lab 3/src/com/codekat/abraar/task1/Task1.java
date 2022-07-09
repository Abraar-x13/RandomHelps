package com.codekat.abraar.task1;

import java.util.*;
import java.io.*;

public class Task1 {
    public static void main() throws IOException {

        File file1 = new File("src/com/codekat/abraar/task1/input1.txt");
        Scanner sc = new Scanner(file1);
        int n = sc.nextInt();
        int e = sc.nextInt();
        GraphT1 g = new GraphT1(n);
        g.clearFile();

        for (int i = 0; i < e; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            g.addEdge(a - 1, b - 1);
        }
        sc.close();
    }
}

class GraphT1 {

    private final LinkedList<Integer>[] adj;

    @SuppressWarnings("unchecked")
    GraphT1(int V) {
        adj = new LinkedList[V];
        for (int i = 0; i < V; ++i)
            adj[i] = new LinkedList<Integer>();
        // System.out.println("Created a graph with " + V + " vertices");
        printAToFile("Created a graph with " + V + " vertices");
    }

    public void addEdge(int v, int w) {
        adj[v].add(w);
        v++; w++;
        // System.out.println("Added an edge from " + v + " to " + w);
        printAToFile("Added an edge from " + v + " to " + w);
    }

    void printAToFile(String s) {
        try {
            FileWriter Writer = new FileWriter("src/com/codekat/abraar/task1/OutputTask1.txt", true);
            Writer.append(s).append("\n");
            Writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    void clearFile() {
        try {
            new FileWriter("src/com/codekat/abraar/task1/OutputTask1.txt", false).close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}