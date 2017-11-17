def functionName( level ):
    if level < 1:
        raise Exception("Invalid level!", level)


try:
    functionName(0)
except "Invalid level!":
    print "Error! "
else:
    print "go on ..."
finally:
    print "always do this"
