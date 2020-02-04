import multiprocessing, signal
import time


def count_numbers(number_process, return_dict):
    try:
        a = 0
        while True:
            a += 1
            if a == 15:
                exit(0)
            time.sleep(1)

    except SystemExit:
        print('exit')
        return_dict[str(number_process)+'-процесс'] = a


def exit_code(*args):
    print(*args)
    if args == 15:
        pass
    else:
        raise SystemExit


def close_process(process):
    if process.name == '1-процесс':
        process.terminate()
        exit(15)
    while True:
        print(process)
        time.sleep(30)


if __name__ == '__main__':
    process_list = []
    signal.signal(signal.SIGTERM, exit_code)
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    for x in range(5):
        process = multiprocessing.Process(target=count_numbers, args=(x, return_dict), name=str(x)+'-процесс')
        process.start()
        process_list.append(process)
        process_eye = multiprocessing.Process(target=close_process, args=(process,), name=str(x)+'-процесс-eye')
        process_eye.start()
        print(process_list)

    time.sleep(1)
    print(process_list)
    time.sleep(13)
    print(return_dict.items())