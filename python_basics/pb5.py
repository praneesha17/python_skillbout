filename = "example.txt"
with open(filename, "w") as file:
    file.write("Hello, Praneesha!\n")
    file.write("Welcome to file handling in Python.\n")
with open(filename, "a") as file:
    file.write("This is an additional line.\n")
with open(filename, "r") as file:
    content = file.read()
    print("📄 File Contents:\n")
    print(content)