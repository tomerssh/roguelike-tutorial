from typing import Optional

import tcod.event

from actions import Action, EscapeAction, MovementAction, FullscreenAction

class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        # alt+enter to fullscreen
        keyboardState = tcod.event.get_keyboard_state()
        isAltHeld = keyboardState[tcod.event.KeySym.LALT.scancode] or keyboardState[tcod.event.KeySym.RALT.scancode]
        if key == tcod.event.K_RETURN and isAltHeld:
            action = FullscreenAction()

        # arrow keys movement
        if key == tcod.event.K_UP:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = MovementAction(dx=1, dy=0)

        # escape to exit
        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()

        # No valid key was pressed
        return action