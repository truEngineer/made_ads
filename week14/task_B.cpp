#include <iostream>
#include <vector>
 
std::string s;
std::vector<int> z;
int l = 0, r = 1;
 
int z_func(int i) {
    if (i <= r) {
        z[i] = std::min(z[i - l], r - i);
    }
    while (s[z[i]] == s[i + z[i]]) {
        z[i] += 1;
    }
    if (i + z[i] > r) {
        l = i;
        r = i + z[i];
    }
    return z[i];
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    std::cin >> s;
    z.resize(s.size(), 0);
    for (int i = 1; i < z.size(); ++i) {
        std::cout << z_func(i) << ' ';
    }
 
    return 0;
}
