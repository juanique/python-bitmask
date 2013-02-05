class BitMaskOptions(object):

    def __init__(self, options):

        self._current = -1
        self.options = {}
        self.keys = options

        for i in range(len(options)):
            option = options[i]
            self.options[option] = 1 << i
            setattr(self, option, option)

    def get_int(self, opt):
        return self.options[opt]

    def __iter__(self):
        return self

    def next(self):
        if self._current >= len(self.keys) - 1:
            self._current = -1
            raise StopIteration
        else:
            self._current += 1
            return self.keys[self._current]

class BitMask(object):

    def __init__(self, options, value=0):
        if type(options) == list:
            options = BitMaskOptions(options)

        self.value = value
        self.options = options

    def has(self, opt):
        if type(opt) != int:
            opt = self.options.options[opt]
        return self.value & opt > 0

    def add(self, opt):
        if type(opt) != int:
            opt = self.options.options[opt]
        self.value = self.value | opt

    def set(self, opt, enabled):
        if type(opt) != int:
            opt = self.options.options[opt]

        if enabled:
            self.value = self.value | opt
        else:
            if self.has(opt):
                self.value = self.value ^ opt
