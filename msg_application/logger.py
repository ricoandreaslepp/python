###############################################
# Completely reworked logging for the project #
###############################################

import config
import logging

# print("source code for reference", logging.__file__)


# -----------------------------------------------
# New methods for logging class

logging.DATA = 50
logging.addLevelName(logging.DATA, "DATA_TRANSFER")

# basically a rip off of other builtin methods (.info, .warning etc)
def data_transfer(self, m : "[from, to, msg]", *args, **kws):
	""" example
	Log.data_transfer(["127.0.0.1:1235", "server", "hello, world!"]) =>
		[2022-07-08 15:59:46,320][data][127.0.0.1:1235 -> server] data: "hello, world!"
	"""

	if self.isEnabledFor(logging.DATA):
		message = f"[data][{m[0]} -> {m[1]}] data: \"{m[2]}\""
		self._log(logging.DATA, message, args, **kws)

# pass it to the Logger class
logging.Logger.data_transfer = data_transfer


# -----------------------------------------------
# make Log object and configure it
Log = logging.getLogger()
Log.setLevel(logging.INFO)
Log.disabled = config.LOGGING_DISABLED


handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s]%(message)s')
handler.setFormatter(formatter)
Log.addHandler(handler)
