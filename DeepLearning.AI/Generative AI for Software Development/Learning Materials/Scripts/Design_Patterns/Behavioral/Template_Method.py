from abc import ABC, abstractmethod


# 1. Abstract Class
class ReportGenerator(ABC):

    # Template Method
    def generate_report(self):
        self.get_data()
        self.process_data()
        self.save_report()

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def process_data(self):
        pass

    @abstractmethod
    def save_report(self):
        pass


# 2. Concrete Class - PDF
class PDFReport(ReportGenerator):

    def get_data(self):
        print("Data retrieved.")

    def process_data(self):
        print("Data processed for PDF format.")

    def save_report(self):
        print("PDF report saved.")


# 3. Concrete Class - Excel
class ExcelReport(ReportGenerator):

    def get_data(self):
        print("Data retrieved.")

    def process_data(self):
        print("Data processed for Excel format.")

    def save_report(self):
        print("Excel report saved.")


# 4. Usage
pdf_report = PDFReport()
pdf_report.generate_report()

print("----------------")

excel_report = ExcelReport()
excel_report.generate_report()