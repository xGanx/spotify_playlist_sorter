from typing import List

class IntegerContainerImpl():

    def __init__(self, container: List[int] = None, dec=0):
        # TODO: implement
        if container is None:
            container = []
        self.container = container

    # TODO: implement interface methods here
    def add(self, value: int) -> int:
        """
        Should add the specified integer `value` to the container
        and return the number of integers in the container after the
        addition.
        """
        self.container.append(value)
        
        # default implementation
        return len(self.container)

    def delete(self, value: int) -> bool:
        """
        Should attempt to remove the specified integer `value` from
        the container.
        If the `value` is present in the container, remove it and
        return `True`, otherwise, return `False`.
        """
        # default implementation
        if value in self.container:
            self.container.remove(value)
            return True
        return False

def main():
    asd = IntegerContainerImpl()
    
    print('hi')
    asd.add(5)
    print(asd.container)
    asd.delete(1)
    print(asd.container)
    asd.delete(5)
    asd.add(1)
    
    abc = IntegerContainerImpl()
    print(f'new container {abc.container}')
    
    print(asd.container)
    
    print(11//2)
    
if __name__ == '__main__':
    main()