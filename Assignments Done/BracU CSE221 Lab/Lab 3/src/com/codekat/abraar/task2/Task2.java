package com.codekat.abraar.task2;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Scanner;

public class Task2 {
    public static void main() throws FileNotFoundException {

        File file1 = new File("src/com/codekat/abraar/task2/input2.txt");
        Scanner sc = new Scanner(file1);
        int n = sc.nextInt();
        int e = sc.nextInt();
        GraphT2 g = new GraphT2(n);
        g.clearFile();

        for (int i = 0; i < e; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            g.addEdge(a - 1, b - 1);
        }
        sc.close();
        g.BFS(1, 12);
    }
}


class GraphT2 {

    private final int V;
    private final LinkedList[] adj;

    public ArrayList<Integer> bfs = new ArrayList<>();

    GraphT2(int V) {
        this.V = V;
        adj = new LinkedList[V];
        for (int i = 0; i < V; ++i)
            adj[i] = new LinkedList<Integer>();
    }

    void addEdge(int v, int w) { adj[v].add(w); }

    void BFSUtil(int s) {

        boolean[] visited = new boolean[V];
        LinkedList<Integer> queue = new LinkedList<>();

        visited[s] = true;
        queue.add(s);

        while (queue.size() != 0) {
            s = queue.poll();
            int p1 = s + 1;
            // System.out.print(p1 + " ");
            bfs.add(p1);

            for (Object o : adj[s]) {
                int n = (int) o;
                if (!visited[n]) {
                    visited[n] = true;
                    queue.add(n);
                }
            }
        }
    }

    public void BFS(int source, int dest) {
        printAToFile("Places: ");
        // System.out.println("Places: ");
        BFSUtil(source-1);
        for (int x : bfs) {
            printAToFile(x + " ");
            // System.out.print(x + " ");
            if (x == dest) {
                printAToFile("\n");
                //System.out.println();
                break;
            }
        }
    }

    void printAToFile(String s) {
        try {
            FileWriter Writer = new FileWriter("src/com/codekat/abraar/task2/output2.txt", true);
            Writer.append(s).append(" ");
            Writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void clearFile() {
        try {
            new FileWriter("src/com/codekat/abraar/task2/output2.txt", false).close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

