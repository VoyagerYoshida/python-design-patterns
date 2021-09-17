final class Config {
    public static let shared: Config =  Config() // 2 (static 変数なのでオブジェクト生成前にアクセス可能)
    private (set) public var modelName: String = "YOLO" // 様々なクラスで共通して使用したい変数. setter のみ private にしている
    
    // 1 (private なので, 外部からオブジェクトを生成しようとするとエラーになる)
    private init() {}
}

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

print(Config.shared.modelName)

var caller0 = Caller0()
print(caller0.getModelName())

var caller1 = Caller1()
print(caller1.getModelName())

Config()
