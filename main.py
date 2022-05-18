from prommms import prommms
from promopen import promopen
from promclose import promclose
from readcsv import readcsv
def main():
    excel = Readcsv()
    pc = promclose()
    po = promopen()
    pmm = prommms()
    excel.set_strategy(pc)
    print(excel.do_something())
    excel.setStrategy(po)
    print(excel.do_something())
    excel.setStrategy(pmm)
    print(excel.do_something())

if __name__ == '__main__':
    main()