import ctypes


class DynamicArray(object):

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        if not 0 <= k < self.n:
            return IndexError('K is out of bounds!')
        return self.A[k]

    def append(self, ele):

        #Here, we are checking the capacity
        if self.n == self.capacity:
            ## If the array is at capacity, we will double the size.
            self.__resize(2*self.capacity)
        
        self.A[self.n] = ele
        self.n += 1

    def _resize(self, new_cap):

        B = self.make_array(new_cap)
        #This is moving the references from a, to b
        for k in range(self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_cap

    def make_array(self, new_cap):

        return (new_cap * ctypes.py_object)()



def main():
    arr = DynamicArray()
    arr.append(['Things!!', "things"])
    print(len(arr))
    print(arr[0])


if __name__ == '__main__':
    main()

        