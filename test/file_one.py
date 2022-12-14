# Python module to execute
import file_two

print("File one __name__ is set to: {}" .format(__name__))

if __name__ == "__main__":
   print("File one executed when ran directly")
else:
   print("File one executed when imported")
