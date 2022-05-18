from prommms import prommms
from promopen import promopen
from promclose import promclose
from readcsv import readcsv
def main():
    excel = Readcsv()
    pc = promclose()
    po = promopen()
    pmm = prommms()
    excel.set_Strategy(pc)
    print(excel.do_Something())
    excel.setStrategy(po)
    print(excel.do_Something())
    excel.setStrategy(pmm)
    print(excel.do_Something())

if __name__ == '__main__':
    main()