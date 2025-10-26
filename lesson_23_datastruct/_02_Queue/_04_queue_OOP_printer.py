class PrinterQueue:

    def __init__(self, printer_queue: list = None):
        if not printer_queue:
            self.__printer_queue = []
        else:
            self.__printer_queue = printer_queue

    @property
    def printer_queue(self):
        return self.__printer_queue

    def add_document(self, document):
        self.printer_queue.append(document)
        print(f'{document} помещен в очередь печати')

    # def print_document(self):
    #     if self.__printer_queue:
    #         document = self.printer_queue.pop(0)
    #         print(f'Печать {document}....')
    #         return document
    #     print("Очередь печати пуста")
    #     return None

    def print_documents(self):
        while self.__printer_queue:
            document = self.printer_queue.pop(0)
            print(f'Печать {document}....')
        print("Нет задач для печати")


if __name__ == '__main__':
    hp_printer = PrinterQueue()
    kyocera_printer = PrinterQueue(['Документ kyocera 1', 'Документ kyocera 2'])

    hp_printer.add_document('Отчет hp1')
    hp_printer.add_document('Отчет hp2')
    hp_printer.print_documents()
    print()

    kyocera_printer.add_document('Документ kyocera 3')
    kyocera_printer.add_document('Документ kyocera 4')
    kyocera_printer.print_documents()
