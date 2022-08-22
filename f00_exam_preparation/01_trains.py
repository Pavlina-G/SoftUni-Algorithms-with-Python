arrivals_time = sorted(list(map(float, input().split())))
departures_time = sorted(list(map(float, input().split())))

trains_count = 0
platforms_count = 0

a_index = 0
d_index = 0

while a_index < len(arrivals_time):
    if arrivals_time[a_index] < departures_time[d_index]:
        trains_count += 1
        platforms_count = max(platforms_count, trains_count)
        a_index += 1

    else:
        trains_count -= 1
        d_index += 1

print(platforms_count)
