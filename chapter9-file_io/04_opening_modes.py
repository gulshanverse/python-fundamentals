#'r' - read a file
#'w' - write in a file
#'a' - open file for append
#'+' - open for updating
#'rb' will open for read in binary Mode 
#'rt' will open for read in text mode


# append file

st = "Hey Parth, You are amazing."

f = open("myFiles","a")

f.write(st)

f.close()