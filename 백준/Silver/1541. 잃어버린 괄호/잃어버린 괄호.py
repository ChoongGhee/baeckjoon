import sys

if __name__ == "__main__":
    string = sys.stdin.readline().strip()
    
    minus_split = string.split("-")
    
    if len(minus_split) == 1:
        sum1 = sum(int(x) for x in minus_split[0].replace("+", " ").split())
        print(sum1)
    else:
        result = sum(int(x) for x in minus_split[0].replace("+", " ").split())
        
        for i in minus_split[1:]:
            result -= sum(int(x) for x in i.replace("+", " ").split())
        
        print(result)