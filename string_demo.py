def calculate_length(text):
    return len(text)
  
def count_letter_str(text,char):
    count=0
    for ch in text:
        if ch==char:
            count+=1
    return count

def start():
    str_text=input("Enter Text:") 
    str_char=input("Enter the Character you need count:")
    count_char=count_letter_str(str_text,str_char)
    print(str(count_char))

if __name__ == "__main__":
    start()
