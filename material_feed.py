from klipper import config
from klipper.device import GPIO

class MaterialFeed:

    def __init__(self, up_pin, down_pin, feed_pin):

        self.up_sensor = GPIO(up_pin, "in", pull_up=True)
        self.down_sensor = GPIO(down_pin, "in", pull_up=True)
        self.feed_signal = GPIO(feed_pin, "out")
        self.feeding = False

    # Инициализируем подачу материала
    self.feed_signal.write(0)

    def check_sensors(self):
        up_state = self.up_sensor.read()
        down_state = self.down_sensor.read()

    # Если нижний датчик сработал - начинаем подачу
    if not down_state and not self.feeding:
        self.start_feeding()

    # Если верхний датчик сработал - останавливаем подачу
    if not up_state and self.feeding:
        self.stop_feeding()
        
    def start_feeding(self):
        self.feed_signal.write(1) # Включаем подачу
        self.feeding = True
        print("Подача начата.")

    def stop_feeding(self):
        self.feed_signal.write(0) # Отключаем подачу
        self.feeding = False
        print("Подача остановлена.")

    # Создаем экземпляр модуля с подключенными пинами
    material_feed = MaterialFeed(config['material_feed']['pin_up_sensor'],
                                 config['material_feed']['pin_down_sensor'],
                                 config['material_feed']['pin_feed'])

    # Проверяем состояние датчиков в цикле (можно вызов делать раз в секунду)
    while True:
        material_feed.check_sensors()