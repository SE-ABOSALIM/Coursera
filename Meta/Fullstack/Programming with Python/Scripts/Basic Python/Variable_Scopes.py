# Global Variable: Accessible from everywhere
global_variable = "(This is a global variable)"

def func1():
    # Accessible only in func1 and nested functions under the func1 (Same as closures)
    enclosed_variable = "(This is an enclosed variable)"

    def func2():
        # Accessible only in func2 and nested functions under the func2 (It's not accessible in func1)
        local_variable = "(This is a local variable)"
        print(f'Accessing the enclosed variable and the global variable from func2: {enclosed_variable} | {local_variable}')
    func2()

func1()