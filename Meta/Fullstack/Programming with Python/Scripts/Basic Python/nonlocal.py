def d():
    color = "green"
    def e():
        nonlocal color # nonlocal allows to get the upper scopes variable that mean color here is equals to "green"
        color = "yellow" # Here the color from upper scope getting changed to "yellow"
    e()
    print("Color: " + color) # "yellow"
    color = "red"
color = "blue"
d()