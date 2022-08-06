#include <iostream>
#include <algorithm>
 
const int MAX_N = int(1e7);
 
int arr_a[MAX_N];
uint64_t arr_t[MAX_N + 1];
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    int n, x, y;
    std::cin >> n >> x >> y >> arr_a[0];
    arr_t[0] = 0;
 
    for (size_t i = 1; i < n; ++i) {
        arr_a[i] = (x * arr_a[i - 1] + y) % (1 << 16);
        arr_t[i] = arr_t[i - 1] + arr_a[i - 1];
    }
 
    arr_t[n] = arr_t[n - 1] + arr_a[n - 1];
    int m, z, t;
    uint64_t b_last, b_cur;
    int c_last, c_cur;
    std::cin >> m >> z >> t >> b_last;
    c_last = b_last % n;
    uint64_t sum = 0;
    
    for (size_t i = 1; i < 2 * m; ++i) {
        b_cur = (z * b_last + t) % (1 << 30);       
        c_cur = b_cur % n;
        if (i % 2 == 1) {
            sum += arr_t[std::max(c_cur, c_last) + 1] - arr_t[std::min(c_cur, c_last)];
        }
        b_last = b_cur;
        c_last = c_cur;
    }
    std::cout << sum << std::endl;
 
    return 0;
}
