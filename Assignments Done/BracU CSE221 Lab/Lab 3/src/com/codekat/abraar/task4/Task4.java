package com.codekat.abraar.task4;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;

public class Task4 {

    @SuppressWarnings("unchecked")
    public static void main() throws FileNotFoundException {

        File file1 = new File("src/com/codekat/abraar/task4/input4.txt");
        Scanner sc = new Scanner(file1);
        clearFile();
        int T = sc.nextInt();
        for(int tc = 0; tc < T; tc++) {

            Task4 T4 = new Task4();
            int n = sc.nextInt();
            int m = sc.nextInt();
            Vector<Integer>[] adj = new Vector[n];

            for (int i = 0; i < adj.length; i++) {
                adj[i] = new Vector<>();
            }

            for (int i =0; i < m; i++) {
                int x = sc.nextInt() - 1;
                int y = sc.nextInt() - 1;
                T4.addEdge(adj, x, y);
            }

            int start = 0;
            int end = n - 1;
            T4.minEdgeBFS(adj, start, end, n);
        }
        sc.close();

    }

    void addEdge(Vector<Integer>[] adj, int u, int v) {
        adj[u].add(v);
        adj[v].add(u);
    }

    void minEdgeBFS(Vector<Integer>[] adj, int u, int v, int n) {

        Vector<Boolean> visited = new Vector<Boolean>(n);
        Vector<Integer> dist = new Vector<Integer>(n);

        for (int i = 0; i < n; i++) {
            visited.addElement(false);
            dist.addElement(0);
        }

        Queue<Integer> Q = new LinkedList<>();
        dist.setElementAt(0, u);
        Q.add(u);
        visited.setElementAt(true, u);
        while (!Q.isEmpty()) {
            int x = Q.peek();  Q.poll();

            for (int i = 0; i < adj[x].size(); i++) {
                if (visited.elementAt(adj[x].get(i))) {
                    continue;
                }
                dist.setElementAt(dist.get(x) + 1, adj[x].get(i));
                Q.add(adj[x].get(i));
                visited.setElementAt(true, adj[x].get(i));
            }
        }
        printAToFile(String.valueOf(dist.get(v)));
    }

    void printAToFile(String s) {
        try {
            FileWriter Writer = new FileWriter("src/com/codekat/abraar/task4/output4.txt", true);
            Writer.append(s).append("\n");
            Writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void clearFile() {
        try {
            new FileWriter("src/com/codekat/abraar/task4/output4.txt", false).close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
