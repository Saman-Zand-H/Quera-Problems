def sort_dependencies(packages: dict, package_name: str):
	assert isinstance(packages, dict) and isinstance(package_name, str)
	deps = []
	visited = set()
	package_dependencies = []
	queue = [package_name]

	while queue:
		current = queue.pop(0)
		if current not in visited:
			visited.add(current)
			if current != package_name:
				deps.append(current)
			for d in packages.get(current, []):
				queue.append(d)

	def prep_ls(ls):
		seen = set()
		for i in ls:
			if i not in seen:
				seen.add(i)
				package_dependencies.append(i)
		package_dependencies.reverse()

	prep_ls(deps)
	print(package_dependencies)
	return package_dependencies


if __name__ == "__main__":
	sort_dependencies(dict(input()), str(input()))
