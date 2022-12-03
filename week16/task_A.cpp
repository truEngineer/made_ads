#include <iostream>
#include <cmath>
 
long x1, y1, x2, y2, x3, y3;
 
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);
 
    std::cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;
    if( (x1 < x2 && x1 < x3) || (y1 < y2 && y1 < y3))
        std::cout << "NO";
    else if( (x1 > x2 && x1 > x3) || (y1 > y2 && y1 > y3))
        std::cout << "NO";
    else {
        double ans = abs(((x1 * y2 - x2 * y1) + 
                          (x2 * y3 - x3 * y2) + 
                          (x3 * y1 - x1 * y3)) / 2.0);
        std::cout << (ans == 0 ? "YES" : "NO");
    }
    
    return 0;
}
