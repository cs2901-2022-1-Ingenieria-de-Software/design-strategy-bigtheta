from prommms import prommms
from promopen import promopen
from promclose import promclose
from readcsv import Readcsv
def main():
    excel = Readcsv()
    pc = promclose()
    po = promopen()
    pmm = prommms()
    excel.set_strategy(pc)
    print(excel.do_something())
    excel.set_strategy(po)
    print(excel.do_something())
    excel.set_strategy(pmm)
    print(excel.do_something())

if __name__ == '__main__':
    main()