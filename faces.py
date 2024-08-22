def main():
  n = input("")
  convert(n)
def convert(str):
  str=str.replace(":)","🙂")
  str=str.replace(":(","🙁")
  print(str,end="")
main()


