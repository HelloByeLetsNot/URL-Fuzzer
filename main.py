import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import ttk
import requests
from ttkthemes import ThemedTk
import os

class URLFuzzerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("URL Fuzzer")

        # Apply dark theme
        self.root.set_theme("plastik")

        # URL entry
        ttk.Label(root, text="URL:").grid(row=0, column=0, padx=10, pady=10)
        self.url_entry = ttk.Entry(root, width=50)
        self.url_entry.grid(row=0, column=1, padx=10, pady=10)

        # Wordlist file selection from dropdown
        ttk.Label(root, text="Wordlist:").grid(row=1, column=0, padx=10, pady=10)
        self.wordlist_combo = ttk.Combobox(root, values=self.get_wordlists(), width=47)
        self.wordlist_combo.grid(row=1, column=1, padx=10, pady=10)

        # Fuzz button
        ttk.Button(root, text="Start Fuzzing", command=self.start_fuzzing).grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Result display
        self.result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20, bg="#333333", fg="#ffffff", insertbackground="white")
        self.result_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def get_wordlists(self):
        try:
            response = requests.get("https://api.github.com/repos/danielmiessler/SecLists/contents/Fuzzing")
            response.raise_for_status()
            files = response.json()
            wordlists = [file['name'] for file in files if file['type'] == 'file']
            return wordlists
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load wordlists: {e}")
            return []

    def download_wordlist(self, wordlist_name):
        try:
            url = f"https://raw.githubusercontent.com/danielmiessler/SecLists/master/Fuzzing/{wordlist_name}"
            response = requests.get(url)
            response.raise_for_status()
            wordlist_path = os.path.join("/tmp", wordlist_name)
            with open(wordlist_path, 'w') as file:
                file.write(response.text)
            return wordlist_path
        except Exception as e:
            messagebox.showerror("Error", f"Failed to download wordlist: {e}")
            return None

    def start_fuzzing(self):
        url = self.url_entry.get()
        selected_wordlist = self.wordlist_combo.get()

        if not url or not selected_wordlist:
            messagebox.showerror("Error", "Please enter a URL and select a wordlist.")
            return

        wordlist_path = self.download_wordlist(selected_wordlist)
        if not wordlist_path:
            return

        try:
            with open(wordlist_path, 'r') as file:
                wordlist = file.readlines()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read wordlist file: {e}")
            return

        self.result_text.delete(1.0, tk.END)
        for word in wordlist:
            word = word.strip()
            fuzzed_url = url.replace("FUZZ", word)
            try:
                response = requests.get(fuzzed_url)
                result = f"{fuzzed_url} - {response.status_code}\n"
            except Exception as e:
                result = f"{fuzzed_url} - Error: {e}\n"
            self.result_text.insert(tk.END, result)
            self.result_text.yview(tk.END)

if __name__ == "__main__":
    root = ThemedTk(theme="plastik")
    app = URLFuzzerApp(root)
    root.mainloop()