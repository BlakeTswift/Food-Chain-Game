{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Monaco;}
{\colortbl;\red255\green255\blue255;\red113\green115\blue122;\red10\green12\blue21;\red255\green255\blue255;
\red164\green191\blue255;\red252\green120\blue8;\red254\green204\blue10;\red86\green182\blue255;}
{\*\expandedcolortbl;;\cssrgb\c51765\c52549\c55294;\cssrgb\c3922\c5098\c10980;\cssrgb\c100000\c100000\c100000;
\cssrgb\c70196\c80000\c100000;\cssrgb\c100000\c54902\c0;\cssrgb\c100000\c82745\c0;\cssrgb\c40000\c76863\c100000;}
\margl1440\margr1440\vieww29200\viewh15960\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 #Food Chain Game Using Python - www.101computing.net/food-chain-game-using-python/\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 import\cf4 \strokec4  \cf6 \strokec6 random\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 organisms\cf4 \strokec4  = [\cf7 \strokec7 "grass"\cf4 \strokec4  , \cf7 \strokec7 "insect"\cf4 \strokec4  , \cf7 \strokec7 "rabbit"\cf4 \strokec4 , \cf7 \strokec7 "slug"\cf4 \strokec4 , \cf7 \strokec7 "frog"\cf4 \strokec4 , \cf7 \strokec7 "vole"\cf4 \strokec4 , \cf7 \strokec7 "thrush"\cf4 \strokec4 , \cf7 \strokec7 "fox"\cf4 \strokec4 , \cf7 \strokec7 "hawk"\cf4 \strokec4 ]\cb1 \
\cf6 \cb3 \strokec6 organismsLength\cf4 \strokec4  = len(\cf6 \strokec6 organisms\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 #Select organism for player\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 playerPosition\cf4 \strokec4  = \cf6 \strokec6 random\cf4 \strokec4 .\cf8 \strokec8 randint\cf4 \strokec4 (\cf6 \strokec6 0\cf4 \strokec4 ,\cf6 \strokec6 organismsLength-1\cf4 \strokec4 )\cb1 \
\cf6 \cb3 \strokec6 playerOrganism\cf4 \strokec4  = \cf6 \strokec6 organisms\cf4 \strokec4 [\cf6 \strokec6 playerPosition\cf4 \strokec4 ]\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 print(\cf7 \strokec7 "Player Organism: "\cf4 \strokec4  + \cf6 \strokec6 playerOrganism\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 #Select organism for computer\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 computerPosition\cf4 \strokec4  = \cf6 \strokec6 random\cf4 \strokec4 .\cf8 \strokec8 randint\cf4 \strokec4 (\cf6 \strokec6 0\cf4 \strokec4 ,\cf6 \strokec6 organismsLength-1\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 #Ensure that the computer organism will be different from the player organism\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 while\cf4 \strokec4  \cf6 \strokec6 computerPosition\cf4 \strokec4 ==\cf6 \strokec6 playerPosition\cf4 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3   \cf6 \strokec6 computerPosition\cf4 \strokec4  = \cf6 \strokec6 random\cf4 \strokec4 .\cf8 \strokec8 randint\cf4 \strokec4 (\cf6 \strokec6 0\cf4 \strokec4 ,\cf6 \strokec6 organismsLength-1\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 computerOrganism\cf4 \strokec4  = \cf6 \strokec6 organisms\cf4 \strokec4 [\cf6 \strokec6 computerPosition\cf4 \strokec4 ]\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3 print(\cf7 \strokec7 "Computer Organism: "\cf4 \strokec4  + \cf6 \strokec6 computerOrganism\cf4 \strokec4 )\cb1 \
\cb3  \cb1 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 foodWeb\cf4 \strokec4  = \{\cf7 \strokec7 'grass'\cf4 \strokec4 : [\cf7 \strokec7 ''\cf4 \strokec4 ],\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3            \cf7 \strokec7 'insect'\cf4 \strokec4 : [\cf7 \strokec7 'grass'\cf4 \strokec4 ],\cb1 \
\cb3            \cf7 \strokec7 'rabbit'\cf4 \strokec4 : [\cf7 \strokec7 'grass'\cf4 \strokec4 ],\cb1 \
\cb3            \cf7 \strokec7 'slug'\cf4 \strokec4 : [\cf7 \strokec7 'grass'\cf4 \strokec4 ],\cb1 \
\cb3            \cf7 \strokec7 'thrush'\cf4 \strokec4 : [\cf7 \strokec7 'slug'\cf4 \strokec4 ,\cf7 \strokec7 'insect'\cf4 \strokec4 ],\cb1 \
\cb3            \cf7 \strokec7 'vole'\cf4 \strokec4 : [\cf7 \strokec7 'insect'\cf4 \strokec4 ],\cb1 \
\cb3            \cf7 \strokec7 'frog'\cf4 \strokec4 : [\cf7 \strokec7 'insect'\cf4 \strokec4 ],\cb1 \
\cb3            \cf7 \strokec7 'hawk'\cf4 \strokec4 : [\cf7 \strokec7 'frog'\cf4 \strokec4 ,\cf7 \strokec7 'vole'\cf4 \strokec4 ,\cf7 \strokec7 'thrush'\cf4 \strokec4 ],\cb1 \
\cb3            \cf7 \strokec7 'fox'\cf4 \strokec4 : [\cf7 \strokec7 'rabbit'\cf4 \strokec4 ,\cf7 \strokec7 'frog'\cf4 \strokec4 ,\cf7 \strokec7 'vole'\cf4 \strokec4 ]\}\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 #Complete code here to find out if the computer organism and the player organism are linked (Direct link or indirect link)\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 def player_link\cf4 \strokec4 ():\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3   \cf2 \strokec2 #enum through values and see if player = CPU\cf4 \cb1 \strokec4 \
\cb3   \cb1 \
\cb3   \cf5 \strokec5 if\cf4 \strokec4  \cf6 \strokec6 playerOrganism\cf4 \strokec4  \cf5 \strokec5 in\cf4 \strokec4  \cf6 \strokec6 foodWeb\cf4 \strokec4 [\cf6 \strokec6 computerOrganism\cf4 \strokec4 ]:\cb1 \
\cb3     \cf5 \strokec5 return\cf4 \strokec4  \cf6 \strokec6 1\cf4 \cb1 \strokec4 \
\cb3   \cf5 \strokec5 elif\cf4 \strokec4  \cf6 \strokec6 computerOrganism\cf4 \strokec4  \cf5 \strokec5 in\cf4 \strokec4  \cf6 \strokec6 foodWeb\cf4 \strokec4 [\cf6 \strokec6 playerOrganism\cf4 \strokec4 ]:\cb1 \
\cb3     \cf5 \strokec5 return\cf4 \strokec4  \cf6 \strokec6 2\cf4 \cb1 \strokec4 \
\cb3   \cf5 \strokec5 else\cf4 \strokec4 :\cb1 \
\cb3     \cf5 \strokec5 return\cf4 \strokec4  \cf6 \strokec6 0\cf4 \cb1 \strokec4 \
\
\cb3 print (\cf7 \strokec7 "\\n"\cf4 \strokec4 )\cb1 \
\cb3 print (\cf7 \strokec7 "Is there a link?:"\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 if\cf4 \strokec4  \cf6 \strokec6 player_link\cf4 \strokec4 () \cf6 \strokec6 !\cf4 \strokec4 = \cf6 \strokec6 0\cf4 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3   print(\cf7 \strokec7 "Yes"\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 else\cf4 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3   print(\cf7 \strokec7 "No"\cf4 \strokec4 )\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 #If a link is detected decide who between the computer and the player wins the game\cf4 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 if\cf4 \strokec4  \cf6 \strokec6 player_link\cf4 \strokec4 () == \cf6 \strokec6 1\cf4 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3   print (\cf7 \strokec7 "Computer Wins!"\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 elif\cf4 \strokec4  \cf6 \strokec6 player_link\cf4 \strokec4 () == \cf6 \strokec6 2\cf4 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf4 \cb3   print (\cf7 \strokec7 "Player Wins!"\cf4 \strokec4 )\cb1 \
\
\
}