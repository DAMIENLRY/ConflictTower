class MapFrictionWrapper:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MapFrictionWrapper, cls).__new__(cls)
            cls._instance.map_friction = []
            cls._instance.map_imgs = []
            cls._instance.lifeSide1 = 0
            cls._instance.lifeSide2 = 0
            cls._instance.countdown = 0
        return cls._instance

    def __init__(self, arbitre):
        self.arbitre = arbitre
        
    def afficher_temps(self):
        minutes, secondes = divmod(self.countdown, 60)
        return f"{minutes}:{secondes:02}"
    
    def get_status_bar(self):
        return f"💗 {self.lifeSide1} - {self.lifeSide2} ⌛ {self.afficher_temps()}"

    def init_status_bar(self):
        self.arbitre.ruleArena("info", self.get_status_bar())

    def update_status_bar(self, name, value, side=1):
        match name:
            case "life":
                if(side == 1): self.lifeSide1 = value
                if(side == 2): self.lifeSide2 = value
            case "countdown":
                self.countdown = value
        self.arbitre.ruleArena("info", self.get_status_bar())

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
    
    def get_time(self):
        return self.countdown
