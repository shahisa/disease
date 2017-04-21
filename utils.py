import jellyfish
#This piece of code is supposed to help with the different types of ascii encoding in Python 2 & 3
#Python 2 uses ascii as the default encoding for source files, which means you must specify another encoding at the top of the file to use non-ascii unicode characters in literals. 
#Python 3 uses utf-8 as the default encoding for source files, so this is less of an issue.
# Used this for a better explaination and pre-error fix of encoding http://stackoverflow.com/a/1342373/2367526
def remove_non_ascii(s): 
	return "".join(i for i in s if ord(i)<128)
 # I'm not sure why this line is fully needed. 
def fuzzy_match(s1, s2, max_dist=.8):
    return jellyfish.jaro_distance(s1, s2) >= max_dist