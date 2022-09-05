from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.lang import Builder
from functions import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import cplot

Builder.load_file('main.kv')

class ScreenManagemer(ScreenManager):
	pass

class FirstScreen(Screen):
	pass


class SecondScreen(Screen):

	plot_exists = False

	def plot_func(self):
		if self.plot_exists == True:
			self.ids.layout_1.clear_widgets()
			plt.clf()
		try:
			self.ids.error_1.text = ""
			func_name = self.ids.comp_func_1.text
			plot_props = get_list(self.ids.axes_lims_nsteps_1.text, 3)
			x1, x2 = float(plot_props[0]), float(plot_props[1])
			nps = int(plot_props[2])
			xs, ys = plot_values(func_name, x1, x2, nps)
			plt.plot(xs, ys)
			canvas = FigureCanvasKivyAgg(plt.gcf(), pos_hint={'x': 0.25, 'y': 0.1}, size_hint=(0.5,0.5))
			self.ids.layout_1.add_widget(canvas)
			canvas.draw()
			self.plot_exists = True

		except Exception as e:
			self.ids.error_1.text = type(e).__name__

	def remove_plot(self):
		self.ids.error_1.text = ""
		self.ids.layout_1.clear_widgets()
		plt.clf()
		self.plot_exists = False

	def back_to_menu(self):
		self.ids.comp_func_1.text = ""
		self.ids.axes_lims_nsteps_1.text = ""
		self.ids.error_1.text = ""
		self.ids.layout_1.clear_widgets()
		plt.clf()
		app.root.current = "FirstScreen"

class ThirdScreen(Screen):

	plot_exists = False

	def plot_func(self):
		if self.plot_exists == True:
			self.ids.layout_2.clear_widgets()
			plt.clf()
		try: 
			self.ids.error_2.text = ""
			func_name = self.ids.comp_func_2.text
			plot_props = get_list(self.ids.axes_lims_nsteps_2.text, 5)
			x1, x2 = float(plot_props[0]), float(plot_props[1])
			y1, y2 = float(plot_props[2]), float(plot_props[3])
			nps = int(plot_props[4])
			xs, ys, zs = plot_values3d(func_name, x1, x2, y1, y2, nps)
			fig = plt.figure()
			ax = fig.add_subplot(111, projection='3d')
			ax.plot_surface(xs, ys, zs)
			canvas = FigureCanvasKivyAgg(plt.gcf(), pos_hint={'x': 0.25, 'y': 0.1}, size_hint=(0.5,0.5))
			self.ids.layout_2.add_widget(canvas)
			canvas.draw()
			self.plot_exists = True

		except Exception as e:
			self.ids.error_2.text = type(e).__name__

	def remove_plot(self):
		self.ids.error_2.text = ""
		self.ids.layout_2.clear_widgets()
		plt.clf()
		self.plot_exists = False

	def back_to_menu(self):
		self.ids.comp_func_2.text = ""
		self.ids.axes_lims_nsteps_2.text = ""
		self.ids.error_2.text = ""
		self.ids.layout_2.clear_widgets()
		plt.clf()
		app.root.current = "FirstScreen"

class FourthScreen(Screen):

	plot_exists = False

	def plot_func(self):
		if self.plot_exists == True:
			self.ids.layout_3.clear_widgets()
			plt.clf()
		try:
			self.ids.error_3.text = ""
			func_name = self.ids.comp_func_3.text
			func = lambdified_func(func_name)
			plot_props = get_list(self.ids.axes_lims_nsteps_3.text, 6)
			re1, re2 = float(plot_props[0]), float(plot_props[1])
			im1, im2 = float(plot_props[2]), float(plot_props[3])
			renps, imnps = int(plot_props[4]), int(plot_props[5])
			cplt = cplot.plot(func, (re1, re2, renps), (im1, im2, imnps))
			canvas = FigureCanvasKivyAgg(plt.gcf(), pos_hint={'x': 0.25, 'y': 0.1}, size_hint=(0.5,0.5))
			self.ids.layout_3.add_widget(canvas)
			canvas.draw()
			self.plot_exists = True

		except Exception as e:
			self.ids.error_3.text = type(e).__name__

	def remove_plot(self):
		self.ids.error_3.text = ""
		self.ids.layout_3.clear_widgets()
		plt.clf()
		self.plot_exists = False

	def back_to_menu(self):
		self.ids.comp_func_3.text = ""
		self.ids.axes_lims_nsteps_3.text = ""
		self.ids.error_3.text = ""
		self.ids.layout_3.clear_widgets()
		plt.clf()
		app.root.current = "FirstScreen"
	

class MyApp(MDApp):

	def build(self):
		self.screen_manager = ScreenManagemer()
		self.screen_manager.add_widget(FirstScreen(name="FirstScreen"))
		self.screen_manager.add_widget(SecondScreen(name="SecondScreen"))
		self.screen_manager.add_widget(ThirdScreen(name="ThirdScreen"))
		self.screen_manager.add_widget(FourthScreen(name="FourthScreen"))
		return self.screen_manager


app = MyApp()
app.run()
