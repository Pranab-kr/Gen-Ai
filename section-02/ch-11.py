# Advance datatype
# import arrow

# brew_time = arrow.utcnow()
# brew_time.to("Europe/Prague")

from collections import namedtuple

ChaiOrder = namedtuple("ChaiOrder", ["type", "size", "sugar_level"])

print(ChaiOrder(type="Masala", size="Large", sugar_level="Medium"))
