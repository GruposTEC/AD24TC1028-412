def menor3(m1,m2,m3):
    """Metodo que saca el menor de tres valores

    Args:
        m1 (int): valor de la moneda 1
        m2 (int): valor de la moneda 2
        m3 (int): valor de la moneda 3

    Returns:
        int: mayor de los tres
    """
    x = 0
    z = 0    
    if(m1 > m2):
        x = m1
    else:
        x = m2
    if m3 > x:
        z = m3
    else:
        z = x
	        
    return z
	    
def main():
	ret = menor3(10, 5, 1)
	print(ret)
	    
print(__name__) 

main()