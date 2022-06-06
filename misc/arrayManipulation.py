# Compare two lists and eliminate common elements in place
def removeCommonElements(list1, list2):
    common_elements = []
    for element in list1:
        if element in list2:
            common_elements.append(element)
    for element in common_elements:
        list1.remove(element)
        list2.remove(element)
    return