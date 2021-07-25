# Abstract Factory


## 概要
Abstract Factory が用いられるのは, 以下の 2 つの条件を満たす場合である. 

1. 他のオブジェクトから構成された複雑なオブジェクトを生成したい場合
1. 構成オブジェクトがある特定のファミリーに属する場合

<p align="center">
  <img src="./assets/ClassDiagram/general.png" width="90%">
<p>

ある抽象ファクトリーについて, 複数の具象ファクトリーが存在する場合を考える. 
それらが同じオブジェクトを生成するメソッドを提供するが, それぞれのプラットフォームに適応したスタイルで実装する必要がある場合, 
ファクトリーのインスタンスを引数にとる汎用的な関数を作ることで, 引数として渡すファクトリーの種類に応じて処理を変化させることができる. 


## サンプルコード
ピザ工場を考える. 
条件は以下の通りである. 

- ピザは, Dough (生地), Source (ソース), Topping (トッピング) の 3 つで構成される. 
- ピザ工場 A, B で作られるピザの各材料は, それぞれ以下の通りである. 

| | PizzaFactoryA | PizzaFactoryB | 
| :---: | :---: | :---: |
| Dough | WheatDough | RiceFlourDough | 
| Source | TomatoSource | BasilSource | 
| Topping | CoanTopping | CheeseTopping | 

- 必要なピザの材料をすべて配列に入れることを「ピザを作る」と定義する.
- ピザを作る際に, サイズによって入れる材料の量を調整する. 
- すべての材料の種類と量を確認するために, 各材料クラスにメソッド ```check()``` をもたせる.

### 一般的な書き方
はじめに, 抽象ファクトリーと抽象プロダクトの 2 種類の基底クラスを用意する. 
具象ファクトリーと具象プロダクトは, これらを継承することで作成する.
なお, 抽象クラスは, 基底クラスと具象クラスの両方の機能を担うクラスとして実装されることが多い. 

抽象ファクトリーが持つ機能は, 以下の 2 つである. 

- ```make_pizza()``` : 材料インスタンスを配列に格納する.
- ```check_pizza()``` : すべての材料インスタンスが持つメソッド ```check()``` を実行する. 

<p align="center">
  <img src="./assets/ClassDiagram/sample.png" width="90%">
<p>

例として, ピザ工場 A でピザの生地を作成する流れは以下のようになっている. 

1. 抽象ファクトリー ```AbstractPizzaFactory``` の中で, メソッド ```add_dough()``` が実行される. 
1. ```self.factory``` は具象ファクトリー ```PizzaFactoryA``` のインスタンスであるため, ```PizzaFactoryA``` クラスのメソッド ```add_dough()``` が実行される. 

```shell
$ python3 src/main.py
--- Pizza 1 ---
[ PizzaFactoryA ] Constructor
 -> ( AbstractPizzaFactory ) Constructor
---------------
( AbstractPizzaFactory ) Method make_pizza()
 -> [ PizzaFactoryA ] Method add_dough()
     -> ( Dough ) Constructor
 -> [ PizzaFactoryA ] Method add_source()
     -> ( Source ) Constructor
 -> [ PizzaFactoryA ] Method add_topping()
     -> ( Topping ) Constructor
---------------
( AbstractPizzaFactory ) Method check_pizza()
 -> [ WheatDough ] amount: 1.2
 -> [ TomatoSource ] amount: 1.2
 -> [ CoanTopping ] amount: 1.2
--- Pizza 2 ---
[ PizzaFactoryB ] Constructor
 -> ( AbstractPizzaFactory ) Constructor
---------------
( AbstractPizzaFactory ) Method make_pizza()
 -> [ PizzaFactoryB ] Method add_dough()
     -> ( Dough ) Constructor
 -> [ PizzaFactoryB ] Method add_source()
     -> ( Source ) Constructor
 -> [ PizzaFactoryB ] Method add_topping()
     -> ( Topping ) Constructor
---------------
( AbstractPizzaFactory ) Method check_pizza()
 -> [ RiceFlourDough ] amount: 1.0
 -> [ BasilSource ] amount: 1.0
 -> [ CheeseTopping ] amount: 1.0
```


ただし, この実装には以下の 3 つの欠点が存在する. 

1. ファクトリーのインスタンスについては実際に生成する必要が無い. 
1. 抽象ファクトリーと具象ファクトリーのコードがほとんど同じである. 
1. 最上位の名前空間にすべてのクラスが含まれる. 

### Python らしい書き方
Python らしく実装する方法として, クラス内クラスを利用する方法がある. 
各具象ファクトリー専用の具象プロダクトをクラス内にネストすることで, 最上位の名前空間に存在するクラスの数を減らすことができる. 

<p align="center">
  <img src="./assets/ClassDiagram/sample_pythonic.png" width="90%">
<p>

```shell
$ python3 src/main_pythonic.py
--- Pizza 1 ---
Func make_pizza()
 -> [ PizzaFactoryA ] Constructor
 -> [ PizzaFactoryA ] Method add_dough()
     -> [ PizzaFactoryA / WheatDough ] Constructor
 -> [ PizzaFactoryA ] Method add_source()
     -> [ PizzaFactoryA / TomatoSource ] Constructor
 -> [ PizzaFactoryA ] Method add_topping()
     -> [ PizzaFactoryA / CoanTopping ] Constructor
---------------
[ PizzaFactoryA ] Method check_pizza()
 -> [ PizzaFactoryA / WheatDough ] amount: 1.2
 -> [ PizzaFactoryA / TomatoSource ] amount: 1.2
 -> [ PizzaFactoryA / CoanTopping ] amount: 1.2
--- Pizza 2 ---
Func make_pizza()
 -> [ PizzaFactoryB ] Constructor
 -> [ PizzaFactoryB ] Method add_dough()
     -> [ PizzaFactoryB / RiceFlourDough ] Constructor
 -> [ PizzaFactoryB ] Method add_source()
     -> [ PizzaFactoryB / BasilSource ] Constructor
 -> [ PizzaFactoryB ] Method add_topping()
     -> [ PizzaFactoryB / CheeseTopping ] Constructor
---------------
[ PizzaFactoryB ] Method check_pizza()
 -> [ PizzaFactoryB / RiceFlourDough ] amount: 1.0
 -> [ PizzaFactoryB / BasilSource ] amount: 1.0
 -> [ PizzaFactoryB / CheeseTopping ] amount: 1.0
```
