# 標準モジュール参照
import asyncio

# pyhookedモジュール参照
from pyhooked import Hook, KeyboardEvent, MouseEvent

class TriggerChecker():
    async def __init__(self):
        hk = Hook()  # make a new instance of PyHooked
        hk.handler = self.handle_events  # add a new shortcut ctrl+a, or triggered on mouseover of (300,400)
        hk.hook()  # hook into the events, and listen to the presses

    async def handle_events(args):
        await if isinstance(args, KeyboardEvent):
            print(args.key_code)
            if args.current_key == 'A' and args.event_type == 'key down' and 'Rcontrol' in args.pressed_key:
                print("Ctrl + A was pressed")
            elif args.current_key == 'Z' and args.event_type == 'key down' and 'Rcontrol' in args.pressed_key:
                hk.stop()
                print('Quitting.')

        await if isinstance(args, MouseEvent):
            if args.mouse_x == 300 and args.mouse_y == 400:
                print("Mouse is at (300,400") 