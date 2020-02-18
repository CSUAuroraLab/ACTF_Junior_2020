import threading

def isqrt(n):
    x = n
    y = (x + n // x) // 2
    while y < x:
      x = y
      y = (x + n // x) // 2
    return x

def Fermat(num, x):
    y2 = x*x - num;
    y = isqrt(y2);
    if y*y == y2:
        print([x+y, x-y]);

if __name__ == "__main__":
    num = int(input('n='))
    x = isqrt(num)
    if x*x < num:
        x += 1
    i = 1
    while(i < 1e20):
        threads = []
        for j in range(40):
            t = threading.Thread(target = Fermat, args = (num, x))
            i += 1
            x += 1
            threads.append(t)
        for t in threads:
            t.start()
        for t in threads:
            t.join()