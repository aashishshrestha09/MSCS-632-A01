#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Comparison function used by qsort for integer sorting
int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

// Calculate the mean (average) of the data array
double calculate_mean(int data[], int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) 
        sum += data[i];
    return (double)sum / n;
}

// Calculate the median of the data array
// Sorts the array and returns middle value or average of two middles
double calculate_median(int data[], int n) {
    qsort(data, n, sizeof(int), compare);
    if (n % 2 == 0)
        return (data[n/2 - 1] + data[n/2]) / 2.0;
    else
        return data[n/2];
}

// Calculate and print mode(s) of the data array
// Finds the value(s) that appear most frequently
void calculate_mode(int data[], int n) {
    int maxCount = 0, count;
    int modes[100], modeIndex = 0;

    for (int i = 0; i < n; i++) {
        count = 1;
        for (int j = i+1; j < n; j++)
            if (data[j] == data[i]) count++;

        if (count > maxCount) {
            maxCount = count;
            modeIndex = 0;
            modes[modeIndex++] = data[i];
        } else if (count == maxCount && count > 1) {
            modes[modeIndex++] = data[i];
        }
    }

    if (maxCount > 1) {
        printf("Mode(s): ");
        for (int i = 0; i < modeIndex; i++)
            printf("%d ", modes[i]);
        printf("(appeared %d times)\n", maxCount);
    } else {
        printf("No mode (all unique values)\n");
    }
}

// Find minimum value in data array
int find_min(int data[], int n) {
    int min = data[0];
    for (int i = 1; i < n; i++)
        if (data[i] < min) min = data[i];
    return min;
}

// Find maximum value in data array
int find_max(int data[], int n) {
    int max = data[0];
    for (int i = 1; i < n; i++)
        if (data[i] > max) max = data[i];
    return max;
}

// Calculate standard deviation of the data array
double calculate_std_dev(int data[], int n, double mean) {
    double sum = 0.0;
    for (int i = 0; i < n; i++)
        sum += (data[i] - mean) * (data[i] - mean);
    return sqrt(sum / n);
}

int main() {
    // Sample data array
    int data[] = {5, 2, 9, 5, 7, 9};
    int n = sizeof(data) / sizeof(data[0]);

    double mean = calculate_mean(data, n);
    printf("Mean: %.2f\n", mean);

    printf("Median: %.2f\n", calculate_median(data, n));

    calculate_mode(data, n);

    int min = find_min(data, n);
    int max = find_max(data, n);
    printf("Min: %d\n", min);
    printf("Max: %d\n", max);
    printf("Range: %d\n", max - min);

    printf("Standard Deviation: %.2f\n", calculate_std_dev(data, n, mean));

    return 0;
}
