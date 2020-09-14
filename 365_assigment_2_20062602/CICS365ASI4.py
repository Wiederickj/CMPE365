#20062602
#Jackson Wiederick
#CISC 365 ASSIGNMENT 2

import random
import operator, math

#used to test various runtimes
'''
def Rand(start, end, num): #testing function to create random sets of S
        S = [] 
      
        for j in range(num): #creates list of random nums
            S.append(random.randint(start, end)) 
      
        return S 
'''

class Subset:  # Subset Class used for both BFI_ and HS_
#def __init__  when an object is created from a class and it allows the class to initialize the attributes of the class https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/
    def __init__(self, elements, sum):  #define a Set object which has attributes:
                                        #elements – a list of the elements in the set
                                        #sum – the sum of the elements in the set
        self.sum = sum
        self.elements = elements



class SubsetBFI: #SubsetBFI Class used for BFI_Subset_Sum

    def __init__(self, S, k, sum_BFI): # Let S be the set whose subsets we want to evaluate, Let k Be the taget value, 
        self.k = k
        self.S = S
        self.sum_BFI = sum_BFI #number of opereations it took to solve
        
        SubsetBFI.BFI_Subset_Sum(self)#sharing attributes 





    def BFI_Subset_Sum(self):
    #'self' is used to represent the instance of a class Subest or BFI_subset. By using the "self" keyword we access the attributes and methods of the class in python.
    #source for __init__ and self: https://www.tutorialspoint.com/What-is-difference-between-self-and-init-methods-in-python-Class
        subsets = [] 
        subsets.append(Subset( [], 0))
        #empty_set=[]
        
        for i  in  range(len(self.S)): #let new_subsets be an empty list of Set objects
            new_subsets = []
            for old_u in subsets: #for each subset old_u in subsets:

                new_u = Subset([self.S[i]], self.S[i]+ old_u.sum) #create a new Set object new_u which is a list of elements

                for x in old_u.elements: #loop for sum of sum_BFI

                    if x>0: #if total x is greater then append x to new_u
                        new_u.elements.append(x)
                        self.sum_BFI += 1


                if new_u.sum == k: #if target value is found

                    Set_of_elem = ', '.join(str(e) for e in new_u.elements) #returns a string in which the elements of sequence have been joined by str separator
                    
                    print ("List of elements = {%s}, sum of values = %s" %(Set_of_elem, new_u.sum)) #print the elements that add up to target value
                    SubsetBFI.EndStatement(self)
                    return



                elif new_u.sum < k: # if the new sum is less then k then appened old_u and new_u to new_subsets
                    new_subsets.append(old_u)
                    new_subsets.append(new_u)


                else: new_subsets.append(old_u) #else add old_u to the new_subsets make subsets = new_subsets
            subsets = new_subsets


           
        print("none of the following subsets sum to the target value.") #Target not found
        SubsetBFI.EndStatement(self) #share attributes 




    def EndStatement(self): #prints the counter for BFI
         print ("Number of Operations:", self.sum_BFI)



class SubsetHS: #SubsetHS Class init, hs_subset_sum, and Pair_sum 

    def __init__(self, S, k, sum_HS):
        self.k = k
        self.S = S
        self.sum_HS = sum_HS #number of operations it took to solve 
                             #S_left and S_right = S list n/2

        n = len(S)

        if (n % 2) == 0: #if S is who number split list in half
                Half_of_S = int(len(S)/2)
                S_Left = SubsetHS.pair_sum(self, 0, Half_of_S)
                if S_Left != None: #if s_left is empty move to right half
                    S_Right = SubsetHS.pair_sum(self, Half_of_S, n)

        else: #not a whole number
                Half_of_S =int((len(S)-1)/2)
                S_Left = SubsetHS.pair_sum(self, 0, Half_of_S)
                if S_Left != None: #if s_left is empty move to right
                    S_Right = SubsetHS.pair_sum(self, Half_of_S+1, n)

        if S_Left != None and S_Right != None: #if both empty
                SubsetHS.HS_Subset_Sum(self, S_Left, S_Right) #share arrtibutes




    def HS_Subset_Sum(self, S_Left, S_Right): #define HS_Subset_Sum

        S_Right.sort(key= operator.attrgetter('sum'))#sort the right half
        S_Left.sort(key= operator.attrgetter('sum'))#sort the left half 

        #define vars
        i = 0 
        z = len(S_Right)-1

        
        while i <= len(S_Left)-1 and z >= 0: #While loop to check if target value is found
            self.sum_HS += 1

            if S_Right[z].sum + S_Left[i].sum  == self.k:
            #if k is in Sums_Left or Sums_Right: print the corresponding subset that sums to k

                Set_of_elem1 = ', '.join(str(e) for e in S_Left[i].elements)
                Set_of_elem2= ', '.join(str(e) for e in S_Right[z].elements)

                
                print("List of elements = {%s, %s}, sum of values = %s" % (Set_of_elem1, Set_of_elem2, self.k))


                SubsetHS.EndStatement(self) #passes on attributes
                return  
            elif S_Right[z].sum + S_Left[i].sum  < self.k: # if total is less then target k i +=1
                i += 1

            elif S_Right[z].sum + S_Left[i].sum  > self.k: #if total is greater then taget k z -=1
                z -=1
            else:
           
                print("none of the following subsets sum to the target value.") #No subsets found
                SubsetHS.EndStatement(self)


    def pair_sum(self, Start, End): #define pair_sum
        subsets = []
        subsets.append(Subset([], 0)) #add supsets to Subset


        for i in range(Start,End): #From start to End 
            new_subsets = []

            for old_u in subsets: #old_u in subsets 
                new_u = Subset([self.S[i]], self.S[i] + old_u.sum) #create new_u subset    


                for z in old_u.elements:
                    if z > 0:
                        new_u.elements.append(z)
                        self.sum_HS += 1


                if new_u.sum == k: #if the sum of new_u is equal to the target value
                    Set_of_elem = ', '.join(str(x) for x in new_u.elements) #use the join methof to return the strong of joined elements 
                    print("List of elements = {%s}, sum of values = %s" % (Set_of_elem, new_u.sum)) #prints new_u elements that add up to target k 
                    SubsetHS.EndStatement(self)

                elif new_u.sum < k: #sum of new_u is less then k then 
                    new_subsets.append(old_u) #append old_u and new_u to new_subsets 
                    new_subsets.append(new_u)
                else:

                    new_subsets.append(old_u)
            subsets = new_subsets
        return subsets

    def EndStatement(self): #prints the counter for HS
        print ("Number of Operations:",self.sum_HS)



#final print loop


if __name__ == "__main__": #__name__ excutes all  the code in the file https://docs.python.org/3/library/__main__.html
    try:
        #num = random.randint(4,15) #generate random size of array #used to generate random S sets to test 
        #start = 1 #range of numbers is 1-100 rnd num from 1-100
        #end = 20
        #S = (Rand(start, end, num))#Random subset we want to evaluate 

        S = [3,5,3,9,18,4,5,6]
        k = 28  # target value
        print("Length of set:", len(S))
        print("Target Value:",k)
        print("In the set:", S)
        sum_BFI = 0
        sum_HS = 0
        print("\n") 
        print("BFI_Subset")
        SubsetBFI(S,k,sum_BFI)
        print("\n")           
        print("HS_Subset")
        SubsetHS(S,k,sum_HS)
       
    except: #throw error if code cant run
        "Error trying to Run code" 
