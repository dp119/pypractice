

# Remove duplicates from a list

# sol1
test_list = [2, 4, 10, 20, 5, 2, 20, 4]


def Remove(test_list):
    final_test_list = []
    for num in test_list:
        if num not in final_test_list:
            final_test_list.append(num)
    return final_test_list


print(Remove(test_list))


# sol2
# converting into set


A = list(set(test_list))
print(A)



# sol3
# converting into dictionary

mylist = ["a", "b", "a", "c", "c"]
mylist = list( dict.fromkeys(mylist) )      #using list elements as keys for dictionary
print(mylist)