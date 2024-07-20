import badger2040
from pngdec import PNG

badger = badger2040.Badger2040()
png = PNG(badger.display)
 
png.open_file("daniel.png")
png.decode(0,0)

# badger.set_pen(15)
# badger.clear()
# badger.set_pen(0)
# badger.set_thickness(7)
# badger.set_font("serif")
# badger.text("daniel", 20, 80, scale=2.5)
# badger.set_font("sans")
# badger.set_thickness(2)
# badger.text("he/him", 20, 20, scale=0.8)
badger.update()