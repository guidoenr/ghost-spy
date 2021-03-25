import abc

class Module(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def run(self):
        pass

