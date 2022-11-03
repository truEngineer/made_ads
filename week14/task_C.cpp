#include <iostream>
#include <vector>
 
std::string s, p, t;
std::vector<int> prf, ans;
 
void kmp() {
    s = p + '+' + t;
    prf.resize(s.size() + 1);
    prf[0] = -1;
    for (int i = 1; i < s.size() + 1; ++i) {
        for (int k = prf[i - 1]; ; k = prf[k]) {
            if (k == -1 or s[k] == s[i - 1]) {
                prf[i] = k + 1;
                break;
            }
        }
        if (prf[i] == p.size()) {
            ans.push_back(i - 2 * p.size());
        }
    }
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    std::cin >> p >> t;
    kmp();
    std::cout << ans.size() << '\n';
    for (int e : ans) {
        std::cout << e << ' ';
    }
 
    return 0;
}
