"""
Name: Jihun Park
Date: 05/01/2019
Brief Project Description: This is a Graphical User Interface (GUI) program to add and learn songs using kivy.
GitHub URL: https://github.com/JihunPark98/CP1404Practical/tree/feedback/A2
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from songlist import SongList


class SongsList(App):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        self.song_list = SongList()

        self.top_label = Label(text="", id="count_label")
        self.status_label = Label(text="")
        self.sort_label = Label(text="Sort by:")
        self.spinner = Spinner(text='Artist', values=('Artist', 'Title', 'Year', 'Required'))
        self.add_song_label = Label(text="Add New Song...")
        self.title_label = Label(text="Title:")
        self.title_text_input = TextInput(write_tab=False, multiline=False)
        self.artist_label = Label(text="Artist:")
        self.artist_text_input = TextInput(write_tab=False, multiline=False)
        self.year_label = Label(text="Year:")
        self.year_text_input = TextInput(write_tab=False, multiline=False)
        self.add_song_button = Button(text='Add Song')
        self.clear_button = Button(text='Clear')

    def songs_sort(self, *args):
        self.song_list.sort(self.spinner.text)
        self.root.ids.rightLayout.clear_widgets()
        self.right_widgets()

    def build(self):
        self.title = "Songs List 2.0"
        self.root = Builder.load_file('app.kv')
        self.song_list.load_songs()
        self.song_list.sort('Artist')
        self.building_widgets()
        self.right_widgets()
        return self.root

    def building_widgets(self):
        self.root.ids.leftLayout.add_widget(self.sort_label)
        self.root.ids.leftLayout.add_widget(self.spinner)
        self.root.ids.leftLayout.add_widget(self.add_song_label)
        self.root.ids.leftLayout.add_widget(self.title_label)
        self.root.ids.leftLayout.add_widget(self.title_text_input)
        self.root.ids.leftLayout.add_widget(self.artist_label)
        self.root.ids.leftLayout.add_widget(self.artist_text_input)
        self.root.ids.leftLayout.add_widget(self.year_label)
        self.root.ids.leftLayout.add_widget(self.year_text_input)
        self.root.ids.leftLayout.add_widget(self.add_song_button)
        self.root.ids.leftLayout.add_widget(self.clear_button)
        self.root.ids.topLayout.add_widget(self.top_label)
        self.spinner.bind(text=self.songs_sort)
        self.add_song_button.bind(on_release=self.add_song_handler)
        self.clear_button.bind(on_release=self.clear_fields)

    def right_widgets(self):
        self.top_label.text = "To learn: " + str(self.song_list.get_required_songs_count()) + ". Learned: " + str(
            self.song_list.get_learned_songs_count())
        for song in self.song_list.songs:
            if song[0].status == 'n':
                song_button = Button(text='"' + song[0].title + '"' + " by " + song[0].artist + " (" + str(
                    song[0].year) + ") " "(Learned)", id=song[0].title)
                song_button.background_color = [88, 89, 0, 0.3]
            else:
                song_button = Button(
                    text='"' + song[0].title + '"' + " by " + song[0].artist + " (" + str(song[0].year) + ")",
                    id=song[0].title)
                song_button.background_color = [0, 88, 88, 0.3]
            song_button.bind(on_release=self.click_handler)
            self.root.ids.rightLayout.add_widget(song_button)

    def click_handler(self, button):
        if self.song_list.get_song(button.id).status == 'n':
            self.song_list.get_song(button.id).status = 'y'
            self.root.ids.bottomLayout.text = "You need to learn " + str(self.song_list.get_song(button.id).title)
        else:
            self.song_list.get_song(button.id).status = 'n'
            self.root.ids.bottomLayout.text = "You have learned " + str(self.song_list.get_song(button.id).title)
        self.songs_sort()
        self.root.ids.rightLayout.clear_widgets()
        self.right_widgets()

    def clear_fields(self, *args):
        self.title_text_input.text = ""
        self.artist_text_input.text = ""
        self.year_text_input.text = ""
        self.root.ids.bottomLayout.text = ""

    def add_song_handler(self, *args):
        if str(self.title_text_input.text).strip() == '' or str(self.artist_text_input.text).strip() == '' or str(
                self.year_text_input.text).strip() == '':
            self.root.ids.bottomLayout.text = "All fields must be completed"
        else:
            try:
                if int(self.year_text_input.text) < 0:
                    self.root.ids.bottomLayout.text = "Please enter a valid number"
                else:
                    self.song_list.add_song(self.title_text_input.text, self.artist_text_input.text,
                                            int(self.year_text_input.text))
                    self.song_list.sort(self.spinner.text)
                    self.clear_fields()
                    self.root.ids.rightLayout.clear_widgets()
                    self.right_widgets()
            except ValueError:
                self.root.ids.bottomLayout.text = "Please enter a valid number"

    def stop(self):
        self.song_list.save_file()

if __name__ == '__main__':
    app = SongsList()
    app.run()
