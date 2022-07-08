import config
import logging

Log = logging.getLogger()
Log.setLevel(logging.INFO)
Log.disabled = config.LOGGING_DISABLED

"""
#it kind of works but it doesnt really

DATA = 10
logging.addLevelName(DATA, "data_transfer")

def data_transfer(self, message, *args, **kws):
	print("ran this")
	print(self.isEnabledFor(DATA))
	if True:
		print("ran this")
		self._log(DATA, message, args, **kws)

logging.RootLogger.data_transfer = data_transfer

print(dir(logging.RootLogger))

Log.data_transfer("hello")
"""

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s [+] %(message)s')
handler.setFormatter(formatter)
Log.addHandler(handler)

Log.info("Started logger...")
