try:
    from googlesearch import search
except ImportError:
    print("MODULE NOT FOUND")

query=input("Enter Query PLz and we will provide top 10 links")

for i in search(query,tld="com",num=10,stop=10,pause=2):
    print(i)