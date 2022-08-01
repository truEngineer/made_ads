#include <iostream>
#include <algorithm>
 
 
const int INF = int(1e9);
 
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    int n, max_len = 0;
    std::cin >> n;
    int arr[n], d[n + 1];
    int pos[n], prev[n];
    for (int i = 0; i < n; ++i) {
        std::cin >> arr[i];
    }
    d[0] = -INF - 1;
    for (int i = 1; i < n + 1; ++i) {
        d[i] = INF + 1;
    }
 
    for (int i = 0; i < n; ++i) {
        if (d[n] > arr[i]) {
            int l = 0, r = n;
            while (l < r) {
                int m = (l + r) / 2;
                if (d[m] < arr[i]) {
                    l = m + 1;
                } else {
                    r = m;
                }
            }
            if (l < n + 1) {
                d[l] = arr[i];
                max_len = std::max(max_len, l);
                pos[l] = i;
                prev[i] = pos[l - 1];
            }
        }
    }
 
    std::cout << max_len << std::endl;
    int p = pos[max_len];
    int res[max_len];
    for (int i = 0; i < max_len; ++i) {
        res[i] = arr[p];
        p = prev[p];
    }
    for (int i = max_len - 1; i >= 0; --i) {
        std::cout << res[i] << " ";
    }
 
    return 0;
}
