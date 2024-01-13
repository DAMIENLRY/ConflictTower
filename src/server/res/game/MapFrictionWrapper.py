from typing import List


class MapFrictionWrapper:
    """
    The MapFrictionWrapper class manages the UX.

    Attributes:
        _instance (MapFrictionWrapper): Singleton instance of MapFrictionWrapper
    """
    _instance = None

    def __new__(cls, *args, **kwargs) -> 'MapFrictionWrapper':
        """
        Singleton pattern implementation for MapFrictionWrapper class.

        Returns:
            MapFrictionWrapper: The singleton instance of MapFrictionWrapper
        """
        if not cls._instance:
            cls._instance = super(MapFrictionWrapper, cls).__new__(cls)
            cls._instance.map_friction = []
            cls._instance.map_imgs = []
            cls._instance.life_side_1 = 0
            cls._instance.life_side_2 = 0
            cls._instance.countdown = 0
        return cls._instance

    def __init__(self, arbiter) -> None:
        """
        Initializes the MapFrictionWrapper instance.

        Args:
            arbiter: The Arbiter instance to communicate with the game.
        """
        self.arbiter = arbiter
        
    def afficher_temps(self) -> str:
        """
        Converts countdown time to a formatted string.

        Returns:
            str: The formatted time string (e.g., "5:30")
        """
        minutes, secondes = divmod(self.countdown, 60)
        return f"{minutes}:{secondes:02}"
    
    def get_status_bar(self) -> str:
        """
        Retrieves the current status bar information.

        Returns:
            str: The status bar information string.
        """
        return f"💗 {self.life_side_1} - {self.life_side_2} ⌛ {self.afficher_temps()}"

    def init_status_bar(self) -> None:
        """
        Initializes the status bar in the game with the current information.
        """
        self.arbiter.ruleArena("info", self.get_status_bar())

    def update_status_bar(self, name, value, side=1) -> None:
        """
        Updates the status bar with the specified information.

        Args:
            name (str): The type of information to update ("life" or "countdown").
            value: The new value for the specified information.
            side (int): The side for which the information is being updated.
        """
        match name:
            case "life":
                if side == 1: self.life_side_1 = value
                if side == 2: self.life_side_2 = value
            case "countdown":
                self.countdown = value
        self.arbiter.ruleArena("info", self.get_status_bar())

    def add_friction(self, friction_index, friction_collision, image_url) -> None:
        """
        Adds friction information to the map.

        Args:
            friction_index (int): The index of the friction.
            friction_collision: The collision information for the friction.
            image_url (str): The URL of the image associated with the friction.
        """
        while len(self.map_friction) <= friction_index:
            self.map_friction.append(0)
        self.map_friction[friction_index] = friction_collision

        while len(self.map_imgs) <= friction_index:
            self.map_imgs.append("")

        self.map_imgs[friction_index] = image_url

        # Update the configuration via arbiter.ruleArena
        self.arbiter.ruleArena("mapFriction", self.map_friction)
        self.arbiter.ruleArena("mapImgs", self.map_imgs)

    def get_map_friction(self) -> List[int]:
        """
        Retrieves the current map friction information.

        Returns:
            list: List containing the map friction information.
        """
        return self.map_friction

    def get_map_imgs(self) -> List[str]:
        """
        Retrieves the URLs of the images associated with map frictions.

        Returns:
            list: List containing the image URLs.
        """
        return self.map_imgs
    
    def get_time(self) -> int:
        """
        Retrieves the current countdown time.

        Returns:
            int: The current countdown time.
        """
        return self.countdown
