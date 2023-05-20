from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Customize the header of the PDF
        pass

    def footer(self):
        # Customize the footer of the PDF
        pass

    def chapter_body(self, output):
        # Customize the content of the chapter in the PDF
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Vocabulary Worksheet', 0, 1, 'C')

        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, output)

    def generate_pdf(self, output):
        self.add_page()
        self.chapter_body(output)

        self.output('output.pdf')


if __name__ == '__main__':
    pdf = PDF()
    pdf.generate_pdf()
