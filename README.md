## Simplified DES Algorithm

1. Take a 64 bit input
2. Divide it into 2 parts LPT and RPT of 32 bits each
3. Prepare a function with the following rounds :
<br>a. Take RPT as input and expand it into 48 bits using an expansion permutation table
<br>b. XOR result of step 3.1 and a 48 bit key
<br>c. Convert the result of step 3.2 into a 32 bit value using an s box substitution.
4. Move out of the function block and XOR with 32 bit LPT
5. Swap LPT and RPT
6. Repeat the Process one more time with a new 48 bit key and expansion permutation tables.
7. finally swap after 2 rounds and concatenate LPT and RPT to obtain the 64 bit Ciphertext