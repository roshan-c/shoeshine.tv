import PySimpleGUI as sg

sg.theme('SandyBeach')      
layout = [
    [sg.Text('Please enter your Username and the Seed provided by the Host')],
    [sg.Text('Username', size =(15, 1)), sg.InputText()],
    [sg.Text('Server Seed', size =(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]
  
window = sg.Window('Shoeshine.tv', layout)
event, values = window.read()
window.close()

username = values[0]
seedinput = values[1]

print(username)
print(seedinput)

connect = False
with open('seed.txt') as f:
    seed = f.read()
    print(seed)

if seed == seedinput:
    connect = True
    print('True')
    f.close()
else:
    connect = False
    print('False')
    f.close()
