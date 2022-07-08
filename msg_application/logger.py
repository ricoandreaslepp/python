import logging
import config

# add custom methods
class BetterLogging(logging.Logger):

	DATA = 50

	def data_transfer(self, m : "[from, to, msg]", *args, **kws):
		if self.isEnabledFor(self.DATA):
			message = f"[data][{m[0]} -> {m[1]}] data: \"{m[2]}\""
			self._log(self.DATA, message, args, **kws)


# basic config
log = BetterLogging("test")
log.disabled = config.LOGGING_DISABLED
log.setLevel(0)

# handler
handler = logging.StreamHandler()
handler.setLevel(0)
log.addHandler(handler)

# formatter
formatter = logging.Formatter('[%(asctime)s]%(message)s')
handler.setFormatter(formatter)
