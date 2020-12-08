print("\nProject :: R11600392\n")

import sys, getopt
import multiprocessing
from multiprocessing import Process

def main(argv):
   inputfile = ''
   outputfile = ''
   tnumber = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:t:",["ifile=","ofile=","tnumb="])
   except getopt.GetoptError:
      print('Krystyna_Urbanczyk_R11600392_final_project.py -i <path_to_input_file> -o <path_to_output_file> -t <int>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('Krystyna_Urbanczyk_R11600392_final_project.py -i <path_to_input_file> -o <path_to_output_file> -t <int>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
      elif opt in ("-t", "--tnumb"):
         tnumber = int(arg)
         
   print('Reading input from ', inputfile, "\n")
   
   # Read in Matrix from file 
   file1 = open(inputfile, 'r') 
   Lines = file1.readlines() 
   
   # Matrix containing first time step
   currentmatrix = []
   for line in Lines:
      row = []
      for c in line.strip():
         row.append(c)
      currentmatrix.append(row)

   # Matrix containing next time step
   nextmatrix = []
   for row in currentmatrix:
      r = [] 
      for char in row:
         r.append(char)
      nextmatrix.append(r)

   print("Simulating...\n")

   # Print the initial matrix
   printmatrix(currentmatrix, 0)

   # print time step # 0-100
   for countstep in range(100):
      myProcs = list()

      splitBy = int((len(currentmatrix))/tnumber)
      currPos = 0
      q = multiprocessing.Queue()
      # Call simulate to perform actions on matrix
      while(currPos < len(currentmatrix)):
         p = Process(target=simulate, args=(currentmatrix, nextmatrix, currPos, currPos+splitBy, q))
         myProcs.append(p)
         p.start()
         currPos += splitBy

      for p in myProcs:
         p.join()
      # clear current matrix
      currentmatrix = []
      while(not q.empty()):
         result = q.get()
         for row in result:
            currentmatrix.append(row)
      
      # print time step # and currentmatrix after actions
      printmatrix(currentmatrix, countstep+1)
   
   # Writing to file 
   file2 = open(outputfile, 'w') 
   for row in currentmatrix:
      for char in row: 
         print(char,sep="",end="",file=file2)
      print("",file=file2)

   print('Simulation complete. Final result stored in output file ', outputfile)
   
def printmatrix(currentprint, timestep):
   print("Time Step #", timestep)
   for row in currentprint:
      print(row)
   print("\n\n")

# Perform actions on matrix
def simulate(currenttime, nexttime, start, end, q):

   r = 0
   c = 0
   maxr = len(currenttime)-1
   maxc = len(currenttime[0])-1

   for r in range(start,end):
      for c in range(maxc+1):
         Cell = currenttime[r][c]
         rPlus1 = r + 1
         cPlus1 = c + 1
         rMinus1 = r - 1
         cMinus1 = c - 1

         # Loop around the matrix for neighbors
         if rPlus1 > maxr:
            rPlus1 = 0
         
         if cPlus1 > maxc:
            cPlus1 = 0
            
         if rMinus1 < 0:
            rMinus1 = maxr
         
         if cMinus1 < 0:
            cMinus1 = maxc

         # Get all the neighbors of the selected cell
         n1 = currenttime[rMinus1][cMinus1]
         n2 = currenttime[rMinus1][c]
         n3 = currenttime[rMinus1][cPlus1]
         n4 = currenttime[r][cMinus1]
         n5 = currenttime[r][cPlus1]
         n6 = currenttime[rPlus1][cMinus1]
         n7 = currenttime[rPlus1][c]
         n8 = currenttime[rPlus1][cPlus1]

         # Count the number of living neighbors
         nliving = 0

         if n1 == "O":
            nliving = nliving + 1

         if n2 == "O":
            nliving = nliving + 1

         if n3 == "O":
            nliving = nliving + 1

         if n4 == "O":
            nliving = nliving + 1
         
         if n5 == "O":
            nliving = nliving + 1

         if n6 == "O":
            nliving = nliving + 1

         if n7 == "O":
            nliving = nliving + 1

         if n8 == "O":
            nliving = nliving + 1

         # Determine if the selected cell will be alive or dead in next time step
         if Cell == "O":
            if nliving == 2 or nliving == 3 or nliving == 4:
               nexttime[r][c] = "O"
            else:
               nexttime[r][c] = "."
         elif Cell == ".":
            if nliving > 0:
               if nliving == 2 or nliving == 4 or nliving == 6 or nliving == 8:
                  nexttime[r][c] = "O"
               else:
                  nexttime[r][c] = "."
            else:
                  nexttime[r][c] = "."
         
   return q.put(nexttime[start:end], start)

if __name__ == "__main__":
   main(sys.argv[1:])