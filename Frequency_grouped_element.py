def frequency(input_list):
    frequency = {}
    for item in input_list:
        if item in frequency:
            frequency[item]+=1
        else:
            frequency[item]=1
    return frequency
def main():
    list_element =input("enter the element")
    input_list= list_element.split()
    result = frequency(input_list)
    print("Grouped Frequency")
    for item,count in result.items():
        print(f"{item} : {count}")
main()
            
