#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
 
struct Vertex {
    int row, col;
    Vertex(): row(-1), col(-1) {}
    Vertex(int row, int col): row(row), col(col) {}
};
 
int n, m;
const int dx[8] = {2, 2, 1, 1, -1, -1, -2, -2};
const int dy[8] = {1,-1, 2, -2, 2, -2, 1, -1};
std::vector<std::vector<Vertex>> prev;
std::vector<std::vector<bool>> visited;
 
bool on_board(const Vertex& p) {
    return p.row >= 0 and p.row < n and p.col >= 0 and p.col < m;
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    std::cin >> n;
    m = n;
    prev.resize(n, std::vector<Vertex>(m, Vertex()));
    visited.resize(n, std::vector<bool>(m, false));
    int beg_row, beg_col, end_row, end_col;
    std::cin >> beg_col >> beg_row >> end_col >> end_row;
    std::queue<Vertex> q;
    Vertex start(beg_row - 1, beg_col - 1);
    q.push(start);
    visited[start.row][start.col] = true;
    while(!q.empty()) {
        Vertex cur = q.front();
        q.pop();
        for (int i = 0; i < 8; ++i) {
            Vertex nbr(cur.row + dy[i], cur.col + dx[i]);
            if (on_board(nbr) and !visited[nbr.row][nbr.col]) {
                visited[nbr.row][nbr.col] = true;
                prev[nbr.row][nbr.col] = cur;
                q.push(nbr);
            }
        }
    }
    Vertex last(end_row - 1, end_col - 1);
    std::vector<Vertex> path;
    while (last.row != -1 or last.col != -1) {
        path.emplace_back(last);
        last = prev[last.row][last.col];
    }
    std::reverse(path.begin(), path.end());
    std::cout << path.size() << "\n";
    for (auto& p : path) {
        std::cout << p.col + 1 << " " << p.row + 1 << "\n";
    }
 
    return 0;
}
