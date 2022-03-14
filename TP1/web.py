import webbrowser

def fill_items(matrix):
    txt = ""
    for i in matrix:
        if i == 0:
            inner = "<div class='zero'>{}</div> ".format(i)
        else:
            inner = "<div class='box'>{}</div> ".format(i)
        txt = txt + inner
    
    return txt

def get_grid(matrix, i):
    html = """
    <p> Paso: """ + str(i) + """
    <li class='game-board'>""" + format(fill_items(matrix)) + """
    </li> """
    return html

def render(node):
    f = open('trace.html','w')
    nodes = node.get_trace()
    page = """ <style> 
    body {
        align-items: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
        margin: auto;
        text-align: center;
    }
    .game-board {
        background: whitesmoke;
        display: grid;
        grid-template-rows: 100px 100px 100px;
        grid-template-columns: 100px 100px 100px;
        margin: 1rem;
        border-radius: 5px;
    }
    .box {
        background: transparent;
        display: flex;
        align-items: center;
        justify-content: center;
        color: black;
        font-size: 35px;
    }
    .zero {
        background: yellow;
        display: flex;
        align-items: center;
        justify-content: center;
        color: black;
        border-radius: 0px 0px 5px 0px;
        font-size: 35px;
    }
    </style>
    <h1> 8 Number Puzzle </h1>
    <h4> Florencia Chao, Ariadna Fernandez Truglia, Faustino Maggioni Duffy </h4>
    <ul> """
    i = 0
    for matrix in nodes:
        message = get_grid(matrix, i)
        i = i + 1
        page = page + message
    page = page + "</ul>"
    f.write(page)
    f.close()

    webbrowser.open_new_tab('trace.html')
