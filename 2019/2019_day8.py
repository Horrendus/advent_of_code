IMAGE_WIDTH = 25
IMAGE_HEIGHT = 6


def puzzle1(layers):
    min_0_layer = min(layers, key=lambda layer: layer.count("0"))
    res = min_0_layer.count("1") * min_0_layer.count("2")
    print(res)


def puzzle2(layers):
    picture = [[0] * IMAGE_WIDTH for _ in range(IMAGE_HEIGHT)]
    for i in range(IMAGE_HEIGHT * IMAGE_WIDTH):
        y = i // IMAGE_WIDTH
        x = i - (y * IMAGE_WIDTH)
        print(x, y, i)
        layer = 0
        pixel = -1
        while layer < len(layers):
            if layers[layer][i] != "2":
                pixel = layers[layer][i]
                break
            else:
                layer += 1
        picture[y][x] = pixel

    for i in range(IMAGE_HEIGHT):
        for j in range(IMAGE_WIDTH):
            pixel = "#" if picture[i][j] == "1" else "."
            print(pixel, end="")
        print()


def main():
    with open("input/input_day8.txt") as f:
        data = f.read()
    layer_size = IMAGE_HEIGHT * IMAGE_WIDTH
    layers = []
    for i in range(0, len(data), layer_size):
        layers.append(data[i : i + layer_size])
    puzzle1(layers)
    print("=" * 80)
    puzzle2(layers)


if __name__ == "__main__":
    main()
