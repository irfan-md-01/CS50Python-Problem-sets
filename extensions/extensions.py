s = input("File Name: ").lower().strip()

if s.endswith(".gif"):
    print("image/gif")
elif s.endswith(".jpg") :
    print("image/jpeg")
elif s.endswith(".jpeg") :
    print("image/jpeg")
elif s.endswith(".png"):
    print("image/png")
elif s.endswith(".pdf"):
    print("application/pdf")
elif s.endswith(".txt"):
    print("text/plain")
elif s.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
