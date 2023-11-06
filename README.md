# aes-encrypt-decrypt-using-python
This is a part of module from my graduation project ( Job Agency Based on Security Control )
############################################################################################

**Simple Calculation using these programs**
-------------------------------------------

When a member(Min Naing Htun) registry to the system, how aes encryption do?

Registry information are as follow:
.
.
.
email = mintun2000@gmail.com
pass = *ismydatasecure?
.
.
.
In this case, the system will be encrypted (pass) data.
Then, the main point is the plain text ("*ismydatasecure?") to cipher text and store in to the database.
AES algorithm's encryption steps are as follow:

Plain text = *ismydatasecure?
System's auto generate key (16 bytes) for member (Min Naing Htun) = 9876543212584600

Plain text in hex:
2a 69 73 6d 79 64 61 74 61 73 65 63 75 72 65 3f

key text in hex:
39 38 37 36 35 34 33 32 31 32 35 38 34 36 30 30

State (for cipher text process)
2a 79 61 75
69 64 73 72
73 61 65 65
6d 74 63 3f

Key (for key generation process)
39 35 31 34
38 34 32 36
37 33 35 30
36 32 38 30

-----------------------------------------
Rcon table : 
01 02 04 08 10 20 40 80 1b 36
00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00
-----------------------------------------

(Key table all column 1 is called rotWord)
Round key generation process
Round 1 key table :
3d 08 39 0d
3c 08 3a 0c
33 00 35 05
2e 1c 24 14

Round 2 key table :
c1 c9 f0 fd
57 5f 65 69
c9 c9 fc f9
f9 e5 c1 d5

Round 3 key table :
3c f5 05 f8
ce 91 f4 9d
ca 03 ff 06
ad 48 89 5c

Round 4 key table :
6a 9f 9a 62
a1 30 c4 59
80 83 7c 7a
ec a4 2d 71

Round 5 key table :
b1 2e b4 d6
7b 4b 8f d6
23 a0 dc a6
46 e2 cf be

Round 6 key table :
67 49 fd 2b
5f 14 9b 4d
8d 2d f1 57
b0 52 9d 23

Round 7 key table :
c4 8d 70 5b
04 10 8b c6
ab 86 77 20
41 13 8e ad

Round 8 key table :
f0 7d 0d 56
b3 a3 28 ee
3e b8 cf ef
78 6b e5 48

Round 9 key table :
c3 be b3 e5
6c cf e7 09
6c d4 1b f4
c9 a2 47 0f

Round 10 key table :
f4 4a f9 1c
d3 1c fb f2
1a ce d5 21
10 b2 f5 fa
------------------------------------------------

2a 79 61 75
69 64 73 72
73 61 65 65
6d 74 63 3f
    XOR
39 35 31 34
38 34 32 36
37 33 35 30
36 32 38 30

				Round 1
#------------------------------------------------#

state of round
13 4c 50 41
51 50 41 44
44 52 50 55
5b 46 5b 0f

after sub byte
7d 29 53 83
d1 53 83 1b
1b 00 53 fc
39 5a 39 76

after shift row
7d 29 53 83
53 83 1b d1
53 fc 1b 00
76 39 5a 39

after mix column
2a 09 ca 4c
58 12 12 03
12 02 90 19
6b 76 41 3d

#------------------------------------------------#

2a 09 ca 4c
58 12 12 03
12 02 90 19
6b 76 41 3d
    XOR
3d 08 39 0d
3c 08 3a 0c
33 00 35 05
2e 1c 24 14

				Round 2
#------------------------------------------------#

state of round
17 01 f3 41
64 1a 28 0f
21 02 a5 1c
45 6a 65 29

after sub byte
f0 7c 0d 83
43 a2 34 76
fd 77 06 9c
6e 02 4d a5

after shift row
f0 7c 0d 83
a2 34 76 43
06 9c fd 77
a5 6e 02 4d

after mix column
a5 56 7f e2
00 c5 ff d1
aa d9 9c f9
fe f0 98 30

#------------------------------------------------#


a5 56 7f e2
00 c5 ff d1
aa d9 9c f9
fe f0 98 30
    XOR
c1 c9 f0 fd
57 5f 65 69
c9 c9 fc f9
f9 e5 c1 d5

				Round 3
#------------------------------------------------#

state of round
64 9f 8f 1f
57 9a 9a b8
63 10 60 00
07 15 59 e5

after sub byte
43 db 73 c0
5b b8 b8 6c
fb ca d0 63
c5 59 cb d9

after shift row
43 db 73 c0
b8 b8 6c 5b
d0 63 fb ca
d9 c5 59 cb

after mix column
5c d8 f0 77
9a d0 e4 f8
30 f1 19 52
04 3c b0 47

#------------------------------------------------#



5c d8 f0 77
9a d0 e4 f8
30 f1 19 52
04 3c b0 47
    XOR
3c f5 05 f8
ce 91 f4 9d
ca 03 ff 06
ad 48 89 5c

				Round 4
#------------------------------------------------#

state of round
60 2d f5 8f
54 41 10 65
fa f2 e6 54
a9 74 39 1b

after sub byte
d0 d8 e6 73
20 83 ca 4d
2d 89 8e 20
d3 92 12 af

after shift row
d0 d8 e6 73
83 ca 4d 20
8e 20 2d 89
af d3 92 12

after mix column
04 1d bf 1d
eb e4 99 a1
be 3c 5c 6c
23 24 6e 18

#------------------------------------------------#


04 1d bf 1d
eb e4 99 a1
be 3c 5c 6c
23 24 6e 18
   XOR
6a 9f 9a 62
a1 30 c4 59
80 83 7c 7a
ec a4 2d 71

				Round 5
#------------------------------------------------#

state of round
6e 82 25 7f
4a d4 5d f8
3e bf 20 16
cf 80 43 69

after sub byte
9f 13 3f d2
d6 48 4c 41
b2 08 b7 47
8a cd 1a f9

after shift row
9f 13 3f d2
48 4c 41 d6
b7 47 b2 08
f9 8a cd 1a

after mix column
b3 3f c2 cc
34 c8 bd 67
b2 54 4d 3a
ac 31 33 87

#------------------------------------------------#


b3 3f c2 cc
34 c8 bd 67
b2 54 4d 3a
ac 31 33 87
    XOR
b1 2e b4 d6
7b 4b 8f d6
23 a0 dc a6
46 e2 cf be

				Round 6
#------------------------------------------------#

state of round
02 11 76 1a
4f 83 32 b1
91 f4 91 9c
ea d3 fc 39

after sub byte
77 82 38 a2
84 ec 23 c8
81 bf 81 de
87 66 b0 12

after shift row
77 82 38 a2
ec 23 c8 84
81 de 81 bf
12 87 66 b0

after mix column
52 23 d4 c7
3e 3a 4d db
b4 94 43 88
d0 75 cd bd

#------------------------------------------------#

52 23 d4 c7
3e 3a 4d db
b4 94 43 88
d0 75 cd bd
    XOR
67 49 fd 2b
5f 14 9b 4d
8d 2d f1 57
b0 52 9d 23
				Round 7
#------------------------------------------------#

state of round
35 6a 29 ec
61 2e d6 96
39 b9 b2 df
60 27 50 9e

after sub byte
96 02 a5 ce
ef 31 f6 90
12 56 37 9e
d0 cc 53 0b

after shift row
96 02 a5 ce
31 f6 90 ef
37 9e 12 56
0b d0 cc 53

after mix column
58 4b 24 a8
a6 9c 64 a2
d4 b8 5e 78
b1 d5 f5 56

#------------------------------------------------#


58 4b 24 a8
a6 9c 64 a2
d4 b8 5e 78
b1 d5 f5 56
    XOR
c4 8d 70 5b
04 10 8b c6
ab 86 77 20
41 13 8e ad

				Round 8
#------------------------------------------------#

state of round
9c c6 54 f3
a2 8c ef 64
7f 3e 29 58
f0 c6 7b fb

after sub byte
de b4 20 0d
3a 64 df 43
d2 b2 a5 6a
8c b4 21 0f

after shift row
de b4 20 0d
64 df 43 3a
a5 6a d2 b2
0f 8c b4 21

after mix column
a1 ef e3 c7
ed 23 7f 95
fa 30 1b 2b
a6 71 82 dd

#------------------------------------------------#

a1 ef e3 c7
ed 23 7f 95
fa 30 1b 2b
a6 71 82 dd
   XOR
f0 7d 0d 56
b3 a3 28 ee
3e b8 cf ef
78 6b e5 48

				Round 9
#------------------------------------------------#

state of round
51 92 ee 91
5e 80 57 7b
c4 88 d4 c4
de 1a 67 95

after sub byte
d1 4f 28 81
58 cd 5b 21
1c c4 48 1c
1d a2 85 2a

after shift row
d1 4f 28 81
cd 5b 21 58
48 1c 1c c4
2a 1d a2 85

after mix column
97 72 8d b0
a2 c0 ec e3
f2 0b cc de
b9 ac 1a 15

#------------------------------------------------#

97 72 8d b0
a2 c0 ec e3
f2 0b cc de
b9 ac 1a 15
   XOR
c3 be b3 e5
6c cf e7 09
6c d4 1b f4
c9 a2 47 0f

				Round 10
#------------------------------------------------#

state of round
54 cc 3e 55
ce 0f 0b ea
9e df d7 2a
70 0e 5d 1a

after sub byte
20 4b b2 fc
8b 76 2b 87
0b 9e 0e e5
51 ab 4c a2

after shift row
20 4b b2 fc
76 2b 87 8b
0e e5 0b 9e
a2 51 ab 4c

#------------------------------------------------#

20 4b b2 fc
76 2b 87 8b
0e e5 0b 9e
a2 51 ab 4c
   XOR
f4 4a f9 1c
d3 1c fb f2
1a ce d5 21
10 b2 f5 fa

#--------------Cipher Text in hex----------------#
d4 01 4b e0
a5 37 7c 79
14 2b de bf
b2 e3 5e b6

d4 a5 14 b2 01 37 2b e3 4b 7c de 5e e0 79 bf b6

#------------------------------------------------#

#-------Cipher Text in Base64 String-------------#

1KUUsgE3K+NLfN5e4Hm/tg==

#------------------------------------------------#




#################################################################################################################################################


AES algorithm's decryption steps are as follow:

Cipher text = 1KUUsgE3K+NLfN5e4Hm/tg==
private key for member (Min Naing Htun) = 9876543212584600

Plain text in hex:
d4 a5 14 b2 01 37 2b e3 4b 7c de 5e e0 79 bf b6

key text in hex:
39 38 37 36 35 34 33 32 31 32 35 38 34 36 30 30

State (for cipher text process)
d4 01 4b e0
a5 37 7c 79
14 2b de bf
b2 e3 5e b6

Key (for key generation process)
39 35 31 34
38 34 32 36
37 33 35 30
36 32 38 30

-----------------------------------------
Rcon table : 
01 02 04 08 10 20 40 80 1b 36
00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00
-----------------------------------------

(Key table column 1 is called rotWord)
Round key generation process
Round 1 key table :
3d 08 39 0d
3c 08 3a 0c
33 00 35 05
2e 1c 24 14

Round 2 key table :
c1 c9 f0 fd
57 5f 65 69
c9 c9 fc f9
f9 e5 c1 d5

Round 3 key table :
3c f5 05 f8
ce 91 f4 9d
ca 03 ff 06
ad 48 89 5c

Round 4 key table :
6a 9f 9a 62
a1 30 c4 59
80 83 7c 7a
ec a4 2d 71

Round 5 key table :
b1 2e b4 d6
7b 4b 8f d6
23 a0 dc a6
46 e2 cf be

Round 6 key table :
67 49 fd 2b
5f 14 9b 4d
8d 2d f1 57
b0 52 9d 23

Round 7 key table :
c4 8d 70 5b
04 10 8b c6
ab 86 77 20
41 13 8e ad

Round 8 key table :
f0 7d 0d 56
b3 a3 28 ee
3e b8 cf ef
78 6b e5 48

Round 9 key table :
c3 be b3 e5
6c cf e7 09
6c d4 1b f4
c9 a2 47 0f

Round 10 key table :
f4 4a f9 1c
d3 1c fb f2
1a ce d5 21
10 b2 f5 fa
------------------------------------------------

d4 01 4b e0
a5 37 7c 79
14 2b de bf
b2 e3 5e b6
    XOR
f4 4a f9 1c
d3 1c fb f2
1a ce d5 21
10 b2 f5 fa
    =
state of round
20 4b b2 fc
76 2b 87 8b
0e e5 0b 9e
a2 51 ab 4c

				Round 1
#------------------------------------------------#

after inverse shift row
20 4b b2 fc
8b 76 2b 87
0b 9e 0e e5
51 ab 4c a2

after inverse sub byte
54 cc 3e 55
ce 0f 0b ea
9e df d7 2a
70 0e 5d 1a

state of round
97 72 8d b0
a2 c0 ec e3
f2 0b cc de
b9 ac 1a 15

after inverse mix column
d1 4f 28 81
cd 5b 21 58
48 1c 1c c4
2a 1d a2 85

#------------------------------------------------#


				Round 2
#------------------------------------------------#

after inverse shift row
d1 4f 28 81
58 cd 5b 21
1c c4 48 1c
1d a2 85 2a

after inverse sub byte
51 92 ee 91
5e 80 57 7b
c4 88 d4 c4
de 1a 67 95

state of round
a1 ef e3 c7
ed 23 7f 95
fa 30 1b 2b
a6 71 82 dd

after inverse mix column
de b4 20 0d
64 df 43 3a
a5 6a d2 b2
0f 8c b4 21

#------------------------------------------------#


				Round 3
#------------------------------------------------#

after inverse shift row
de b4 20 0d
3a 64 df 43
d2 b2 a5 6a
8c b4 21 0f

after inverse sub byte
9c c6 54 f3
a2 8c ef 64
7f 3e 29 58
f0 c6 7b fb

state of round
58 4b 24 a8
a6 9c 64 a2
d4 b8 5e 78
b1 d5 f5 56

after inverse mix column
96 02 a5 ce
31 f6 90 ef
37 9e 12 56
0b d0 cc 53

#------------------------------------------------#


				Round 4
#------------------------------------------------#

after inverse shift row
96 02 a5 ce
ef 31 f6 90
12 56 37 9e
d0 cc 53 0b

after inverse sub byte
35 6a 29 ec
61 2e d6 96
39 b9 b2 df
60 27 50 9e

state of round
52 23 d4 c7
3e 3a 4d db
b4 94 43 88
d0 75 cd bd

after inverse mix column
77 82 38 a2
ec 23 c8 84
81 de 81 bf
12 87 66 b0

#------------------------------------------------#


				Round 5
#------------------------------------------------#

after inverse shift row
77 82 38 a2
84 ec 23 c8
81 bf 81 de
87 66 b0 12

after inverse sub byte
02 11 76 1a
4f 83 32 b1
91 f4 91 9c
ea d3 fc 39

state of round
b3 3f c2 cc
34 c8 bd 67
b2 54 4d 3a
ac 31 33 87

after inverse mix column
9f 13 3f d2
48 4c 41 d6
b7 47 b2 08
f9 8a cd 1a

#------------------------------------------------#


				Round 6
#------------------------------------------------#

after inverse shift row
9f 13 3f d2
d6 48 4c 41
b2 08 b7 47
8a cd 1a f9

after inverse sub byte
6e 82 25 7f
4a d4 5d f8
3e bf 20 16
cf 80 43 69

state of round
04 1d bf 1d
eb e4 99 a1
be 3c 5c 6c
23 24 6e 18

after inverse mix column
d0 d8 e6 73
83 ca 4d 20
8e 20 2d 89
af d3 92 12

#------------------------------------------------#

				Round 7
#------------------------------------------------#

after inverse shift row
d0 d8 e6 73
20 83 ca 4d
2d 89 8e 20
d3 92 12 af

after inverse sub byte
60 2d f5 8f
54 41 10 65
fa f2 e6 54
a9 74 39 1b

state of round
5c d8 f0 77
9a d0 e4 f8
30 f1 19 52
04 3c b0 47

after inverse mix column
43 db 73 c0
b8 b8 6c 5b
d0 63 fb ca
d9 c5 59 cb

#------------------------------------------------#


				Round 8
#------------------------------------------------#

after inverse shift row
43 db 73 c0
5b b8 b8 6c
fb ca d0 63
c5 59 cb d9

after inverse sub byte
64 9f 8f 1f
57 9a 9a b8
63 10 60 00
07 15 59 e5

state of round
a5 56 7f e2
00 c5 ff d1
aa d9 9c f9
fe f0 98 30

after inverse mix column
f0 7c 0d 83
a2 34 76 43
06 9c fd 77
a5 6e 02 4d

#------------------------------------------------#


				Round 9
#------------------------------------------------#

after inverse shift row
f0 7c 0d 83
43 a2 34 76
fd 77 06 9c
6e 02 4d a5

after inverse sub byte
17 01 f3 41
64 1a 28 0f
21 02 a5 1c
45 6a 65 29

state of round
2a 09 ca 4c
58 12 12 03
12 02 90 19
6b 76 41 3d

after inverse mix column
7d 29 53 83
53 83 1b d1
53 fc 1b 00
76 39 5a 39

#------------------------------------------------#


				Round 10
#------------------------------------------------#

after inverse shift row
7d 29 53 83
d1 53 83 1b
1b 00 53 fc
39 5a 39 76

after inverse sub byte
13 4c 50 41
51 50 41 44
44 52 50 55
5b 46 5b 0f

#------------------------------------------------#

13 4c 50 41
51 50 41 44
44 52 50 55
5b 46 5b 0f
   XOR
39 35 31 34
38 34 32 36
37 33 35 30
36 32 38 30

#--------------Plain Text in hex----------------#
2a 79 61 75
69 64 73 72
73 61 65 65
6d 74 63 3f

2a 69 73 6d 79 64 61 74 61 73 65 63 75 72 65 3f

#------------------------------------------------#

#--------Plain Text in character-----------------#

*ismydatasecure?

#------------------------------------------------#
