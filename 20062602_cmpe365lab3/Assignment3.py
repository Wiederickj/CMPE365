# CMPE365 | Algorithms | Assignment 3 Submission | Jackson Wiederick | 20062602 | 16jw98 
import math
import os

#Define the import of files and file names
File1ASC = "File1ASC.txt"
File2ASC = "File2ASC.txt"
Part_1_Code_Strings_File = "Part_1/Code_Strings.txt"
Part_1_Encoded_File = "Part_1/encodedmessage.txt"
Part_1_Decoded_File = "Part_1/decodedmessage.txt"



#Used to help write read and write: https://www.tutorialspoint.com/python/python_files_io.htm
def File_Write(output, Code_Strings): #writes the message to a text file
    outputmessage = open(output, "w+")
    outputmessage.write(Code_Strings)
    outputmessage.close()
    print("Wrote: " + output)

def File_Read(input): 
    message = open(input, "r+")
    List_S = message.read()
    message.close()
    return List_S.split("\n")

#file functions
def Return_FileSize(files, encoded):
    print("File: " + files)
    fileSize = math.ceil(len(encoded)/8) #divide by 8 to get the "actual" size, because we are simulating bits
    print("Size of file: " + str(fileSize) + " bytes")
    
def Return_Code_Strings(filename, dictionary):
    #fix up the code
    fixcode = File_Read(filename)
    fixcode = [code.split("\t") for code in fixcode] 
    fixcode.pop()
    #Create a dictionary 
    Code_list = {} 
    if dictionary:
        for code in fixcode:
            Code_list[int(code[0])] = code[1]
    else:
        Code_list = [{"Key" : int(code[0]), "Code" : code[1]} for code in fixcode]
    return Code_list

List_Key = [j for j in range(32, 127)]

Right_Side = "1" #set right side to 1
Left_Side = "0" #set left side to 0

#used to go through all Canonical_Collections
def Collections(x):
    Canonical_Collections = []
    filename = "Canonical_Collection"

    for j in range(0, x): 
        Canonical_Collections.append(filename + str(j + 1))

    return Canonical_Collections

#Building Huffan algorithm,Site used to help: https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/  

class Make_Node:
    #define the value, the counter left node and right node
    def __init__(self, value, counter, left_node, right_node):
        self.left_node = left_node
        self.right_node = right_node
        self.counter = counter
        self.value = value

#done
    def Return_Code_String(self, key):
        if self.value == key:
            return "" 
        else:
            if self.left_node != None:
                if self.left_node.Tree_check(key):
                    return Left_Side + self.left_node.Return_Code_String(key)
            if self.right_node != None:
                if self.right_node.Tree_check(key):
                    return Right_Side + self.right_node.Return_Code_String(key)
            return ""

#done
    def Tree_check(self, key): #Check the tree to see if the value is equal to the key, if equal return true else return false 
        
        if self.value == key:
            return True
        else:
            TreeVal = False
            if self.right_node != None:
                TreeVal = self.right_node.Tree_check(key)
            if self.left_node != None and TreeVal == False:
                TreeVal = self.left_node.Tree_check(key)
            return TreeVal

#done
        
def CreateDirectory(input, output):
    dire = os.listdir(input) #site used to help https://www.tutorialspoint.com/python/os_listdir.htm 

#create the list of keys and frequencies
    Listofvals = []
    for key in List_Key:
        Listofvals.append({"Key": key, "Frequency": 0})
    Listofvals.append({"Key": 10, "Frequency": 0})

#for loop to get Unitext    
    for message in dire:
        List_S = File_Read(input + "/" + message)

        for string in List_S:
            for char in string:
                Unitext = ord(char) 
#return the unitext from the character

                if Unitext != 10 and Unitext < 126: #126 1 less then 127 becuase starts at 0
                    Listofvals[Unitext - 32]["Frequency"] += 1
                elif Unitext == 10:
                    Listofvals[-1]["Frequency"] += 1
            Listofvals[-1]["Frequency"] += 1

    Huff_Tree = buildTree(Listofvals) #create Huffman Tree
    Huff_root = Huff_Tree[0] #Huffman Root made from the Huffman tree

    Code_Strings = ""

    #create kvals which is a list of key values
    kvals = List_Key
    kvals.insert(0, 10)

    for key in kvals: 
        Code_Strings += str(key) + "\t" + Huff_root.Return_Code_String(key) + "\n" #sets code_strings to root of the key+=

    File_Write(output, Code_Strings) #write the Code_Strings file
    return Code_Strings


#DONE

def MakeCode_String(input, output): #this fuunction makes the new string codes from the input text
    Listofvals = []
    for key in List_Key:
        Listofvals.append({"Key": key, "Frequency": 0})
    Listofvals.append({"Key": 10, "Frequency": 0})
    
    List_S = File_Read(input)

    for string in List_S:
        for char in string:
            Unitext = ord(char) # Get unitext from the character
            #if statment to check if the Unitext to make sure it is in range

            if Unitext != 10 and Unitext < 126:
                Listofvals[Unitext - 32]["Frequency"] += 1

            elif Unitext == 10:
                Listofvals[-1]["Frequency"] += 1
        Listofvals[-1]["Frequency"] += 1
    
    Huff_Tree = buildTree(Listofvals)
    Huff_root = Huff_Tree[0] # Get root node from the tree
    Code_Strings = ""

    kvals = List_Key #make a list of the key values 
    kvals.insert(0, 10)
    for key in kvals: #adds the current key and root to list
        Code_Strings += str(key) + "\t" + Huff_root.Return_Code_String(key) + "\n"
    
    File_Write(output, Code_Strings)
    return Code_Strings  #returns the Code_String as a file that can be viewed


#sites used to help decoede and encode:
#https://www.geeksforgeeks.org/python-strings-decode-method/
#https://www.programiz.com/python-programming/methods/string/encode

def Decode_File(Code_list, input, output):
    Code_Strings = Return_Code_Strings(Code_list, False) #reurns dictionarie with list of codes
    #sort tthe codes ineverse
    Code_Strings = sorted(Code_Strings, key=lambda z:z["Code"], reverse=True)  
    
    encoded_file = open(input, "r+") #Read the enconded file
    encoded = encoded_file.read()
    encoded_file.close()
    
    
    decoded = "" #Starts the decoded the encoded file
    j = 0 
    while (j < len(encoded)): #go through the whole document
        curt = "" + encoded[j]   #checks the current string
        key = Trytomatch(Code_Strings, curt) 
        while (j+1 < len(encoded) and key == -1):
            #code should be building the string the whole time 
            j += 1
            curt += encoded[j]
            key = Trytomatch(Code_Strings, curt)

        if (key != -1):
        #if the next item is code then add to decode
            decoded += chr(key)
        j += 1
    
    
    File_Write(output, decoded)
    
    return decoded #return decoded message

def Encode_File(input, Code_list, output): #function used to write encoded files
    Code_Strings = Return_Code_Strings(Code_list, True) 
    inFile = open(input, "r+") #"r+ used to read input data:
    data = inFile.read() #read file and exit
    inFile.close()
    
    Encode_String = ""
    for char in data:
        if(ord(char) <= 126): #one less than 127 starts at 0
            Encode_String += Code_Strings[ord(char)]
    
    File_Write(output, Encode_String) #write encoded file
    return Encode_String




#DONE




def Trytomatch(Code_list, r): #reurns the match for each charecter encode/decode
    for j in Code_list:
        if (r == j["Code"]):
            return j["Key"]
    return -1




def buildTree(freq):

    tree = sorted(freq, key = lambda z:z["Frequency"])
    tree = [Make_Node(entry["Key"], entry["Frequency"], None, None) for entry in tree] #build tree with empty roots
    
    while len(tree) > 1:
        tempNode = Make_Node(0, tree[0].counter + tree[1].counter, tree[0], tree[1])

        tree.remove(tree[1])
        tree.remove(tree[0])

        index = 0
    
        while index < len(tree) and tree[index].counter < tempNode.counter:
            index += 1
        if index > len(tree):
            tree.insert(-1, tempNode)
        else:
            tree.insert(index, tempNode)
    
    return tree
#return the tree

#Part 1 main this builds a code_string dictonary that encodes and decodes a text file.
def main():
    print ("CMPE 365")
    print ("Assignment #3 - Huffman Coding")
    print ("Author: Jackson Wiederick")
    print ("Student Number: 20062602")
    Part1_Code_list = MakeCode_String("File1ASC.txt", "Part_1/Code_Strings.txt")
    Part1_EncodedMessage = Encode_File(File2ASC, Part_1_Code_Strings_File, Part_1_Encoded_File)
    part1_DecodedMessage = Decode_File(Part_1_Code_Strings_File, Part_1_Encoded_File, Part_1_Decoded_File)



    """ Part 2 of the assignment
    """
    Canonical_Collections = Collections(3)
    for collection in Canonical_Collections:
        #going thorugh all three collections
        Strings_File = "Part_2/" + collection + "/" + "Code_Strings.txt"
        Code_Strings = CreateDirectory(collection, Strings_File)
        for files in os.listdir("Data_Files"): #open data_files

            input = "Data_Files/" + files 

            #output for both encoded/decoded message
            outputDecodedMessage = "Part_2/" + collection + "/" + files + "DecodedMessage.txt"
            outputEncodedMessage = "Part_2/" + collection + "/" + files + "EncodedMessage.txt"
            decodedmessage = Decode_File(outputEncodedMessage, Strings_File, outputDecodedMessage)
            encodedmessage = Encode_File(input, Strings_File, outputEncodedMessage)
            Return_FileSize(files, encodedmessage)

main()
