#include <iostream>
#include <cstdlib>
#include <algorithm>
 
 
int partition(int arr[], int left, int right, int pivotind) {
    int pivot = arr[pivotind];
    std::swap(arr[pivotind], arr[right]);
    int pivotind_new = left;
    
    for (int i = left; i < right; ++i) {
        if (arr[i] <= pivot) {
            std::swap(arr[i], arr[pivotind_new]);
            pivotind_new++;
        }
    }
    
    std::swap(arr[pivotind_new], arr[right]);
    return pivotind_new;
}
 
int quickselect(int arr[], int left, int right, int k) {
    if (left == right)
        return arr[left];
 
    int pivotind = left + std::rand() % (right - left + 1);
    pivotind = partition(arr, left, right, pivotind);
 
    // pivot is in its final position
    if (k == pivotind)
        return arr[k];
    // k is less than the pivot index
    else if (k < pivotind)
        return quickselect(arr, left, pivotind - 1, k);
    // k is more than the pivot index
    else
        return quickselect(arr, pivotind + 1, right, k);
}
 
int main() {
    int n;
    std::cin >> n;
    int iq_arr[n];
    for (int q = 0; q < n; ++q)
        std::cin >> iq_arr[q];
    int m;
    std::cin >> m;
    
    for (int r = 0; r < m; ++r) {
    	// requests processing
    	int i, j, k;
    	std::cin >> i >> j >> k;
    	int size_slc = j - i + 1;
    	
    	int iq_slc[size_slc];
    	for (int s = 0; s < size_slc; ++s)
    		iq_slc[s] = iq_arr[i - 1 + s]; // i >= 1
    	
    	std::cout << quickselect(iq_slc, 0, size_slc - 1, k - 1) << std::endl; // k >= 1
    }
 
    return 0;
}
