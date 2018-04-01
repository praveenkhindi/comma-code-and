#Say you have a list value like this:
#spam = ['apples', 'bananas', 'tofu', 'cats']
#Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space, with and inserted before the last item.
#But your function should be able to work with any list value passed to it.

spam= ['apples', 'bananas', 'tofu', 'cats']
def spam_func(list):
    newString = ''
    for i in spam:
        newString = newString + str(i)
        if list.index(i) == (len(list)-2):
                newString = newString + ' and '
        elif list.index(i) == (len(list)-1):
                newString = newString
        else:
            newString = newString + ','
    return newString
print(spam_func(spam))
