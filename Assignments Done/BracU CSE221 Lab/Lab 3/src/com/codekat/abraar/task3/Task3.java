package com.codekat.abraar.task3;


import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Scanner;

public class Task3 {
    public static void main() throws FileNotFoundException {

        File file1 = new File("src/com/codekat/abraar/task3/input3.txt");
        Scanner sc = new Scanner(file1);
        int n = sc.nextInt();
        int e = sc.nextInt();
        GraphT3 g = new GraphT3(n);
        g.clearFile();

        for (int i = 0; i < e; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            g.addEdge(a - 1, b - 1);
        }
        sc.close();
        g.DFS(n);

    }
}

class GraphT3 {

    private final int V;
    private final LinkedList[] adj;

    public ArrayList<Integer> dfs = new ArrayList<>();

    GraphT3(int V) {
        this.V = V;
        adj = new LinkedList[V];
        for (int i = 0; i < V; ++i)
            adj[i] = new LinkedList<>();
    }


    void addEdge(int v, int w) { adj[v].add(w); }


    void DFSUtil(int v, boolean[] visited, int dest) {

        visited[v] = true;
        int p2 = v + 1;
        // System.out.print(p2 + " ");
        dfs.add(p2);

        for (Object o : adj[v]) {
            int n = (int) o;
            if (!visited[n]) {
                DFSUtil(n, visited, dest);
            }
        }
    }

    void DFS(int dest) {

        boolean[] visited = new boolean[V];

        for (int i = 0; i < V; ++i) {
            if (!visited[i]) {
                DFSUtil(i, visited, dest);
            }
        }

        printAToFile("Places: ");
        for (int x : dfs) {
            printAToFile(x + " ");
            if (x == dest) {
                printAToFile("\n");
                break;
            }
        }
    }

    void printAToFile(String s) {
        try {
            FileWriter Writer = new FileWriter("src/com/codekat/abraar/task3/output3.txt", true);
            Writer.append(s).append(" ");
            Writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void clearFile() {
        try {
            new FileWriter("src/com/codekat/abraar/task3/output3.txt", false).close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}

