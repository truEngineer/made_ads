#include <iostream>
#include <vector>
#include <unordered_set>
 
const int PRIME = 1123;
const int LEN = 10001;
const int INF = INT_MAX;
 
std::vector<std::vector<int>> h;
std::vector<std::string> str;
std::vector<int> p(LEN);
 
std::string find_common_substr(int l) {
    std::unordered_set<int> set;
    for (int j = 0; j < h[0].size() - l; ++j) {
        set.insert(h[0][j + l] - h[0][j] * p[l]);
    }
    std::string ans;
    auto k = h.size();
    for (int i = 0; i < k; ++i) {
        std::unordered_set<int> next_set;
        for (int j = 0; j < h[i].size() - l; ++j) {
            auto hash = h[i][j + l] - h[i][j] * p[l];
            if (set.count(hash)) {
                next_set.insert(hash);
                if (i == k - 1) {
                    ans = str[i].substr(j, l);
                    break;
                }
            }
        }
        set = next_set;
    }
    return ans;
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    int k;
    std::cin >> k;
    h.resize(k);
    str.resize(k);
    p[0] = 1;
    for (int i = 1; i < LEN; ++i) {
        p[i] = PRIME * p[i - 1];
    }
    int l = -1;
    int r = INF;
    for (int i = 0; i < k; ++i) {
        std::cin >> str[i];
        auto s = str[i];
        r = std::min(r, (int)s.size() + 1);
        h[i].resize(s.size() + 1);
        h[i][0] = 0;
        for (int j = 1; j < h[i].size(); ++j) {
            h[i][j] = h[i][j - 1] * PRIME + s[j - 1];
        }
    }
    std::string res;
    while (r - l > 1) {
        int m = (l + r) / 2;
        std::string s = find_common_substr(m);
        if (!s.empty() or !m) {
            res = s;
            l = m;
        } else {
            r = m;
        }
    }
    std::cout << res;
 
    return 0;
}
