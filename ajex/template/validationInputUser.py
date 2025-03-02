def validationInputUser(file):
    try:
        val_typeFile=file
        if type(val_typeFile) == ".csv" or type(val_typeFile)==".xlsx":
            print("next")
    except:
        print(f"Erro de {TypeError}")
    return None