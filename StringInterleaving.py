str1 = "axy"
str2 = "a"
strIL = "aaxy"
"""
String interleave is a task which needs dynamic programming,
We have to create 2 dimensional array which has 1 extra column and 1 extra row
"""

class Solution(object):
    @staticmethod
    def check_interleave(str1, str2, strIL):
        if len(strIL) == 0:
            print("\nstrIL = %s, is not the interleaving of str1 = %s and  str2 = %s " % (strIL, str1, str2))
        elif (len(str1) + len(str2)) != len(strIL):
            print("\nstrIL = %s, is not the interleaving of str1 = %s and  str2 = %s " % (strIL, str1, str2))
        else:
            # initializing the 2 dimensional array (il_dp = interleaving dynamic programming)
            il_dp = [[0]*(len(str1)+1) for i in range(len(str2)+1)]
            il_dp[0][0] = 1 # Initializing the two dimensional array's first element [0][0] to 1
            """
            The  2 dimensional array is not of the same size as either len of strings,
            It has one more extra element which has 1 written at [0][0]
            """
            # All the prints in the for loop are for the
            for i in range(len(str2)):
                print("\nFor i = ", i)
                for j in range(len(str1)):
                    print("\tFor j = ", j)
                    print("\t\tstrIL[%s] == str1[%s]" % ((i + j), j), "(%s == %s)" % (strIL[i + j], str1[j]))
                    if strIL[i+j] == str1[j]:
                        print("\t\t\til_dp[%s][%s] = il_dp[%s][%s] = %s" % (i, (j + 1), i, j, il_dp[i][j]))
                        il_dp[i][j+1] = il_dp[i][j]
                    else:
                        print("\t\t\til_dp[%s][%s] != il_dp[%s][%s] = %s" % (i, (j + 1), i, j, il_dp[i][j]))
                        pass
                    print("\t\tstrIL[%s] == str2[%s]" % ((i + j), i), "(%s == %s)" % (strIL[i + j], str2[i]))
                    if strIL[i+j] == str2[i]:
                        print("\t\t\til_dp[%s][%s] = il_dp[%s][%s] = %s" % ((i + 1), j, i, j, il_dp[i][j]))
                        il_dp[i+1][j] = il_dp[i][j]
                    else:
                        print("\t\t\til_dp[%s][%s] != il_dp[%s][%s] = %s" % ((i + 1), j, i, j, il_dp[i][j]))
                        pass

            """
            The last element of the 2 dimensional cannot be accessed from the for loop inside
            Have to create one extra checking.
            """
            if strIL[len(str2) + len(str1) - 1] == str1[len(str1) - 1]:
                il_dp[len(str2)][len(str1)] = il_dp[len(str2)][len(str1) - 1]
            if strIL[len(str2) + len(str1) - 1] == str2[len(str2) - 1]:
                il_dp[len(str2)][len(str1)] = il_dp[len(str2) - 1][len(str1)]


            """
            Print the dynamic programming array being used

            """
            print("\nDynamic Programming array used:  ")
            print("\033[91;1m   | 0 |", " | ".join(i for i in str1))
            print(" 0 |\033[0m"," | ".join(str(il_dp[0][i]) for i in range(len(str1)+1)))
            for i in range(0, len(str2)):
                print("\033[91;1m",str2[i],"|\033[0m"," | ".join(str(il_dp[i+1][j]) for j in range(len(str1)+1)))

            if il_dp[len(str2)][len(str1)] == 1:
                print("\nstrIL = %s, is the interleaving of str1 = %s and  str2 = %s " %(strIL, str1, str2))
            else:
                print("\nstrIL = %s, is not the interleaving of str1 = %s and  str2 = %s " % (strIL, str1, str2))

Solution.check_interleave(str1, str2, strIL)

"""
SAMPLE OUTPUT:

For i =  0
	For j =  0
		strIL[0] == str1[0] (a == a)
			il_dp[0][1] = il_dp[0][0] = 1
		strIL[0] == str2[0] (a == a)
			il_dp[1][0] = il_dp[0][0] = 1
	For j =  1
		strIL[1] == str1[1] (a == a)
			il_dp[0][2] = il_dp[0][1] = 1
		strIL[1] == str2[1] (a == x)
			il_dp[1][1] = il_dp[0][1] = 1
	For j =  2
		strIL[2] == str1[2] (x == b)
			il_dp[0][3] != il_dp[0][2] = 1
		strIL[2] == str2[2] (x == y)
			il_dp[1][2] != il_dp[0][2] = 1

For i =  1
	For j =  0
		strIL[1] == str1[0] (a == a)
			il_dp[1][1] = il_dp[1][0] = 1
		strIL[1] == str2[0] (a == a)
			il_dp[2][0] != il_dp[1][0] = 1
	For j =  1
		strIL[2] == str1[1] (x == a)
			il_dp[1][2] != il_dp[1][1] = 1
		strIL[2] == str2[1] (x == x)
			il_dp[2][1] = il_dp[1][1] = 1
	For j =  2
		strIL[3] == str1[2] (a == b)
			il_dp[1][3] != il_dp[1][2] = 0
		strIL[3] == str2[2] (a == y)
			il_dp[2][2] != il_dp[1][2] = 0

For i =  2
	For j =  0
		strIL[2] == str1[0] (x == a)
			il_dp[2][1] != il_dp[2][0] = 0
		strIL[2] == str2[0] (x == a)
			il_dp[3][0] != il_dp[2][0] = 0
	For j =  1
		strIL[3] == str1[1] (a == a)
			il_dp[2][2] = il_dp[2][1] = 1
		strIL[3] == str2[1] (a == x)
			il_dp[3][1] != il_dp[2][1] = 1
	For j =  2
		strIL[4] == str1[2] (y == b)
			il_dp[2][3] != il_dp[2][2] = 1
		strIL[4] == str2[2] (y == y)
			il_dp[3][2] = il_dp[2][2] = 1

Dynamic Programming array used:
   | 0 | a | a | b
 0 | 1 | 1 | 1 | 0
 a | 1 | 1 | 0 | 0
 x | 0 | 1 | 1 | 0
 y | 0 | 0 | 1 | 1

strIL = aaxayb, is the interleaving of str1 = aab and  str2 = axy

Process finished with exit code 0

"""