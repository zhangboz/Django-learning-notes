# try:
#     you do your operations here...
# except ExceptionI:
#     if there is ExceptionI, then excute this block.
# except ExceptionII:
#     if there is ExceptionII then excute this block.
# else:
#     if there is no exception then execute this block

try:
    f = open("simple.txt", "r")
    f.write("test write to simple text!")
except IOError: ## IOError, input output operation error.
    print("ERROR: COULD NOT FIND FILE OR READ DATA!")
else:
    print("SUCCESS!")
    f.close()

print("CODE IS CONTINUE RUNNING")

try:
    f = open("simple.txt", "r")
    f.write("test write to simple text!")
except: ## no error type indicated, script will continue to run despite any kind of error.
    print("ERROR: GENERAL ERROR MESSAGE")
else:
    print("SUCCESS!")
    f.close()
finally:
    print("I ALWAYS WORK, NO MATTER WHAT!")
print("CODE IS CONTINUE RUNNING")
