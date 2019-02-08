class UnitConverter:
    def __init__(self):
        self.conv_unit = None
        self.units = dict()

    def add_unit(self, unit_tuple, quantities):
        (known_unit, new_unit) = unit_tuple
        if not self.conv_unit:
            self.conv_unit = known_unit
            self.units[known_unit] = 1

        assert known_unit in self.units or unit_tuple[1] in self.units
        self.units[new_unit] = \
            (quantities[1] / quantities[0]) * \
            self.units[known_unit]

    def convert(self, source_unit, source_quantity, target_unit):
        assert source_unit in self.units and target_unit in self.units
        source_conv = source_quantity / self.units[source_unit]
        return round(source_conv * self.units[target_unit], 2)


# Tests
uc = UnitConverter()
uc.add_unit(("inch", "foot"), (12, 1))
uc.add_unit(("foot", "yard"), (3, 1))
uc.add_unit(("yard", "chain"), (22, 1))
assert uc.convert("inch", 24, "foot") == 2.0
assert uc.convert("inch", 36, "yard") == 1
assert uc.convert("inch", 48, "yard") == 1.33
assert uc.convert("foot", 4, "yard") == 1.33
assert uc.convert("chain", 2, "inch") == 1584.0
assert uc.convert("chain", 3, "foot") == 198.0
