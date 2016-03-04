import numpy as np

def svd_inverse(A,b):
   U, s, V = np.linalg.svd(A, full_matrices=False)
   V_t = np.transpose(V)
   U_t = np.transpose(U)

   for x, y in np.ndindex(A.shape):
      if (A[x,y] != 0):      
         A[x,y] = 1/A[x,y]

   S = np.diag(s)

   print(s)
   print(U_t)
   print(V_t)

   sol = np.dot(V_t, np.dot(S, np.dot(U_t,b)))
   print(sol)


A = np.array([[-11,2],[2,3],[2,-1]])
b = np.array([[0],[7],[5]])
print(A)
print(b)
svd_inverse(A,b)
