# Affine-Cipher
Affine Cipher
Author: ephemeralwaves

==About==
A simple mono alphabetic substitution cipher I used to help me level up my programming/math skills :) Though I would not suggest using it for anything other than education/historic purposes since it is highly insecure (by means of frequency analysis, brute force, guessing or otherwise).


=====Software=====
Tested in Python 2.7 on Windows and Gnu/Linux


==Instructions==

To run: (sudo) python Affine_Encrypt_Decrypt.py
Select if you want to encrypt or decrypt
Input 2 keys (a & b)

Note on key "a":
The code is only set to work with plain text that is all in capitals. It doesn’t handle spaces or punctuation very well either, so that I’ll leave to someone else to improve on (or maybe my future self :P)
The “a” value for the key must be coprime with m, in this case m = 26 (i.e., if gcd(a, m) = 1; the number 26 has 12 numbers that it’s coprime with [1,3,5,7,9,11,15,17,19,21,23,25]).

===Some Keys of interest====
Atbash Affine Cipher: a= 25, b =25
Ciphertext example: ZGYZHSXRKSVI
Caesar cipher: a= 1, b =3
Ciphertext example: FDHVDUFLSKHU
ROT13: a=1, b=13
Ciphertext example: EBGPVCURE
