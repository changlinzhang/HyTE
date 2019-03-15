def generate_triple2id(num, filename):
    with open(filename, 'w') as f:
        f.write(str(num)+'\n')
        for i in range(num):
            f.write(str(i)+'\t'+str(i)+'\n')


if __name__ == "__main__":
    generate_triple2id()
