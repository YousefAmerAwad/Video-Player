from kivy.app import App
from kivy.uix.video import Video

class MyApp(App):
    def build(self):
        self.title = 'Video Player'
        video = Video(source='vid.mp4')
        video.state = 'play'
        video.options={'eos':'loop'}
        video.allow_stretch =  True
        return video
