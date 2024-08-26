names = [
    "John.Doe",
    "jane.doe",
    "Alice Wonderland",
    "Mr.Smith",
    "Dr.Jones",
    "Emily.",
    "michael.Clark",
    "Dr.Jane.Doe",
    "Ms.Mary-jane",
    "mr.bean"
]

valid_name = []
non_valid_names=[]

for name in names:
    if all(char not in ["-","_"] for char in name):
        print(name.title()) 


                
            