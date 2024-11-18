def age_group_frequency_simple(ages, range_size=10):
    ranges = [f"{i}-{i + range_size - 1}" for i in range(0, max(ages) + 1, range_size)]
    freq = {r: 0 for r in ranges}

    for age in ages:
        for r in freq:
            start, end = map(int, r.split('-'))
            if start <= age <= end:
                freq[r] += 1

    for age_range, count in freq.items():
        print(f"{age_range}: {count}")


ages = [5, 12, 17, 25, 30, 5, 45, 22, 30, 34, 29, 18, 40, 28]
age_group_frequency_simple(ages)