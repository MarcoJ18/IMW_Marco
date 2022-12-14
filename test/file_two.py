# Python module to import

print("File two __name__ is set to: {}" .format(__name__))

if __name__ == "__main__":
   print("File two executed when ran directly")
else:
   print("File two executed when imported")
