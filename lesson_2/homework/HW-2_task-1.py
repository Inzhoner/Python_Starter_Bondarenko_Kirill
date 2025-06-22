# // Дані для розрахунку

distance_km = 250  # Відстань у кілометрах

speed_kmh = 80  # Швидкість у км/год

# @ Варіант-1

# hours = distance_km / speed_kmh  # розрахунок часів
#
# minutes = hours % 1 * 60  # розрахунок хвилин
#
# seconds = minutes % 1 * 60  # розрахунок секунд
#
# # // Виведення результату
# print(f"Час поїздки: {int(hours)} годин {int(minutes)} хвилин {int(seconds)} секунд")

# @ Варіант-2

hour = distance_km / speed_kmh  # розрахунок часів

total_seconds = hour * 3600  # розрахунов секунд загальних

hours = total_seconds // 3600  # розрахунок часів

minutes = (total_seconds % 3600) // 60  # розрахунок хвилин

seconds = total_seconds % 60  # розрахунок секунд

# // Виведення результату
print(f"Час поїздки: {int(hours)} годин {int(minutes)} хвилин {int(seconds)} секунд")
