def compare(string1, string2):
	str_1 = list(string1)[::-1]
	str_2 = list(string2)[::-1]

	i = 0
	while str_1 and str_2:
		str_1.reverse()
		str_2.reverse()
		if str_1[0] < str_2[0]:
			del str_1[0]
		elif str_2[0] < str_1[0]:
			del str_2[0]
		else:
			del str_1[0]
			del str_2[0]

	if str_1:
		return "".join(str_1)
	elif str_2:
		return "".join(str_2)
	else:
		return "Both strings are empty!"
