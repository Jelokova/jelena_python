# method r+ read and write
# import datetime
# with open(f"test{datetime.date.today()}.txt", 'r+', encoding="utf-8") as file:
#     data=file.read()
#     file.seek(0)
#     file.write('XXXXXXXXXXXXX')

with open(f"lorem.txt", 'r', encoding="utf-8") as file:
    data=file.read(100)
    with open(f'lorem.txt', 'w', encoding="utf-8") as wfile:
        wfile.write(data.upper())