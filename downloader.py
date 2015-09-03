__author__ = 'ET'
import urllib

def main():
    for x in ['A','B','C','D','E']:
        for y in range(0, 51):
            if (y < 10):
                z = "0" + str(y)
            else:
                z = str(y)
            src = "http://www.utexas.edu/parking/bike/auction2015/original/" + str(x) + z + ".JPG"
            dst = str(x) + z + ".jpg"
            urllib.urlretrieve (src, dst)

if __name__ == "__main__":
    main()