#include <bits/stdc++.h>

using namespace std;

/*
   ========== MERGE SORT ==========
*/

vector<int> merge_sort (vector<int> arr)
{
    if(arr.size() <= 1)
        return arr;

    // DIVIDE

    int mid  = arr.size() / 2;

    vector<int>left_half;
    vector<int>right_half;

    for(int i = 0; i < mid; i++)
        left_half.push_back(arr[i]);
    for(int i = mid; i < arr.size(); i++)
        right_half.push_back(arr[i]);

    vector<int>sorted_left = merge_sort(left_half);
    vector<int>sorted_right = merge_sort(right_half);

    // CONQUER
    vector<int>sorted_arr;
    int idx1 = 0,idx2 = 0;

    for(int i = 0; i < arr.size() ;i++){

        if(idx1 == sorted_left.size())
        {
            sorted_arr.push_back(sorted_right[idx2]);
            idx2++;

        }
        else if (idx2 == sorted_right.size())
        {
            sorted_arr.push_back(sorted_left[idx1]);
            idx1++;
        }

        else if(sorted_left[idx1] < sorted_right[idx2])
        {
            sorted_arr.push_back(sorted_left[idx1]);
            idx1++;
        }
        else
        {
            sorted_arr.push_back(sorted_right[idx2]);
            idx2++;
        }
    }


    return sorted_arr;

}


int main () {

    vector<int>a = {5, 3, 7, 1, 8, 9};
    vector<int> ans = merge_sort(a);

    for(int i = 0; i < ans.size(); i++){
        cout << ans[i] << " ";
    }

    return 0;
}
