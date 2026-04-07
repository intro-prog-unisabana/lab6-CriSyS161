def temp_and_color(dictionary):
    valor_temp = dictionary.get("temp")
    valor_color = dictionary.get("color")
    return (valor_temp, valor_color)

data1 = {"temp":22.5, "color":"blue", "status":"ok"}
data2 = {"status":"ok"}

print(temp_and_color(data1))
print(temp_and_color(data2))