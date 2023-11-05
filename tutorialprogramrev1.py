def func1(firstnumb,secondnumb):
    
    if(firstnumb==secondnumb):
        return secondnumb
        
    if(firstnumb!=secondnumb):
        return firstnumb

if __name__=="__main__":
    result = func1(100,100)
    print(result)
