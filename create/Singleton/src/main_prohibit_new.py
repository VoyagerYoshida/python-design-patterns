from model.config_prohibit_new import Config

def main():
	class Caller0:
		def __init__(self):
			self.config = Config.get_instance()

		def get_model_name(self):
			return self.config.model_name

	class Caller1:
		def __init__(self):
			self.config = Config.get_instance()

		def get_model_name(self):
			return self.config.model_name

	
	print(f"初期化時: {Config.model_name}")
	Config.set_name("YOLO") # シングルトンのプロパティを変更

	print(f"直接プロパティにアクセス: {Config.model_name}")
	print(f"id: {Config.get_instance()}")

	caller0 = Caller0()
	print(f"Caller0 クラスからアクセス: {caller0.get_model_name()}")
	print(f"id: {caller0.config}")

	caller1 = Caller1()
	print(f"Caller1 クラスからアクセス: {caller1.get_model_name()}")
	print(f"id: {caller1.config}")

	new_config = Config()
	
if __name__ == "__main__":
	main()

