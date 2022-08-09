#include <iostream>
#include <algorithm>
 
const int MAX_N = int(1e5);
const int POW_N = 17; // 2^17 = 131072
 
int arr_a[MAX_N + 1];
int arr_sparse[MAX_N + 1][POW_N];
 
int request(int l, int r) {
    int i = 0;
    int s = 1;
    while (s <= r - l + 1) {
        i += 1;
        s *= 2;
    }
    int k = i - 1;
    return std::min(arr_sparse[l][k], arr_sparse[r - (1 << k) + 1][k]);
}
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
    
    int n, m, a1, u1, v1;
    std::cin >> n >> m >> a1 >> u1 >> v1;
    arr_a[1] = a1;
    
    for (int i = 2; i <= n; ++i) {
        arr_a[i] = (23 * arr_a[i - 1] + 21563) % 16714589;
    }
 
    for (int i = 1; i <= n; ++i) {
        arr_sparse[i][0] = arr_a[i];
    }
 
    for (int j = 1; j < POW_N; ++j) {
        int k = 1 << (j - 1);
        for (int i = 1; i <= MAX_N + 1; ++i) {
            if (i + k > -1 && i + k < MAX_N + 1) {
                arr_sparse[i][j] = std::min(arr_sparse[i][j - 1], arr_sparse[i + k][j - 1]);
            }
        }
    }
    
    int u2, v2, res1, res2;
    res1 = request(std::min(u1, v1), std::max(u1, v1));
    for (int i = 1; i < m; ++i) {
        u2 = ((17 * u1 + 751 + res1 + 2 * i) % n) + 1;
        v2 = ((13 * v1 + 593 + res1 + 5 * i) % n) + 1;
        u1 = u2;
        v1 = v2;
        res2 = request(std::min(u2, v2), std::max(u2, v2));
        res1 = res2;
    }
    std::cout << u1 << " " << v1 << " " << res1 << std::endl;
    
    return 0;
}
