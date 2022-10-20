'''Problem
Chef has 33 numbers A,B and C.

Chef wonders if it is possible to choose exactly two numbers out of the three numbers such that their sum is odd.

Input Format
The first line of input will contain a single integer TT, denoting the number of test cases.
Each test case consists of three integers A, B, CA,B,C.
Output Format
For each test case, output YES if you can choose exactly two numbers with odd sum, NO otherwise.

The output is case-insensitive. Thus, the strings YES, yes, yeS, and Yes are all considered the same.

Constraints
1 \leq T \leq 1001≤T≤100
1 \leq A, B, C \leq 101≤A,B,C≤10

Sample 1:

Input
4
1 2 3
8 4 6
3 3 9
7 8 6

Output:

YES
NO
NO
YES
Explanation:
Test case 1: Chef can choose 22 and 33 since 2 + 3 = 52+3=5 and 55 is odd.

Test case 2: It can be shown that Chef cannot choose two numbers among 88, 44 and 66 with odd sum.

'''
#code

for i in range(int(input())):
    a,b,c=map(int,input().split())
    if (a+b)%2!=0 or (b+c)%2!=0 or (a+c)%2!=0:
        print('yes')
    else:
        print('no')
