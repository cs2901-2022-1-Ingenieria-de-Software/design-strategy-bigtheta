from prommms import prommms
from promopen import promopen
from promclose import promclose
from readcsv import readcsv
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