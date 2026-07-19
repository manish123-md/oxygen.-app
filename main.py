import time
import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window

# Android-specific commands ke liye dummy modules (Buildozer ise handle karega)
# Real hardware features ke liye jnius ka use hota hai
try:
    from jnius import autoclass
except ImportError:
    autoclass = None

# Jokes ki list jab assistant ko command samajh na aaye ya default function trigger ho
JOKES = [
    "Papa: Beta, phone pe kaun hai?\nPappu: Oxygen hai papa, bol rahi hai life support chahiye!",
    "Python ko thand kyun lagti hai? Kyunki usme bohot saare 'conditional clauses' hote hain!",
    "Doctor: Aapko oxygen ki kami hai.\nPatient: Sir, phone badal loon ya assistant?",
    "Why do programmers wear glasses? Because they can't C#!",
    "Computer se pucha- Tera baap kaun hai? Usne bola- Electricity!"
]

class DynamicIsland(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint = (None, None)
        
        # Ek smooth, rounded, semi-transparent pill shape setup
        self.size = (200, 50) 
        self.pos_hint = {'center_x': 0.5, 'top': 0.95}
        
        # Transparent background setup (Simulated here)
        self.label = Label(text="", color=(1, 1, 1, 1), font_size='14sp')
        self.add_widget(self.label)
        
        # Fake trigger just for testing (In real app, voice detection builds this loop)
        Clock.schedule_once(self.listen_for_wake_word, 2)

    def listen_for_wake_word(self, dt):
        # Yahan tumhara Speech Recognition system chalu hoga
        # Abhi ke liye hum pretend kar rahe hain ki 'Oxygen' bola gaya hai
        self.activate_island("Hey Master! whats going on...")

    def activate_island(self, message):
        self.label.text = message
        # Apple jaisa Dynamic Island expand animation
        anim = Animation(size=(350, 100), duration=0.4, t='out_quad')
        anim.bind(on_complete=self.process_command)
        anim.start(self)

    def process_command(self, instance, widget):
        # Default behavior: User ki baat sunne ke baad ek naya joke sunana
        time.sleep(2)  # Processing time simulation
        joke = random.choice(JOKES)
        self.label.text = joke
        
        # Joke dikhane ke 4 second baad island wapas chota hokar transparent ho jayega
        Clock.schedule_once(self.deactivate_island, 4)

    def deactivate_island(self, dt):
        anim = Animation(size=(0, 0), duration=0.4, t='in_quad')
        anim.start(self)

class OxygenAssistantApp(App):
    def build(self):
        # Window ko transparent banane ki koshish (Android transparent window theme)
        Window.clearcolor = (0, 0, 0, 0) 
        return DynamicIsland()

if __name__ == '__main__':
    OxygenAssistantApp().run()