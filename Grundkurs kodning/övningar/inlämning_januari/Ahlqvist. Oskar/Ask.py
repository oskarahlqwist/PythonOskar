def check_datatype (data,datatype,message):
    if datatype == "String":
        if data.isalpha():
            return True, data
        else:
            print(message)
            return False, data

    elif datatype == "Int":
        if data.isdigit():
            return True, int(data)
        else:
            print(message)
            return False, data
    
    elif datatype == "Float":
        if not data.isdigit():
            try:
                float(data)
                return True, float(data)
            except ValueError:
                print(message)
                return False, data
            
def check_interval(data,start,end,message):
    if data.isdigit() and start < int(data) < end:
        return True, int(data)
    else:
        print(message)
        return False, data