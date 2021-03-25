#File name-->
with open("--filenameHERE.txt", "r") as file:
    depth = len(file.readlines())
    file.seek(0)
    #creating a rows*column matrix for incoming input (each row will be equal to pyramid's row)
    rows, cols = (depth, depth)
    pyr = [[0 for i in range(cols)] for j in range(rows)]
    x=0 # this is for row
    for line in file: # columns for each row
        #I assumed there are no special characters in "filename.txt" file, so i use split method to split each number for our 2d array.
        data = line.split()
        length = len(data)
        for t in range(0,length,1):
            pyr[x][t] = int(data[t])

        #This is for first question. Char-by-char read to know input is digit(because there are special characters like *1) or not.
        #To avoid blank and special characters.
        #--------------------------------------------------------------------------------------------------------
        """
        t=0
        for character in line:
            if(character.isdigit()):
                pyr[x][t] = int(character)
                t+=1
        """
        #--------------------------------------------------------------------------------------------------------
        
        x+=1
#if we reverse the pyramid like bottom to top and top to bottom. Pyramid's New top will be our former bottom line.
#so that'll help us to solve the summation with less complexity
#P.S. : We could use 1d array to solve that problem. In that case, we'd to find the formula to reach each rows starting number
def pyrsum(pyr,depth):
    for i in range(depth-2, -1, -1):
        for j in range(i+1):
            if(isprime(pyr[i][j]) == False):#If the number is prime we've to skip it. If the given number isn't prime, we can add the bigger one to the next line.
                if (pyr[i+1][j] > pyr[i+1][j+1]):
                    pyr[i][j] += pyr[i+1][j]
                else:
                    pyr[i][j] += pyr[i+1][j+1]
    print(pyr[0][0])

def isprime(num):
    #assuming the "num" is positive integer. Otherwise we've to use abs function to abstract the number. with "num = abs(num)"
    if(num > 2):
        for k in range(2, int(num/2)+1):
            if (num % k) == 0:
                return False
    elif(num == 2):
        return True
    else:
        return False

#function call
pyrsum(pyr,depth)
