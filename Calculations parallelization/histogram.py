import matplotlib.pyplot as plt
import threading
import cv2

def histogram(img, i, h):
    h[i] = (cv2.calcHist([img], [i], None, [256], [0, 256]))


def main():
    path = 'photo1.jpg'
    img = cv2.imread(path)
    col = ('b', 'g', 'r')
    h = [0, 0, 0]

    threads = list()
    for i in range(3):
        t = threading.Thread(target=histogram, args=(img, i, h))
        threads.append(t)
        t.start()

    for i, thread in enumerate(threads):
        thread.join()
        plt.plot(h[i], color=col[i])

    plt.title("Histogram")
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()