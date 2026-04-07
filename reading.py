input_file = input ("Input File:\n")
with open(input_file,"r") as miArchivo:
    print(miArchivo.readlines())