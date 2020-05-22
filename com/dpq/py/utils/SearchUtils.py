import multiprocessing as mp


class SearchUtil:

    @staticmethod
    def linearsearch(list1, num):
        print("linearsearch called")
        for x in list1:
            if x == num:
                return True
        else:
            return False

    @staticmethod
    def optimizedSearch(list1, num):
        print("optimizedSearch called")
        n = len(list1)
        front, back = 0, n - 1

        while front <= back:
            if list1[front] == num or list1[back] == num:
                return True
            front += 1
            back -= 1
        else:
            return False


if __name__ == '__main__':
    # Linear search time complexity for worst case is o(n)
    print(SearchUtil.linearsearch([1, 23, 45, 23, 12, 0, 4, 2], 23))
    print(SearchUtil.linearsearch([1, 23, 45, 23, 12, 0, 4, 2], 25))
    # The worst case complexity is O(n / 2)(equivalent to O(n)) when element is in the middle or not present in the
    # array.
    # The best case complexity is O(1) when element is first or last element in the array.
    print(SearchUtil.optimizedSearch([1, 23, 45, 23, 12, 0, 4, 2], 23))
    print(SearchUtil.optimizedSearch([1, 23, 45, 23, 12, 0, 4, 2], 25))

    # Distributed way to find elements
    pool = mp.Pool(mp.cpu_count())
    print("no of CPUs: ", mp.cpu_count())
    results = [pool.apply(SearchUtil.linearsearch, args=([1, 23, 45, 23, 12, 0, 4, 2], 25))]
    print("Parallel results:", results)

    results = [pool.apply(SearchUtil.linearsearch, args=([1, 23, 45, 23, 12, 0, 4, 2], 23))]
    print("Parallel results:", results)
    pool.close()
