from collections import Counter
from math import sqrt

class StatisticsCalculator:
    """Calculates various statistics on a list of integers."""

    def __init__(self, data):
        """Initialize with the data list."""
        self.data = data

    def calculate_mean(self):
        """Return the mean (average) of the data."""
        return sum(self.data) / len(self.data)

    def calculate_median(self):
        """Return the median value of the data."""
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 0:
            return (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
        else:
            return sorted_data[n//2]

    def calculate_mode(self):
        """Return mode(s) and their frequency if they exist, else None."""
        frequency = Counter(self.data)
        max_count = max(frequency.values())
        modes = [k for k, v in frequency.items() if v == max_count and v > 1]
        if modes:
            return modes, max_count
        else:
            return None, None

    def find_min(self):
        """Return minimum value in data."""
        return min(self.data)

    def find_max(self):
        """Return maximum value in data."""
        return max(self.data)

    def calculate_std_dev(self, mean):
        """Return standard deviation of data based on mean."""
        variance = sum((x - mean) ** 2 for x in self.data) / len(self.data)
        return sqrt(variance)

if __name__ == "__main__":
    data = [5, 2, 9, 5, 7, 9]
    stats = StatisticsCalculator(data)

    mean = stats.calculate_mean()
    print(f"Mean: {mean:.2f}")
    print(f"Median: {stats.calculate_median():.2f}")
    modes, count = stats.calculate_mode()
    if modes:
        print(f"Mode(s): {modes} (appeared {count} times)")
    else:
        print("No mode (all unique values)")
    print(f"Min: {stats.find_min()}")
    print(f"Max: {stats.find_max()}")
    print(f"Range: {stats.find_max() - stats.find_min()}")
    print(f"Standard Deviation: {stats.calculate_std_dev(mean):.2f}")
