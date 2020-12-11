with open("8input.txt") as input:
    input = input.read()
    width = 25
    height = 6
    area = height * width
    length = len(input)
    print(length)
    num_layers = length // area
    print(num_layers)
    layers = []
    for i in range(0,num_layers):
        layers.append(input[:area])
        input = input[area:]
    layer_index = 0
    count_of_0 = layers[layer_index].count('0')
    for layer in layers:
        if count_of_0 > layer.count('0'):
            count_of_0 = layer.count('0')
            layer_index = layers.index(layer)
    print(layers[layer_index].count('1') * layers[layer_index].count('2'))

    for layer in layers:
        print(layer)
    #0 is black, 1 is white, and 2 is transparent.
    image = list(layers[-1])
    print('and den')
    print(layers[-1])
    print(layers[-2])
    for i in range(num_layers-1, -1, -1):
        for px_i in range(0, area-1):
            if layers[i][px_i] == '0' or layers[i][px_i] == '1':
                image[px_i] = layers[i][px_i]

    image = ''.join(image)
    image = image.replace('0', ' ')
    for i in range(1, height+2):
        row = image[:width]
        print(row)
        image = image[width:]