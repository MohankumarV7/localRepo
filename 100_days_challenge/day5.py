## comments
# for a new line use \n
# \ is a escape sequence character 

print("hey",6,7, sep="~",end="009\n")
print("harry")

# the sep parameter is used to separate the values with a specific character, here it is "~"
# the end parameter is used to specify what to print at the end of the line

# Other Parameters of print statement
''' Object(s): Any object, and as manay as you like. Will be converted to string before printing.
    sep: (optional) A string inserted between values, default a space.
    end: (optional) A string appended after the last value, default a newline.
    file: (optional) An object with a write(string) method; defaults to the current sys.stdout.
    flush: (optional) A boolean, specifying if the output is flushed (True) or buffered (False). Default is False.'''