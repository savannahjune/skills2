string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "Sam", "I", "am"]

"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""

# can use item in items to count individual letters
def count_unique(string1):
    uniquedict = {}
    for word in words:
    	if word not in uniquedict:
    		uniquedict[word] = 1
    	else: 
    		uniquedict[word] += 1
    return uniquedict
count_unique(string1)

"""
Given two lists, (without using the keywords 'if __ in ____' or the method 'index')
return a list of all common items shared between both lists
"""
def common_items(list1, list2):
#     uniquedict1 = {}
#     uniquedict2 = {}
#     commondict = {}
#     for item in list1:
#     	if item not in uniquedict1:
#     		uniquedict1[item] = 1
#     	else: 
#     		uniquedict1[item] += 1
 
#     for item in list2:
#     	if item not in uniquedict2:
#     		uniquedict2[item] = 1
#     	else: 
#     		uniquedict2[item] += 1

#     for key in uniquedict1:
#     	if key in uniquedict2:
#     		commondict[key] = 1
#     	else:
#     		continue
#     return commondict.keys()
# common_items(list1, list2)

# learning to use set 

	uniquelist1 = set(list1)
	uniquelist2 = set(list2)
	return list(uniquelist1 & uniquelist2)
# print common_items(list1, list2)

"""
Given two lists, (without using 'if __ in ____' or 'index'
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""
def common_items2(list1, list2):
    uniquedict1 = {}
    uniquedict2 = {}
    commondict = {}
    for item in list1:
    	if item not in uniquedict1:
    		uniquedict1[item] = 1
    	else: 
    		uniquedict1[item] += 1
    print uniquedict1
    for item in list2:
    	if item not in uniquedict2:
    		uniquedict2[item] = 1
    	else: 
    		uniquedict2[item] += 1
    print uniquedict2

    for key in uniquedict1:
    	if key in uniquedict2:
    		commondict[key] = 1
    	else:
    		continue
    return commondict.keys()
common_items(list1, list2)

"""
Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(list1):
    sumzerolist = []
    for i in range(len(list1)):
    	for index in range(len(list1[i:])):
    		if list1[i] + list1[index] == 0:
    			sumzerolist.append((list1[i], list1[index]))
    return sumzerolist

# print sum_zero(list1)


"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
    return list(set(words))

# print find_duplicates(words)

"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""
def word_length(words):
    word_dict = {}
    opp_word_dict = {}

    # make dictionary with words as keys and value is length of word
    # it's very luck that green eggs and ham ascends in length of word by its nature

    for item in words:
    	word_dict[item] = len(item)
    for key, value in word_dict.iteritems():
    	opp_word_dict[value] = opp_word_dict.get(value, []) + [key]

    return opp_word_dict

    	# if value not in opp_word_dict:
    	# 	opp_word_dict[value] = [key]
    	# else:
    	# 	opp_word_dict[value].append(key)


   	# print opp_word_dict
  

    # for i range(len(word_dict)):
    # 	word = word_dict[i][0]
    # 	count = word_dict[i][1]
    # 	word_dict_tuple_time.append((count, word))

    # sort_word_dict = sorted(word_dict_tuple_time)

    # for i in range(len(sort_word_dict)):
    	# print sort_word_dict[i][1], sort_word_dict[i][0]

print word_length(words)


"""
Here's a table of English to Pirate translations
English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey

Write a program that asks the user to type in a sentence and then
print the sentece translated to pirate.
"""

def pirate_translate():
	pass
