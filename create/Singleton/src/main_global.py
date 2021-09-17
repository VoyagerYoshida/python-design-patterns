class Config:
	def __init__(self):
		self.model_name = "hoge"

	def set_name(self, name):
		self.model_name = name


CONFIG = Config()

def main():
	class Caller0:
		def __init__(self):
			self.config = CONFIG

		def get_model_name(self):
			return self.config.model_name

	class Caller1:
		def __init__(self):
			self.config = CONFIG

		def get_model_name(self):
			return self.config.model_name


	print(f"初期化時: {CONFIG.model_name}")
	CONFIG.set_name("YOLO")  # シングルトンのプロパティを変更

	print(f"直接プロパティにアクセス: {CONFIG.model_name}")

	caller0 = Caller0()
	print(f"Caller0 クラスからアクセス: {caller0.get_model_name()}")

	caller1 = Caller1()
	print(f"Caller1 クラスからアクセス: {caller1.get_model_name()}")
	

if __name__ == "__main__":
	main()

