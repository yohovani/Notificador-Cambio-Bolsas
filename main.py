from compareData import compare

def start_process():
    process = compare()
    x = 0

    while x < 4:
        process.update_data_set_update()
        process.compare_nikkei()
        process.compare_dax()
        process.compare_nasdaq()
        x += 1
    print("finalizado")


if __name__ == '__main__':
    start_process()
