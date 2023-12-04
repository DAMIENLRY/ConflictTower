class MapFrictionWrapper:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MapFrictionWrapper, cls).__new__(cls)
            cls._instance.map_friction = []
            cls._instance.map_imgs = []
        return cls._instance

    def __init__(self, arbitre):
        self.arbitre = arbitre

    def add_friction(self, frictionIndex, frictionCollision, imageURL):
        while len(self.map_friction) <= frictionIndex:
            self.map_friction.append(0)
        self.map_friction[frictionIndex] = frictionCollision

        while len(self.map_imgs) <= frictionIndex:
            self.map_imgs.append("")

        self.map_imgs[frictionIndex] = imageURL

    def get_map_friction(self):
        return self.map_friction

    def get_map_imgs(self):
        return self.map_imgs
