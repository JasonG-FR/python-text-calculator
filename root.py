from sys import exit
exit("Please do not run this file `root.py' directly. Use `import root' or `from root import <whatever>' instead.")
def cubeInternal(x):
    # all credit goes to user4466285's answer to "https://stackoverflow.com/questions/28014241/how-to-find-cube-root-using-python"
    if 0 <= x: 
        return x**(1./3.)
    return -(-x)**(1./3.)
def cu():
    print(cubeInternal(int(input("Number to be rooted? "))))
