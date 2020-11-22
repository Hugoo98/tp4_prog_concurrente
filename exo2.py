from multiprocessing import Process, Queue

def calcul_square(list,queue):
    for n in list:
        queue.put(n**2)

def calcul_cube(list,queue):
    for n in list:
        queue.put(n**3)



if __name__ == '__main__':
    list = {2,3,8,9,12}
    queue = Queue()

    square_process = Process(target=calcul_square, args=(list, queue))
    cube_process = Process(target=calcul_cube, args=(list, queue))

    square_process.start()
    cube_process.start()

    square_process.join()
    cube_process.join()

    while not queue.empty():
        print(queue.get())
