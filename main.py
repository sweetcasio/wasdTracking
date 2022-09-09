import keyboard
import time

def main():
    times = {t:0 for t in 'wasd'}
    keys = {key:0 for key in 'wasd'}
    def test(key):
        if key.name in keys.keys():
            methods = {
                'w':'forward',
                'a':'left',
                's':'backward',
                'd':'right'
            }
            info = f'{methods[key.name]}({round(time.time() - times[key.name], 1)})'
            
            if keys[key.name] == 0 and key.event_type == 'down':
                keys[key.name] += 1
                times[key.name] = time.time()
            elif key.event_type == 'up':
                keys[key.name] = 0
                with open('moves.txt', 'a') as file:
                    file.write(info + '\n')

    keyboard.hook(test)
    mainloop()
    
def mainloop():
    is_closed = False
    def switch():
        nonlocal is_closed 
        is_closed = not is_closed

    keyboard.on_press_key('esc', lambda key: switch())
    while not is_closed:
        do_nothing()

    def do_nothing():
        pass

if __name__ == '__main__':
    main()
