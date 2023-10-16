import PySimpleGUI as sg
import base64

class MainApp:
	def __init__(self):
		sg.change_look_and_feel("Dark")
		layout = [
			[sg.Text("Text to Encode/Decode", size=(15,0))],
			[sg.Multiline(size=(50,7), key="target_text")],
			[sg.Radio("Base64", "base_type", key="bs64"), sg.Radio("Base32", "base_type", key="bs32")],
			[sg.Button("Encode", key="encode"), sg.Button("Decode", key="decode")],
			[sg.Multiline("No Results", key="-OUTPUT-", disabled=True, size=(50,7))]
		]

		self.window = sg.Window("Base Encoder", size=(450,300)).layout(layout)

	def start(self):
		while True:
			self.event, self.values = self.window.Read()
			bs64 = self.values["bs64"]
			bs32 = self.values["bs32"]
			target_text = self.values["target_text"]
			if "encode" in self.event:
				if target_text is not None:
					plain_text_bytes = target_text.encode("UTF-8")
					if bs64:
						bs64_encoded = base64.b64encode(plain_text_bytes).decode("UTF-8")
						self.window["-OUTPUT-"].update(bs64_encoded)
					elif bs32:
						bs32_encoded = base64.b32encode(plain_text_bytes).decode("UTF-8")
						self.window["-OUTPUT-"].update(bs32_encoded)
			elif "decode" in self.event:
				if target_text is not None:
					if bs64:
						bs64_decoded = base64.b64decode(target_text).decode()
						self.window["-OUTPUT-"].update(bs64_decoded)
					elif bs32:
						bs32_decoded = base64.b32decode(target_text).decode()
						self.window["-OUTPUT-"].update(bs32_decoded)

main_window = MainApp()
main_window.start()
