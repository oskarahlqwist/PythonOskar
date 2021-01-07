
def check_datatype (data,datatype,message):
    if datatype == "String":
        if data != "":
            return True, str(data)
        else:
            print(message)
            return False, data

    elif datatype == "Int":
        if isinstance(data, int):
            return True, int(data)
        else:
            print(message)
            return False, data
    
    elif datatype == "Float":
        if not data.isdigit():
            return True, float(data)
        else:
            print(message)
            return False, data
            
def check_interval(data,start,end,message):
    if data.isdigit() and start < int(data) < end:
        return True, int(data)
    else:
        print(message)
        return False, data