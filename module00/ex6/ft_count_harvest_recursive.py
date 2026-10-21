def ft_print_harvest_day(current_day: int, last_day: int):
	if current_day <= last_day:
		print(f"Day {current_day}")
		ft_print_harvest_day(current_day + 1, last_day)
	else:
		print("Harvest time!")

def ft_count_harvest_recursive():
	days_until_harvest = int(input("Days until harvest: "))
	ft_print_harvest_day(1, days_until_harvest)
