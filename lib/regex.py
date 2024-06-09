import re

my_pattern = r""
my_regex = re.compile(my_pattern)

my_regex = re.compile(r"^[A-Z][\w\s',’-]*[?.]$", re.MULTILINE)