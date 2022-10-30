#include <iostream>
#include <vector>
 
const int PRIME = 11;
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    std::string s;
    std::cin >> s;
    std::vector<int> pow(s.size() + 1);
    std::vector<int> hash(s.size() + 1);
    pow[0] = 1;
    hash[0] = 0;
    for (int i = 1; i < s.size() + 1; ++i) {
        pow[i] = PRIME * pow[i - 1];
        hash[i] = hash[i - 1] * PRIME + s[i - 1];
    }
    int m, a, b, c, d;
    std::cin >> m;
    for (int i = 0; i < m; ++i) {
        std::cin >> a >> b >> c >> d;
        std::cout << ((hash[b] - hash[a - 1] * pow[b - (a - 1)] ==
                       hash[d] - hash[c - 1] * pow[d - (c - 1)]) 
                       ? "Yes\n" : "No\n");
    }
 
    return 0;
}
