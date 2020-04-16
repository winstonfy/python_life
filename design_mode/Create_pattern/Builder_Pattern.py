#__author__ = 'Winston'
#date: 2020/3/26

# 将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。

from abc import ABCMeta,abstractmethod

class Player:
    def __init__(self,face = None,body = None,arm = None,leg = None):
        self.face = face
        self.body = body
        self.arm = arm
        self.leg = leg

    def __str__(self):
        return "%s, %s, %s, %s"%(self.face,self.body,self.arm,self.leg)

class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def builder_face(self):
        pass

    @abstractmethod
    def builder_body(self):
        pass

    @abstractmethod
    def builder_arm(self):
        pass

    @abstractmethod
    def builder_leg(self):
        pass

    @abstractmethod
    def get_player(self):
        pass

class BeautyBuilder(PlayerBuilder):

    def __init__(self):
        self.player = Player()

    def builder_face(self):
        self.player.face = '漂亮脸蛋'

    def builder_arm(self):
        self.player.arm = '细胳膊'

    def builder_body(self):
        self.player.body = '苗条细腰'

    def builder_leg(self):
        self.player.leg = '长腿'

    def get_player(self):
        return self.player

class PlayerDirector:
    def build_player(self,builder):
        builder.builder_body()
        builder.builder_face()
        builder.builder_arm()
        builder.builder_leg()
        return builder.get_player()

pd = PlayerDirector()
pb = BeautyBuilder()
p = pd.build_player(pb)
print(p)


# 角色：
# 抽象建造者（Builder）
# 具体建造者（Concrete Builder）
# 指挥者（Director）
# 产品（Product）

# 建造者模式与抽象工厂模式相似，也用来创建复杂对象。
# 主要区别是建造者模式着重一步步构造一个复杂对象，而抽象工厂模式着重于多个系列的产品对象。

# 适用场景
# 当创建复杂对象的算法（Director）应该独立于该对象的组成部分以及它们的装配方式（Builder）时
# 当构造过程允许被构造的对象有不同的表示时（不同Bullder）。

# 优点：
# 隐藏了一个产品的内部结构和装配过程
# 将构造代码与表示代码分开
# 可以对构造过程进行更精细的控制
