#/usr/bin/env python3

import pickle

favorite_color = { "lion": "yellow", "kitty": "red" }
 
pickle.dump( favorite_color, open( "./pickles/save.p", "wb" ) )
