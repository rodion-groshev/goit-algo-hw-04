import timeit
import random
from insertion_sort import insertion_sort
from merge_sort import merge_sort

small_data = [random.randint(0, 10_000) for _ in range(1000)]
medium_data = [random.randint(0, 10_000) for _ in range(5000)]
large_data = [random.randint(0, 10_000) for _ in range(10000)]

if __name__ == "__main__":
    small_insertion = timeit.timeit(lambda: insertion_sort(small_data), number=3)
    small_merge = timeit.timeit(lambda: merge_sort(small_data), number=3)
    small_sort = timeit.timeit(lambda: small_data[:].sort(), number=3)

    medium_insertion = timeit.timeit(lambda: insertion_sort(medium_data), number=3)
    medium_merge = timeit.timeit(lambda: merge_sort(medium_data), number=3)
    medium_sort = timeit.timeit(lambda: medium_data[:].sort(), number=3)

    large_insertion = timeit.timeit(lambda: insertion_sort(large_data), number=3)
    large_merge = timeit.timeit(lambda: merge_sort(large_data), number=3)
    large_sort = timeit.timeit(lambda: large_data[:].sort(), number=3)

    print(f"| {'Algorithm':<20} | {'Small':<20} | {'Medium':<20} | {'Large':<20} |")
    print(f"| {'-' * 20} | {'-' * 20} | {'-' * 20} | {'-' * 20} |")
    print(f"| {'Insertion Sort':<20} | {small_insertion:20.5f} | {medium_insertion:20.5f} | {large_insertion:20.5f} |")
    print(f"| {'Merge Sort':<20} | {small_merge:20.5f} | {medium_merge:20.5f} | {large_merge:20.5f} |")
    print(f"| {'Timsort':<20} | {small_sort:20.5f} | {medium_sort:20.5f} | {large_sort:20.5f} |")
