int bfs_find_max_dist(int s, vector <int>& dist){
    while (!q.empty())q.pop();
    for (int i = 1; i <= n; i++){
        dist[i] = -1;
    }
    dist[s] = 0;
    q.push(s);
    while (!q.empty()){
        int u = q.front();
        q.pop();
        for (int v: graph[u]){
            if (dist[v] == -1){
                q.push(v);
                dist[v] = dist[u] + 1;
            }
        }
    }
    int i_max = s;
    for (int i = 1; i <= n; i++){
        if (dist[i] > dist[i_max] && (affected[i])) i_max = i;
    }
    return i_max;
}
 
int main(){
   // read();
    cin >> n >> m >> d;
    for (int i = 1; i <= m; i++){
        cin >> p[i];
        affected[p[i]] = 1;
    }
    for (int i = 1; i < n; i++){
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }
    dist0.resize(n + 1);
    dist1.resize(n + 1);
    distA.resize(n + 1);
    distB.resize(n + 1);
    int u = bfs_find_max_dist(p[1], dist0);
    int v = bfs_find_max_dist(u, dist1);
    //cout << u << " " << v << endl;
 
    bfs_find_max_dist(u, distA);
    bfs_find_max_dist(v, distB);
    int res = 0;
    for (int i = 1; i <= n; i++){
        if (distA[i] <= d && distB[i] <= d){
            res++;
            //cout << i << " ";
        }
    }
    //cout << endl;
    cout << res << endl;
}

main()