from datetime import datetime


class FactorHandler:
	def __init__(self):
		self.data = dict()

	def get_format_str(self, time_format:str):
		time_ls = time_format.split("/")
		time_ls[time_ls.index("yyyy")] = "%Y"
		time_ls[time_ls.index("mm")] = "%m"
		time_ls[time_ls.index("dd")] = "%d"
		return "/".join(time_ls)

	def append_dict(self, key, value):
		if not key in self.data:
			self.data[key] = [value]
		else:
			self.data[key].append(value)

	def add_factor(self, time_format, time, value):
		format_str = self.get_format_str(time_format)
		formatted_time = datetime.strptime(time, format_str)
		self.append_dict(formatted_time, value)

	def remove_all_factors(self, time_format, time):
		format_str = self.get_format_str(time_format)
		formatted_time = datetime.strptime(time, format_str)
		self.data.pop(formatted_time, None)

	def get_sum(self, time_format, start_time, finish_time):
		time_fmt = self.get_format_str(time_format)
		start_time_obj = datetime.strptime(start_time, time_fmt)
		finish_time_obj = datetime.strptime(finish_time, time_fmt)
		return (
			sum(
				[
					sum(v)
					for k, v in self.data.items() 
					if (k<=finish_time_obj and k>=start_time_obj)
				]
			)
		)


if __name__ == "__main__":
	fh = FactorHandler()
	fh.add_factor("dd/mm/yyyy", "02/10/2019", 10)
	fh.add_factor("dd/mm/yyyy", "03/10/2019", 10)
	fh.add_factor("dd/mm/yyyy", "03/10/2019", 20)
	fh.add_factor("dd/mm/yyyy", "05/10/2019", 5)
	print(fh.get_sum("yyyy/dd/mm", "2019/02/10", "2019/03/10")==60)
	fh.remove_all_factors("mm/dd/yyyy", "10/03/2019")
	print(fh.get_sum("yyyy/dd/mm", "2019/02/10", "2019/05/10")==15)
