print("Project :: R11600392")

import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print('Krystyna_Urbanczyk_R11600392_final_project.py -i <path_to_input_file> -o <path_to_output_file>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('Krystyna_Urbanczyk_R11600392_final_project.py -i <path_to_input_file> -o <path_to_output_file>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
      #elif opt in ("-t", "--tnumb"):
         #
   print('Input file is "', inputfile)
   print('Output file is "', outputfile)
   # Read in Matrix from file 
   file1 = open('time_step_0.dat', 'r') 
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
   
   printmatrix(currentmatrix, 0)
   # initialize time step count
   # print time step # 0-100
   for countstep in range(100):
      # perform actions on nextmatrix
      nextmatrix = simulate(currentmatrix, nextmatrix)
      # clear current matrix
      currentmatrix = []
      # copy nextmatrix to currentmatrix
      for row in nextmatrix:
         rows = []
         for char in row:
            rows.append(char)
         currentmatrix.append(rows)
      # print time step # and currentmatrix after actions
      printmatrix(currentmatrix, countstep+1)
   
   # Writing to file 
   file2 = open('time_step_100.dat', 'w') 
   for row in nextmatrix:
      for char in row: 
         print(char,sep="",end="",file=file2)
      print("",file=file2)
   
def printmatrix(currentprint, timestep):
   print("Time Step #", timestep)
   for row in currentprint:
      print(row)
   print("\n\n")

def simulate(currenttime, nexttime):
   r = 0
   c = 0
   maxr = len(currenttime)-1
   maxc = len(currenttime[0])-1


   # Start at currenttime[0][0] 

   for r in range(maxr+1):
      for c in range(maxc+1):
         Cell = currenttime[r][c]
         rPlus1 = r + 1
         cPlus1 = c + 1
         rMinus1 = r - 1
         cMinus1 = c - 1

         if rPlus1 > maxr:
            rPlus1 = 0
         
         if cPlus1 > maxc:
            cPlus1 = 0
            
         if rMinus1 < 0:
            rMinus1 = maxr
         
         if cMinus1 < 0:
            cMinus1 = maxc
         
         # always 8 neighbors
         # matrix[row][columm]
         # neighbors of Cell aka matrix[r][c]
         #  matrix[r-1][c-1]
         #  matrix[r-1][c]
         #  matrix[r-1][c+1]
         #  matrix[r][c-1]
         #  matrix[r][c+1]
         #  matrix[r+1][c-1]
         #  matrix[r+1][c]
         #  matrix[r+1][c+1]

         n1 = currenttime[rMinus1][cMinus1]
         n2 = currenttime[rMinus1][c]
         n3 = currenttime[rMinus1][cPlus1]
         n4 = currenttime[r][cMinus1]
         n5 = currenttime[r][cPlus1]
         n6 = currenttime[rPlus1][cMinus1]
         n7 = currenttime[rPlus1][c]
         n8 = currenttime[rPlus1][cPlus1]

         #print(n1 + " " + n2 + " " + n3 + "\n")
         #print(n4 + " " + Cell + " " + n5 + "\n")
         #print(n6 + " " + n7 + " " + n8 + "\n")

         nliving = 0
         ndead = 0

         if n1 == "O":
            nliving = nliving + 1
         else:
            ndead = ndead + 1

         if n2 == "O":
            nliving = nliving + 1
         else:
            ndead = ndead + 1

         if n3 == "O":
            nliving = nliving + 1
         else:
            ndead = ndead + 1

         if n4 == "O":
            nliving = nliving + 1
         else:
            ndead = ndead + 1
         
         if n5 == "O":
            nliving = nliving + 1
         else:
            ndead = ndead + 1

         if n6 == "O":
            nliving = nliving + 1
         else:
            ndead = ndead + 1

         if n7 == "O":
            nliving = nliving + 1
         else:
            ndead = ndead + 1

         if n8 == "O":
            nliving = nliving + 1
         else:
            ndead = ndead + 1


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
         
   return nexttime

   # if Cell is alive 
   #     if number of living neighbors == 2 | 3 | 4 
   #           Cell = alive for next time step
   #     else
   #           Cell = dead for next time step

   # if Cell is dead 
   #     if number of living neighbors > 0 
   #           if iseven number of living neighbors
   #                 Cell = alive for next time step
   #           else
   #                 Cell = dead for next time step
   #     else
   #           Cell = dead for next time step

   # read in input file with matrix to memory
   # create matrix called currentmatrix = []
   # save input file matrix to variable currentmatrix
   # create matrix called nextmatrix = []
   # perform actions on currentmatrix and save results to nextmatrix
   #     after all actions performed
   #           make currentmatrix = nextmatrix
   #           clear nextmatrix 



if __name__ == "__main__":
   main(sys.argv[1:])