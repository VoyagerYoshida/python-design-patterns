from threading import Lock

class Config:
	_unique_instance = None
	_lock = Lock() # クラスロック

	model_name = "hoge"

	def __new__(cls):
		raise NotImplementedError("Cannot initialize via Constructor")

	@classmethod
	def __internal_new__(cls):
		return super().__new__(cls)

	@classmethod
	def get_instance(cls):
		if not cls._unique_instance:
			with cls._lock:
				if not cls._unique_instance:
					cls._unique_instance = cls.__internal_new__()
		return cls._unique_instance
	
	@classmethod
	def set_name(cls, name):
		cls.model_name = name