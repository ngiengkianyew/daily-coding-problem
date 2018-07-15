class SampleClass:
    instances = dict()
    even_instance = False

    def __init__(self, instance_num):
        self.instance_num = instance_num

    @staticmethod
    def initialize():
        SampleClass.instances[0] = SampleClass(0)
        SampleClass.instances[1] = SampleClass(1)

    @staticmethod
    def get_instance():
        if not SampleClass.instances:
            SampleClass.initialize()

        SampleClass.even_instance = not SampleClass.even_instance
        return SampleClass.instances[int(SampleClass.even_instance)]


# Tests


SampleClass.initialize()

i1 = SampleClass.get_instance()
assert i1.instance_num == 1
i2 = SampleClass.get_instance()
assert i2.instance_num == 0
i3 = SampleClass.get_instance()
assert i3.instance_num == 1
i4 = SampleClass.get_instance()
assert i4.instance_num == 0
i5 = SampleClass.get_instance()
assert i5.instance_num == 1
