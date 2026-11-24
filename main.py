from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.utils import platform
import os, re

try:
    import fitz  # PyMuPDF
    HAS_FITZ = True
except ImportError:
    HAS_FITZ = False

PATTERNS = [
    (r'\b(LINE|L)[- ]?\d{1,2}[- ]?\d{1,3}[- ]?\d{2,4}\b', 'Line'),
    (r'\b(FI|FT|FC|FIC|PI|PT|PIC|TI|TT|TIC|LI|LT|LIC|AI|AT|AIC|XV|PV|FV|LV|TV|PSV|PRV|CV)[- ]?\d{1,4}[A-Z]?\b', 'Instrument'),
    (r'\b(EQP|EQ|PUMP|PMP|HEX|TNK|TANK|VESSEL|COMP|MTR|MOTOR|P-|E-|V-|K-|M-|C-)\d{1,4}[A-Z]?\b', 'Equipment'),
]

class PIDExtractor(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)
        self.status = Label(text="Select a PDF P&ID file to begin.",
                            size_hint_y=None, height=60, text_size=(None, None))
        self.add_widget(self.status)

        btn = Button(text="📁 Choose PDF", size_hint_y=None, height=60,
                     background_color=(0.2, 0.6, 0.8, 1))
        btn.bind(on_press=self.show_file_chooser)
        self.add_widget(btn)

        self.scroll = ScrollView()
        self.results = BoxLayout(orientation='vertical', size_hint_y=None)
        self.results.bind(minimum_height=self.results.setter('height'))
        self.scroll.add_widget(self.results)
        self.add_widget(self.scroll)

    def show_file_chooser(self, instance):
        if not HAS_FITZ:
            self.status.text = "❌ PyMuPDF missing. Check build."
            return
        content = BoxLayout(orientation='vertical')
        fc = FileChooserListView(filters=['*.pdf'])
        content.add_widget(fc)
        bar = BoxLayout(size_hint_y=None, height=50)
        cancel = Button(text="Cancel")
        ok = Button(text="Select")
        bar.add_widget(cancel); bar.add_widget(ok)
        content.add_widget(bar)
        popup = Popup(title="Select P&ID PDF", content=content, size_hint=(0.95, 0.95))
        cancel.bind(on_press=popup.dismiss)
        ok.bind(on_press=lambda x: self.load_pdf(fc.selection, popup))
        popup.open()

    def load_pdf(self, selection, popup):
        popup.dismiss()
        if not selection:
            return
        path = selection[0]
        self.status.text = f"Processing {os.path.basename(path)}..."
        self.results.clear_widgets()
        try:
            doc = fitz.open(path)
            text = "\n".join(p.get_text() for p in doc)
            doc.close()
            if len(text.strip()) < 50:
                self.status.text = "No embedded text (scanned PDF)."
                return
            tags = self.extract_tags(text)
            self.display(tags)
            self.status.text = f"✅ Found {len(tags)} tags."
        except Exception as e:
            self.status.text = f"Error: {e}"

    def extract_tags(self, text):
        found = set()
        for line in text.split('\n'):
            line = line.strip()
            if not line: continue
            for pattern, cat in PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    found.add(f"[{cat}] {line}")
                    break
        return sorted(found)

    def display(self, tags):
        self.results.clear_widgets()
        if not tags:
            self.results.add_widget(Label(text="No P&ID tags found.",
                                          size_hint_y=None, height=40))
            return
        for t in tags:
            lbl = Label(text=t, size_hint_y=None, height=40,
                        halign='left', valign='middle')
            lbl.bind(size=lbl.setter('text_size'))
            self.results.add_widget(lbl)

class PIDApp(App):
    def build(self):
        Window.clearcolor = (0.05, 0.1, 0.15, 1)
        return PIDExtractor()

if __name__ == '__main__':
    PIDApp().run()