
def check_datatype (data,datatype,message):
    if datatype == "String":
        if data == "":
            return (False, data)
        else:
            return (True, data)

def check_interval(data,start,end,message):