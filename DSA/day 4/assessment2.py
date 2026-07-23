class PrinterQueue:

    def __init__(self):
        self.queue = []

    # Add print job
    def add_job(self, document):
        self.queue.append(document)
        print(f"{document} added to the printer queue.")

    # Print document
    def print_job(self):
        if len(self.queue) == 0:
            print("No documents to print.")
        else:
            document = self.queue.pop(0)
            print(f"Printing: {document}")

    # Show waiting documents
    def show_queue(self):
        print("Current Queue:", self.queue)


printer = PrinterQueue()

printer.add_job("Resume.pdf")
printer.add_job("Assignment.pdf")
printer.add_job("Project_Report.pdf")

printer.show_queue()

printer.print_job()

printer.show_queue()

printer.print_job()

printer.show_queue()