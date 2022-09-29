with open('files/pyt_pict.jpg', 'rb') as file:
    data=file.read()
    print(data)
    with open('files/pyt_pict_copy.jpg', 'wb') as wfile:
        wfile.write(data)