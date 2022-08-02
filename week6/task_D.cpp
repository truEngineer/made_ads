
#include <iostream>
#include <algorithm>
 
 
const int SIZE = 1001;
 
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    int n, m;
    std::string str1, str2;
    std::cin >> str1;
    std::cin >> str2;
    n = str1.length();
    m = str2.length();
    int mat[SIZE][SIZE];
    for (int i = 1; i <= m; ++i) {
        mat[i][0] = i;
    }
    for (int j = 1; j <= n; ++j) {
        mat[0][j] = j;
    }
    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; ++j) {
            int k = 1;
            if (str1[j - 1] == str2[i - 1]) {
                k = 0;
            }
            mat[i][j] = std::min(mat[i - 1][j], mat[i][j - 1]) + 1;
            mat[i][j] = std::min(mat[i][j], mat[i - 1][j - 1] + k);
        }
    }
    std::cout << mat[m][n];
 
    return 0;
}
