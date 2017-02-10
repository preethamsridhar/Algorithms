noOfPermute = 0
def permute(word, low, high):
    global noOfPermute   # to count the number of permutations of the string
    if low == high:
        print("".join(n for n in word))
        noOfPermute +=1
    else:
        for i in range(low, high):
            word[i], word[low] = word[low], word[i]  # swap the 
            permute(word, low+1, high)
            word[i], word[low] = word[low], word[i]


name = ['A','B','C','D']
print("The permutations")
permute(name, 0, len(name))
print("No of permutation: ",noOfPermute)





