def user_input():
    n = input("Enter number of blocks: ")
    n = int(n)

    start = 1
    blocks = []

    while start <= n:
        block = input("Enter the hight of block #{}: ".format(start))
        block = int(block)
        blocks += [block]
        start += 1
    
    return blocks

def visable_blocks(blocks):
    visable_blocks = [0]
    limit = blocks[0]
    index = 0

    for block in blocks:
        if block > limit:
            visable_blocks += [index]
            limit = block
        index += 1

    return visable_blocks

def print_by_index(user_list, indexes):
    
    for index in indexes:
        print(user_list[index])
        

if __name__ == "__main__":
    blocks = user_input()
    visable = visable_blocks(blocks)
    print("Visable blocks are:")
    print_by_index(blocks, visable)
