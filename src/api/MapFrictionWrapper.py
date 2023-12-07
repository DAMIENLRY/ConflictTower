class MapFrictionWrapper:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MapFrictionWrapper, cls).__new__(cls)
            cls._instance.map_friction = []
            cls._instance.map_imgs = []
            cls._instance.copper = "🟠 0 - 0"
            cls._instance.life = "💗 0 - 0"
            cls._instance.countdown = "⌛ 0:00"
        return cls._instance

    def __init__(self, arbitre):
        self.arbitre = arbitre


    def init_status_bar(self):
        updatedStatus = f" {self.copper} {self.life} {self.countdown}"
        self.arbitre.ruleArena("info", updatedStatus)

    def update_status_bar(self, name, args):
        match name:
            case "copper":
                copper = f"🟠 {args[0]} - {args[1]}"
                updatedStatus = f" {copper} {self.life} {self.countdown}"
            case "life":
                life = f"💗 {args[0]} - {args[1]}"
                updatedStatus = f" {self.copper} {life} {self.countdown}"
            case "countdown":
                countdown = f"⌛ {args[0]}"
                updatedStatus = f" {self.copper} {self.life} {countdown}"
        self.arbitre.ruleArena("info", updatedStatus)

    def add_friction(self, frictionIndex, frictionCollision, imageURL):
        while len(self.map_friction) <= frictionIndex:
            self.map_friction.append(0)
        self.map_friction[frictionIndex] = frictionCollision

        while len(self.map_imgs) <= frictionIndex:
            self.map_imgs.append("")

        self.map_imgs[frictionIndex] = imageURL

        # Mise à jour de la configuration via arbitre.ruleArena
        self.arbitre.ruleArena("mapFriction", self.map_friction)
        self.arbitre.ruleArena("mapImgs", self.map_imgs)

    def get_map_friction(self):
        return self.map_friction

    def get_map_imgs(self):
        return self.map_imgs
