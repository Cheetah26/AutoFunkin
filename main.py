from pynput.keyboard import Key, KeyCode, Listener
import keypresser
import threading
import os

running = False
timegap = 0.015

NORMAL_ARROW_COLOR = (135, 163, 173)

# arrow coords
top_y = 130
bottom_y = 270
arrow_x_coords = {
  'left': 1486,
  'down': 1710,
  'up': 1950,
  'right': 2170,
}

def screenshot():
  from PIL import ImageGrab
  return ImageGrab.grab()

def on_press(key):
  global running
  global timegap
  if key == KeyCode.from_char('q'):
    running = not running
    print('Starting' if running else 'Stopping')
  elif key == KeyCode.from_char(']'):
    timegap += 0.005
    print('Keypress Delay: ' + str(timegap))
  elif key == KeyCode.from_char('['):
    if timegap > 0.005:
      timegap -= 0.005
      print('Keypress Delay: ' + str(timegap))
    else:
      print('Cannot decrement any further')

def check_pixels(frame):
  for dir in arrow_x_coords:
    top_pixel = frame.getpixel((arrow_x_coords[dir], top_y))
    bottom_pixel = frame.getpixel((arrow_x_coords[dir], bottom_y))
    if top_pixel != NORMAL_ARROW_COLOR or bottom_pixel != NORMAL_ARROW_COLOR:
      keypresser.TapKey(dir, timegap)

def main():
  print()
  print('Press Q at anytime to start AutoFunkin')
  print('Brackets [ ] adjust keypress time if necessary')
  print('Use Ctrl+C in this terminal to quit the program')
  print()

  listener = Listener(on_press=on_press)
  listener.start()

  while True:
    if running:
      frame = screenshot()
      check_pixels(frame)

if __name__ == '__main__':
  main()