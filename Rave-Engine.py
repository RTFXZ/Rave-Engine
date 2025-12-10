# Rave-Engine.py
import time
import json

class GameEngine:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.objects = []
        self.running = True

    def add_object(self, obj):
        self.objects.append(obj)

    def update(self, delta_time):
        for obj in self.objects:
            if hasattr(obj, 'update'):
                obj.update(delta_time)

    def get_state(self):
        return {
            'width': self.width,
            'height': self.height,
            'objects': [obj.to_dict() for obj in self.objects if hasattr(obj, 'to_dict')]
        }

class GameObject:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def to_dict(self):
        return {'x': self.x, 'y': self.y, 'width': self.width, 'height': self.height}

    def update(self, delta_time):
        # example: move right at 10 units/second
        self.x += 10 * delta_time

if __name__ == '__main__':
    engine = GameEngine()
    engine.add_object(GameObject(0, 0, 32, 32))

    last = time.time()
    try:
        while engine.running:
            now = time.time()
            dt = now - last
            last = now
            engine.update(dt)
            print(json.dumps(engine.get_state(), indent=None))
            time.sleep(0.1)
    except KeyboardInterrupt:
        print('Shutting down.')
