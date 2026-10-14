def inspect_data(data):
    if data is None:
        print("data is empty. like very empty")
    else:
        print(f"data: {data}, type: {type(data).__name__}")


data = 0
inspect_data(data)
# output ➜ data: 0, type: int

data = ""
inspect_data(data)
# output ➜ data: , type: str