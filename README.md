# char_to_codel
Mapping letters to the codels in a Piet image

From char_to_codel.txt

To use char_to_codel.py, run "python char_to_codel.py [codel size] [filename of code to be read] [optionally, the filename of the output image]"
For example, "python char_to_codel.py 20 hello_world.txt", which creates a .png "hello_world_20.png" or "python char_to_codel.py 5 hello_world.txt hello_world.png" which creates "hello_world.png"

The mapping

black    k
white    w

         light  medium  dark
red      q      r       s
yellow   x      y       z
green    f      g       h
cyan     a      c       e
blue     p      b       d
magenta  l      m       n

All other characters map to white

The Piet color transition to command table

            Lightness change
Hue change  None       1 Darker     2 Darker
None                   push         pop
1 Step      add        subtract     multiply
2 Steps     divide     mod          not
3 Steps     greater    pointer      switch
4 Steps     duplicate  roll         in(number)
5 Steps     in(char)   out(number)  out(char)
