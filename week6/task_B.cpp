#include <iostream>
#include <algorithm>
#include <vector>
 
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    int n, m;
    std::cin >> n >> m;
    std::vector<char> answer;
    std::vector<std::vector<int>> cur(n, std::vector<int>(m, 1));
    std::vector<std::vector<int>> cnt(n, std::vector<int>(m, 0));
 
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            std::cin >> cur[i][j];
        }
    }
 
    cnt[0][0] = cur[0][0];
    for (int i = 1; i < m; ++i) {
        cnt[0][i] = cnt[0][i - 1] + cur[0][i];
    }
 
    for (int i = 1; i < n; ++i) {
        cnt[i][0] = cnt[i - 1][0] + cur[i][0];
    }
 
    for (int i = 1; i < n; ++i) {
        for (int j = 1; j < m; ++j) {
            if (cnt[i][j - 1] >= cnt[i - 1][j]) {
                cnt[i][j] = cur[i][j] + cnt[i][j - 1];
            } else {
                cnt[i][j] = cur[i][j] + cnt[i - 1][j];
            }
        }
    }
 
    int i = n - 1;
    int j = m - 1;
    while (i > 0 && j > 0) {
        if (cnt[i][j - 1] > cnt[i - 1][j]) {
            answer.push_back('R');
            j -= 1;
        } else {
            answer.push_back('D');
            i -= 1;
        }
    }
    while (i > 0) {
        answer.push_back('D');
        i -= 1;
    }
    while (j > 0) {
        answer.push_back('R');
        j -= 1;
    }
 
    std::cout << cnt[n - 1][m - 1] << std::endl;
    for (int k = answer.size() - 1; k >= 0; --k) {
        std::cout << answer[k];
    }
 
    return 0;
}
