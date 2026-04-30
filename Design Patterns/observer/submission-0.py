class Observer(ABC):
    @abstractmethod
    def notify(self, itemName: str) -> None:
        pass

class Customer(Observer):
    def __init__(self, name: str) -> None:
        self.name = name
        self.notifications = 0

    def notify(self, itemName: str) -> None:
        self.notifications += 1

    def countNotifications(self) -> int:
        return self.notifications

class OnlineStoreItem:
    def __init__(self, itemName: str, stock: int) -> None:
        self.itemName = itemName
        self.stock = stock
        self.subscribed=set()

    def subscribe(self, observer: Observer) -> None:
        self.subscribed.add(observer)

    def unsubscribe(self, observer: Observer) -> None:
        self.subscribed.remove(observer)

    def updateStock(self, newStock: int) -> None:
        if self.stock==0:
            call=True
        else:
            call=False
        self.stock=newStock
        if call:
            for customer in self.subscribed:
                customer.notify(self.itemName)
                customer.countNotifications()
