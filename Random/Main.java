import java.util.*;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int e = sc.nextInt();
        Graph g = new Graph(n);

        for (int i = 0; i < e; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            g.addEdge(a -1 , b -1);
        }
        sc.close();

        System.out.println( "\nDFS -");
        g.DFS(n);
        for (int x : g.dfs) {
            System.out.print(x + " ");
            if (x == n) {
                System.out.println();
                break;
            }
        }
        
        System.out.println("\nBFS -");
        g.BFS(0);
        for (int x : g.bfs) {
            System.out.print(x + " ");
            if (x == n) {
                System.out.println();
                break;
            }
        }

    }
}

class Graph {

    private int V;
    private LinkedList<Integer> adj[];

    public ArrayList<Integer> bfs = new ArrayList<>();
    public ArrayList<Integer> dfs = new ArrayList<>();

    @SuppressWarnings("unchecked")
    Graph(int V) {
        this.V = V;
        adj = new LinkedList[V];
        for (int i = 0; i < V; ++i)
            adj[i] = new LinkedList<Integer>();
    }

    void addEdge(int v, int w) {
        adj[v].add(w);
    }

    void BFS(int s) {

        boolean visited[] = new boolean[V];
        LinkedList<Integer> queue = new LinkedList<Integer>();

        visited[s] = true;
        queue.add(s);

        while (queue.size() != 0) {
            s = queue.poll();
            int p1 = s + 1;
            // System.out.print(p1 + " ");
            bfs.add(p1);

            Iterator<Integer> i = adj[s].listIterator();
            while (i.hasNext()) {
                int n = i.next();
                if (!visited[n]) {
                    visited[n] = true;
                    queue.add(n);
                }
            }
        }
    }

    void DFSUtil(int v, boolean visited[], int dest) {

        visited[v] = true;
        int p2 = v + 1;
        // System.out.print(p2 + " ");
        dfs.add(p2);

        Iterator<Integer> i = adj[v].listIterator();
        while (i.hasNext()) {
            int n = i.next();
            if (!visited[n]) {
                DFSUtil(n, visited, dest);
            }
        }
    }

    void DFS(int dest) {

        boolean visited[] = new boolean[V];

        for (int i = 0; i < V; ++i) {
            if (!visited[i]) {
                DFSUtil(i, visited, dest);
            }
        }
    }
}

