#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int h, w;
    cin >> h >> w;

    vector<int> arr(w);
    for (int i = 0; i < w; i++)
    {
        cin >> arr[i];
    }

    int sum = 0;

    for (int i = 1; i < w - 1; i++)
    {
        int left_max = *max_element(arr.begin(), arr.begin() + i);
        int right_max = *max_element(arr.begin() + i + 1, arr.end());

        int min_height = min(left_max, right_max);

        if (arr[i] < min_height)
        {
            sum += min_height - arr[i];
        }
    }

    printf("%d", sum);
}