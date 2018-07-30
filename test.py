import abc
# 各版都繼承這個父類別
class Section(abc.ABC):
    # 初始化各版的名字和訂閱者列表
    def __init__(self, name):
        self.name = name
        self.subscriberList = []
    # 新增訂閱者
    def attach(self, subscriber):
        for i in self.subscriberList:
            if i.getName() == subscriber.getName():
                print('Subscriber was already exist!!')
                return 0
        self.subscriberList.append(subscriber)
        subscriber.addSection(self.name)
        return 0
    # 移除訂閱者
    def detach(self, subscriber):
        for i in self.subscriberList:
            if i.getName() == subscriber.getName():
                self.subscriberList.remove(i)
                subscriber.removeSection(self.name)
                return 0
        print('Subscriber didn\'t exist!!')
        return 0
    #發佈消息
    def notify(self):
        print('{}版有一則新的消息'.format(self.name))
        print(self.getNews())
        for i in self.subscriberList:
            i.update(self.name)
        return 0
    #取得新聞(抽象)
    @abc.abstractmethod
    def getNews(self):
        return NotImplemented

# 體育版
class Sport(Section):
    def __init__(self, news = 'Nothing new'):
        super(Sport, self).__init__('Sport')
        self.news = news
    #取得新聞
    def getNews(self):
        return self.news
    #設定新聞
    def setNews(self, paragraph):
        self.news = paragraph
# 科技版
class Tech(Section):
    def __init__(self, news = 'Nothing new'):
        super(Tech, self).__init__('Tech')
        self.news = news
    #取得新聞
    def getNews(self):
        return self.news
    #設定新聞
    def setNews(self, paragraph):
        self.news = paragraph
# 娛樂版
class Entertainment(Section):
    def __init__(self, news = 'Nothing new'):
        super(Entertainment, self).__init__('Entertainment')
        self.news = news
    #取得新聞
    def getNews(self):
        return self.news
    #設定新聞
    def setNews(self, paragraph):
        self.news = paragraph

# 訂閱者
class Subscriber:
    def __init__(self, name):
        self.name = name
        self.subscribeList = []
    # 取得訂閱者名字
    def getName(self):
        return self.name
    # 增加訂閱列表
    def addSection(self, section):
        for i in self.subscribeList:
            if i == section:
                print('{} is already subscribed {}!'.format(self.name, i))
                return 0
        self.subscribeList.append(section)
    # 移除訂閱列表
    def removeSection(self, section):
        for i in self.subsribeList:
            if i == section:
                self.subscribeList.remove(i)
                return 0
        print('{} is not in subscribe list!'.format(i))
    # 更新消息
    def update(self, section):
        print('{} had recieved a news from {}'.format(self.name, section))
    # 印出訂閱列表
    def getSubscribeList(self):
        print('{} have subscribed ↓'.format(self.name))
        for i in self.subscribeList:
            print(i)


# 測試
# 水果公司 0: 體育版 1:科技版 2:娛樂版
# fruitPaper =[Sport(),Tech(),Entertainment()]
# # 訂閱者 Tom Ben Alex Brian
# Tom = Subscriber('Tom')
# Ben = Subscriber('Ben')
# Alex = Subscriber('Alex')
# Brian = Subscriber('Brian')
# # 設置新聞
# fruitPaper[0].setNews('瓊斯盃邀請賽 台灣贏韓國啦!!!!')
# fruitPaper[1].setNews('王小明發佈新書-Python從入門到放棄')
# fruitPaper[2].setNews('一日幕僚觀看數破800萬啦!!!')
# # Tom 訂閱 體育版 科技版
# # Ben 訂閱 體育版
# # Alex 訂閱 體育版 科技版 娛樂版
# # Brian 訂閱 娛樂版
# fruitPaper[0].attach(Tom)
# fruitPaper[0].attach(Ben)
# fruitPaper[0].attach(Alex)
# fruitPaper[1].attach(Tom)
# fruitPaper[1].attach(Alex)
# fruitPaper[2].attach(Alex)
# fruitPaper[2].attach(Brian)
# # 體育版發佈消息
# fruitPaper[0].notify()
# # 科技版發佈消息
# fruitPaper[1].notify()
# # 娛樂版發佈消息
# fruitPaper[2].notify()
# print()
# # 取得訂閱列表
# Tom.getSubscribeList()

a = [0,1,2,3,4,0,0,0,1,2,3,4,0,1,2,3,4,5]
for i in a:
    print(i)
    try:
        a.remove(0)

    except ValueError:
        pass
print(a)
