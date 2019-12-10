from intcode import main

if __name__ == "__main__":
    machine = main("input", inputs=[])
    for output in machine:
        print(output)
