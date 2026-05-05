from pygame import mixer
from pygame.mixer import Sound

mixer.init()

class Bg_music():
    """背景音乐"""
    def __init__(self):
        self.sound = mixer.Sound('music/riya - 小さなてのひら (小小的手心).mp3')
        self.sound.set_volume(0.5)  # 设置音量为50%

class Shoot_sound():
    """射击声音"""
    def __init__(self):
        self.sound = mixer.Sound('music/shoot_sound.mp3')
        self.sound.set_volume(0.5)  # 设置音量为50%
        

        
