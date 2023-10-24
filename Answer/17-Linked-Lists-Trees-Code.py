class Link:
	empty = ()
	def __init__(self, first, rest=empty):
		assert rest is Link.empty or isinstance(rest, Link)
		self.first = first
		self.rest = rest

def sum_link(link):
	if link is Link.empty:
		return 0
	return link.first + sum_link(link.rest)

def display_nested_link(link):
	str_num = ''
	while link is not Link.empty:
		if isinstance(link.first, Link):
			elem = display_nested_link(link.first)
		else:
			elem = str(link.first)
		str_num += elem + ' '
		link = link.rest
	return '< ' + str_num + '>'

def map_link(f, link):
	if link is not Link.empty:
		return Link(f(link.first), map_link(f, link.rest))
	else:
		return Link.empty


