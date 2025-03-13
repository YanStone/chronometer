from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.graphics import Color, RoundedRectangle

class RoundedButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (1, None)
        self.height = 50
        self.background_normal = ''  # Remove default background
        self.background_color = (0, 0, 0, 0)  # Transparent background
        
        with self.canvas.before:
            Color(0.2, 0.6, 0.8, 1)  # Button color
            self.rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[25, 25, 25, 25])
        
        self.bind(pos=self.update_rect, size=self.update_rect)
    
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class ChronometerApp(App):
    def build(self):
        self.time = 0
        self.running = False
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=30, size_hint=(None, None), size=(400, 400), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.label = Label(text='0.0', font_size=60, size_hint=(None, None), size=(200, 100), pos_hint={'center_x': 0.5})
        
        button_layout = BoxLayout(size_hint=(None, None), size=(320, 60), spacing=10, pos_hint={'center_x': 0.5})
        
        self.start_button = RoundedButton(text='Start', size_hint=(0.5, None))
        self.stop_button = RoundedButton(text='Stop', size_hint=(0.5, None))
        self.start_button.bind(on_press=self.start)
        self.stop_button.bind(on_press=self.stop)
        
        self.reset_button = RoundedButton(text='Reset', size_hint=(1, None), pos_hint={'center_y': 0})
        self.reset_button.bind(on_press=self.reset)
        
        button_layout.add_widget(self.start_button)
        button_layout.add_widget(self.stop_button)
        
        layout.add_widget(self.label)
        layout.add_widget(Widget(size_hint_y=None, height=50))  # Spacer to move buttons down
        layout.add_widget(button_layout)
        layout.add_widget(Widget(size_hint_y=None, height=20))  # Spacer between rows
        layout.add_widget(self.reset_button)
        layout.add_widget(Widget(size_hint_y=None, height=5))  # Push reset button to the bottom
        
        return layout
    
    def update_time(self, dt):
        self.time += dt
        self.label.text = f'{self.time:.1f}'
    
    def start(self, instance):
        if not self.running:
            self.running = True
            Clock.schedule_interval(self.update_time, 0.1)
    
    def stop(self, instance):
        self.running = False
        Clock.unschedule(self.update_time)
    
    def reset(self, instance):
        #self.running = False
        #Clock.unschedule(self.update_time)
        self.time = 0
        self.label.text = '0.0'
        
if __name__ == '__main__':
    ChronometerApp().run()
