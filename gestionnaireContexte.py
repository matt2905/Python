class HTML:
    level = 0

    def __init__(self, balise):
        self.balise = balise

    def __enter__(self):
        print("    " * HTML.level + "<" + self.balise + ">")
        HTML.level += 1

    def __exit__(self, exc_type, exc_val, exc_tb):
        HTML.level -= 1
        print("    " * HTML.level + "</" + self.balise + ">")


with HTML("html"), HTML("body"), HTML("p"):
    print("Lorem ipsum")
