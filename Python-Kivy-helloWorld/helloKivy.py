from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class HelloKivy(App):
  helloOrKivy = True
  
  def build(self):
    f = FloatLayout()
    
    self.l = Label(text='Hello', font_size=75, valign='top', size_hint=(1,.5))
    labelAnch = AnchorLayout(anchor_x='center', anchor_y='top')
    labelAnch.add_widget(self.l)
    
    b = Button(text='clicky', font_size=75, size_hint=(1,.5), on_press=self.callback)
    buttonAnch = AnchorLayout(anchor_x='center', anchor_y='bottom')
    buttonAnch.add_widget(b)
    f.add_widget(labelAnch)
    f.add_widget(buttonAnch)
    return f
  
  def callback(self, event):
      if self.helloOrKivy:
        self.l.text = 'Kivy'
        self.helloOrKivy = False
      else:
        self.l.text = 'Hello'
        self.helloOrKivy = True
    
    
if __name__ == "__main__":
  HelloKivy().run()