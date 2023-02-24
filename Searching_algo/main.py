#twitter/linkdin/github - DixitDhiman144

#Implementation of linear & binary search algorithm!!

#Linear search / native search : scan the intire lish and ask if its match to the target
# if it's match then return index otherwise -1
def linear_search(list_, target):
    for i in range(len(list_)):
        if target == list_[i]:
            return i + 1
    return -1
        

#Binary search for binary search we needs to short the list
#binary search uses divide and conquer!
#we will leverage the fact that ur list is sorted
def binary_search(list_, target):
    mid_point = len(list_)//2
    if list_[mid_point] == target:
        return mid_point + 1
    elif list_[mid_point] > target:
        return binary_search(list_[:mid_point], target)
    else: #list_[mid_point] < target
        return binary_search(list_[mid_point+1:], target)

#Another way
def binary_search_(list_, target, low= None, high= None):
    if low is None and high is None:
        low = 0
        high = len(list_)
    
    if low > high:
        return -1
    
    mid_point = (low + high) //2
    if list_[mid_point] == target:
        return mid_point + 1
    elif list_[mid_point] > target:
        return binary_search_(list_, target, low, high= mid_point-1) #low= 0 already define
    else: #list_[mid_point < target]
        return binary_search_(list_, target, mid_point+1, high) #high= len(target)

if __name__ == "__main__":
    example_list = [1,2,4,5,6,7,8,11,15,16,22,25]
    example_target = 5
    print(linear_search(example_list, example_target))
    print(binary_search(example_list, example_target))
    print(binary_search_(example_list, example_target))