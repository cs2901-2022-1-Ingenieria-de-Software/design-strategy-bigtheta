from prommms import *
from promopen import *
from promclose import *
from readcsv import *
def main():
    excel = Readcsv()
    pc = promclose()
    po = promopen()
    pmm = prommms()
    excel.setStrategy(pc)
    print(excel.doSomething())
    excel.setStrategy(po)
    print(excel.doSomething())
    excel.setStrategy(pmm)
    print(excel.doSomething())

if __name__ == '__main__':
    main()