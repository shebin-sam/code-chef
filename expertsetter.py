'''Problem
A problem setter is called an expert if at least 50 \%50% of their problems are approved by Chef.

Munchy submitted XX problems for approval. If YY problems out of those were approved, find whether Munchy is an expert or not.

Input Format
The first line of input will contain a single integer TT, denoting the number of test cases.
Each test case consists of a two space-separated integers XX and YY - the number of problems submitted and the number of problems that were approved by Chef.
Output Format
For each test case, output on a new line YES, if Munchy is an expert. Otherwise, print NO.

The output is case-insensitive. Thus, the strings YES, yes, yeS, and Yes are all considered the same.

Constraints
1 \leq T \leq 10001≤T≤1000
1 \leq Y \le X \leq 10^61≤Y≤X≤10 
6
 
Sample 1:
Input
4
5 3
1 1
4 1
2 1

Output

YES
YES
NO
YES
Explanation:
Test case 11: We are given that 33 out of 55 problems were approved. Thus, 60 \%60% of the problems were approved. Since at least 50 \%50% of the problems were approved, Munchy is an expert.

Test case 22: We are given that 11 out of 11 problems were approved. Thus, 100 \%100% of the problems were approved. Since at least 50 \%50% of the problems were approved, Munchy is an expert.

Test case 33: We are given that 11 out of 44 problems were approved. Thus, 25 \%25% of the problems were approved. Since at least 50 \%50% of the problems were not approved, Munchy is not an expert.

Test case 44: We are given that 11 out of 22 problems were approved. Thus, 50 \%50% of the problems were approved. Since at least 50 \%50% of the problems were approved, Munchy is an expert.'''

#code
for i in range(int(input())):
    a=list(map(int,input().split()))
    if a[1]/a[0] >=0.5:
        print('Yes')
    else:
        print('No')
