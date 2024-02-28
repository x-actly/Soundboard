import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from pygame import mixer
import configparser
import os

class SoundboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Soundboard by x-actly")
        self.root.geometry("630x100")
        self.root.resizable(False, False)
        self.root.configure(bg="#4f5d75")

        mixer.init()

        self.config_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "config.ini")

        self.buttons = []
        self.load_config()
        for i in range(2):
            for j in range(6):
                button_name = tk.StringVar()
                button_name.set(f"Button {i * 6 + j + 1}")
                button = tk.Button(root, textvariable=button_name, command=lambda idx=i * 6 + j: self.play_sound(idx), width=10, height=2, borderwidth=2, relief=tk.GROOVE, bg="#2d3142", fg="#ffffff")
                button.grid(row=i, column=j, padx=5, pady=5)
                button.bind("<Button-3>", lambda event, idx=i * 6 + j, name_var=button_name: self.configure_button(event, idx, name_var))
                self.buttons.append({"button": button, "name": button_name, "sound_file": None})

        load_button = tk.Button(root, text="Load Config", command=self.load_config, relief=tk.GROOVE, width=10, height=2, bg="#2d3142", fg="#ffffff")
        load_button.grid(row=0, column=6, padx=5, pady=5)
        load_button.bind("<Button-1>", lambda event: self.load_config_from_file())

        save_button = tk.Button(root, text="Save Config", command=self.save_config, relief=tk.GROOVE, width=10, height=2, bg="#2d3142", fg="#ffffff")
        save_button.grid(row=1, column=6, padx=5, pady=5)
        save_button.bind("<Button-1>", lambda event: self.save_config_as())

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def play_sound(self, idx):
        sound_file = self.buttons[idx]["sound_file"]
        if sound_file:
            try:
                mixer.music.load(sound_file)
                mixer.music.play()
            except pygame.error as e:
                print(f"Error loading soundfile: {e}")

    def configure_button(self, event, idx, name_var):
        new_name = simpledialog.askstring("Button Configuration", f"Set a new button name {idx+1} :", initialvalue=name_var.get())
        if new_name:
            name_var.set(new_name)

        selected_file = filedialog.askopenfilename(filetypes=[("Sound files", ("*.mp3", "*.wav"))])
        if selected_file:
            self.buttons[idx]["sound_file"] = selected_file
            print(f"Soundfile für Button {idx+1} zugewiesen: {selected_file}")

    def on_closing(self):
        self.save_config()
        self.root.destroy()

    def save_config(self, event=None):
        self.save_config_to_file(self.config_file_path)
        # Set visual state of button
        self.reset_button_state()

    def reset_button_state(self):
        for button_data in self.buttons:
            button_data["button"].configure(relief=tk.GROOVE)

    def save_config_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".ini", filetypes=[("INI files", "*.ini")])
        if file_path:
            self.save_config_to_file(file_path)

    def save_config_to_file(self, file_path):
        config = configparser.ConfigParser()

        for i, button_data in enumerate(self.buttons):
            section_name = f"Button_{i + 1}"
            sound_file = button_data["sound_file"] if button_data["sound_file"] is not None else ""

            # Set section if its not still created 
            if not config.has_section(section_name):
                config.add_section(section_name)

            config.set(section_name, "name", button_data["name"].get())
            config.set(section_name, "sound_file", sound_file)

        try:
            with open(file_path, "w") as configfile:
                config.write(configfile)
            print(f"Configuration saved to {file_path}")
        except Exception as e:
            print(f"Error writing config file: {e}")

    def load_config(self, file_path=None):
        if file_path is None:
            file_path = self.config_file_path
        config = configparser.ConfigParser()

        try:
            with open(file_path, "r") as configfile:
                config.read_file(configfile)

            for i, button_data in enumerate(self.buttons):
                section_name = f"Button_{i + 1}"
                if config.has_section(section_name):
                    button_data["name"].set(config.get(section_name, "name"))
                    sound_file = config.get(section_name, "sound_file")
                    button_data["sound_file"] = sound_file if sound_file != "" else None
                    print(f"Loaded config for Button {i+1}: Name={button_data['name'].get()}, Sound_file={button_data['sound_file']}")
        except (FileNotFoundError, configparser.Error) as e:
            print(f"Error loading config file: {e}")

    def load_config_from_file(self, event=None):
        selected_file = filedialog.askopenfilename(filetypes=[("INI files", "*.ini")])
        if selected_file:
            try:
                self.config_file_path = selected_file
                self.load_config(selected_file)
                self.reset_button_state()  # load reset button method
                messagebox.showinfo("Configuration loaded", f"The configuration has loaded from {selected_file}.")
            except Exception as e:
                messagebox.showerror("Error", f"Error loading configuration file: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SoundboardApp(root)
    root.mainloop()