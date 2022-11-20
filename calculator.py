from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class CalculatorDisplay(GridLayout):
	def get_value(self, val):
		print(f"the value of the key selected is {val}")

	def get_math_operator(self, operator):
		print(f"the operator you pressed was {operator}")

	def calculate(self, calculation):
		if calculation:
			try:
				self.display.text = str(eval(calculation))
			except Exception:
				self.display.text = "Error"

class CalculatorApp(App):
	pass

if __name__ =="__main__":
	CalculatorApp().run()
