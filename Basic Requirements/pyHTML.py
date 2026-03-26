import pyhtml as ph

code =  ph.html(
    ph.head(ph.title("This is the title of web-site")),
    ph.body(
        ph.h1("This is the heading of website"),
        ph.div(ph.p("Paragraph here"),
            ph.h2("This is second heading")
            )
    )
)

print(code.render())