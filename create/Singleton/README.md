# Singleton

## 概要
オブジェクト指向言語では, 一般的に 1 つのクラスから複数のインスタンスが作成可能である. 
Singleton はオブジェクトが 1 つしかないことを保証したい時に用いられる. 
スクリプト内で統一して扱いたい Config 系の変数などに適用されることが多い. 

以下のようなモチベーションで使用する. 

- オブジェクトが呼び出される場所やタイミングに関わらず, 特定の値を保持してほしい
- あるオブジェクトを複数のクラスから異なるタイミングで使用したい
- オブジェクトを使い回すことでメモリ効率を向上させたい

## サンプルコード

1 つしかないオブジェクト (Config) を考える. 

### 一般的な書き方
1. 外部からオブジェクトの作成を防ぐため, イニシャライザを private にする
2. 外部からシングルトンオブジェクトにアクセスするための静的変数を作成する

以下に swift を使用して例を示す. `main.swift`

```swift
final class Config {
	public static let shared: Config =  Config() // 2 (static 変数なので直接アクセス可能. ライフサイクルとしては, 最初に shared にアクセスした際に Config オブジェクトが生成される)
	public var modelName: String = "hoge" // 他のクラスで共通して使用したい変数
	
	// 1 (private なので, 外部からオブジェクトを生成しようとするとエラーになる)
	private init() {}
}
```

シングルトンオブジェクトを使用したい時は, 静的変数 shared を通じてアクセスする

```swift
class Caller0 {
	private let config = Config.shared

	public func getModelName() -> String {
		return self.config.modelName
	} 
}

class Caller1 {
	private let config = Config.shared

	public func getModelName() -> String {
		return self.config.modelName
	} 
}
```

```swift
print("初期化時: \(Config.shared.modelName)")
Config.shared.modelName = "YOLO" // シングルトンのプロパティを変更

print("shared からプロパティにアクセス: \(Config.shared.modelName)")

var caller0 = Caller0()
print("Caller0 クラスからアクセス: \(caller0.getModelName())")

var caller1 = Caller1()
print("Caller1 クラスからアクセス: \(caller1.getModelName())")

var newConfig = Config()
```

出力

```
初期化時: hoge
shared からプロパティにアクセス: YOLO
Caller0 クラスからアクセス: YOLO
Caller1 クラスからアクセス: YOLO
error: 'Config' initializer is inaccessible due to 'private' protection level
```

Config クラスの modelName にどこからアクセスしても, 変更後のプロパティが共有されていることが分かる.  
また, Config クラスのオブジェクトの新たな生成はコンパイルエラーにより防がれている. 


### Python らしい書き方
Python にはアクセス修飾子 (public, private, ) が存在しないため, イニシャライザを private にすることはできない. 
そこで, 以下の 2 種類の方針が考えられる. 

- グローバル変数の利用
- \_\_new\_\_ を禁止する

#### グローバル変数の利用
Python では関数の外側で宣言された変数はグローバルスコープになるという性質を利用する. 
Singleton の変数の宣言は変数名を大文字とすることが多い. 
このように, クラスではなく仕様とルールで対応する. 

```python
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
```

出力

```
src % python3 main_global.py 
初期化時: hoge
直接プロパティにアクセス: YOLO
Caller0 クラスからアクセス: YOLO
Caller1 クラスからアクセス: YOLO
```

#### \_\_new\_\_ を禁止する
Pythonのクラスは初期化時に `__new__` がよばれ, その後に `__init__` が呼ばれる. 
シングルトンにしたいクラスでは, `__new__` を呼び出しをエラーにし, 
通常の `__new__` と同様の処理を行う `__internal_new__` を定義して, `get_instance` 内部ではそちらを呼ぶようにする. 

```python
from threading import Lock

class Config:
	_unique_instance = None
	_lock = Lock() # クラスロック (マルチスレッド動作の保証)

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
```

出力

```
src % python3 main_prohibit_new.py
初期化時: hoge
直接プロパティにアクセス: YOLO
id: <__main__.Config object at 0x10642c4f0>
Caller0 クラスからアクセス: YOLO
id: <__main__.Config object at 0x10642c4f0>
Caller1 クラスからアクセス: YOLO
id: <__main__.Config object at 0x10642c4f0>
Traceback (most recent call last):
  File "python-design-patterns/create/Singleton/src/main_prohibit_new.py", line 62, in <module>
    main()
  File "python-design-patterns/create/Singleton/src/main_prohibit_new.py", line 59, in main
    new_config = Config()
  File "python-design-patterns/create/Singleton/src/main_prohibit_new.py", line 10, in __new__
    raise NotImplementedError("Cannot initialize via Constructor")
NotImplementedError: Cannot initialize via Constructor
```

Config クラスの modelName にどこからアクセスしても, 変更後のプロパティが共有されていることが分かる.  
また, Config クラスのオブジェクトの新たな生成はエラーにより防がれている. 


## 参考文献
- [Singletonパターン - Pythonにおけるデザインパターン -](https://pydp.info/GoF_dp/creation/05_Singleton/index.html)
- [Pythonでシングルトン(Singleton)を実装してみる - [Dd]enzow(ill)? with DB and Python](https://www.denzow.me/entry/2018/01/28/171416)
- [PythonでSingletonパターンを実現する方法 | ソフトウェア開発日記](https://lightgauge.net/language/python/8546/)