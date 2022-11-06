#include <iostream>
#include <vector>
#include <unordered_map>
 
const int MAX = int(2e6);
 
int last = 0;
int tsize = 1;
std::vector<int> len(MAX, 0), link(MAX, 0), pos(MAX, 0);
std::unordered_map<char, int> next[MAX];
 
void add(char c, int place) {
    len[tsize] = len[last] + 1;
    pos[tsize] = place;
    int cur = tsize++;
    int p = last;
    while (p >= 0 and !next[p][c]) {
        next[p][c] = cur;
        p = link[p];
    }
    if (p != -1) {
        int q = next[p][c];
        if (len[p] == len[q] - 1) {
            link[cur] = q;
        } else {
            link[tsize] = link[q];
            next[tsize] = next[q];
            int vertex = tsize++;
            len[vertex] = len[p] + 1;
            pos[vertex] = place;
            link[q] = vertex;
            link[cur] = vertex;
            while (p >= 0 and next[p][c] == q) {
                next[p][c] = vertex;
                p = link[p];
            }
        }
    }
    last = cur;
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    std::string text;
    int m;
    std::cin >> text;
    std::cin >> m;
    link[0] = -1;
    std::string words[m];
    for(int i = 0; i < m; ++i) {
        std::cin >> words[i];
    }
    for (int i = 0; i < text.size(); ++i) {
        add(text[i], i);
    }
    for (auto& w : words) {
        bool match = true;
        int k = 0;
        for (auto c : w) {
            if (!next[k][c]) {
                match = false;
                break;
            }
            k = next[k][c];
        }
        std::cout << (match ? "Yes\n" : "No\n");
    }
 
    return 0;
}
