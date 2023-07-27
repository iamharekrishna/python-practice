def extract_number(str):
    num=''
    for  chr in str:
      if chr.isdigit() or chr==".":
        num+=chr
    num=float(num)  
    print(num)

def start():
    text = "X-DSPAM Co  nfidence:456.7666   gfhfhgf fghgfhgf "
    extract_number(text)
if __name__=="__main__":
    start()