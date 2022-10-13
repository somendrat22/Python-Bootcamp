#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

# https://www.hackerrank.com/challenges/whats-your-name/problem

def print_full_name(first, last):
    # %s represents string 
    # %d represents integre
    # %f represents  float 
    print("Hello %s %s! You just delved into python." %(first, last))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)