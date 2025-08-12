from fpdf import FPDF


def main():
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("Times", "B", 50)
    pdf.cell(210, 40, "CS50 Shirtificate", align="C", center=True)
    pdf.image("shirtificate.png", x=5, y=70, w=200)
    pdf.set_font("Times", "B", 30)
    pdf.set_text_color(255, 255, 255)
    pdf.ln(110)
    pdf.cell(210, 30, get_name(), align="C", center=True)
    pdf.output("shirtificate.pdf")


def get_name():
    name = input("Name: ")
    return f"{name} took CS50"


if __name__ == "__main__":
    main()
