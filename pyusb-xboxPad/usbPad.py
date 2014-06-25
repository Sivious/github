import usb.core

dev = usb.core.find()
if dev is None:
  raise ValueError ('Our device is not connected')

