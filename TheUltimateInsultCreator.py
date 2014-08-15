# Insult Generator
# by Logan G.
#
# Sorry for the sloppy, uncommented code.
# I started it at 2am and don't care
# enough to make it more understandable.
# # # # # # # # # # # # # # # # # # # # #


import console, sound, random, scene, ui, speech, webbrowser, string
from scene import *


console.clear()
console.set_color(0.2, 0.2, 0.2)
console.set_font('Helvetica', 14)


class InsultGenerator (Scene):
	def setup(self):
		self.sw, self.sh = self.size.w, self.size.h
		self.iPad = self.sw > 700
		
		self.First = ['Lazy', 'Stupid', 'Insecure', 'Idiotic', 'Slimy', 'Slutty', 'Smelly', 'Pompous', 'Communist', 'Dicknose', 'Pie-Eating', 'Racist', 'Elitist', 'White Trash', 'Drug-Loving', 'Butterface', 'Tone Deaf', 'Ugly', 'Creepy']
		self.Second = ['Douche', 'Ass', 'Turd', 'Rectum', 'Butt', 'Cock', 'Shit', 'Crotch', 'Bitch', 'Prick', 'Slut', 'Taint', 'Fuck', 'Dick', 'Boner', 'Shart', 'Nut', 'Sphincter']
		self.Third = ['Pilot', 'Canoe', 'Captain', 'Pirate', 'Hammer', 'Knob', 'Box', 'Jockey', 'Nazi', 'Waffle', 'Goblin', 'Blossum', 'Biscuit', 'Clown', 'Socket', 'Monster', 'Hound', 'Dragon', 'Balloon']
		
		self.Display = 'Tap the screen for a random insult!'
		self.FirstDisplay = ''
		self.SecondDisplay = ''
		self.ThirdDisplay = ''
		
		self.Full = ''
		
		self.Randum = -60
		self.Dunn = True
		self.ButtonPressed = False
		
		self.SpeechEnabled = True
		
		self.tX = 0
		self.Dragging = False
		self.Stage = 'Insult'
		self.Barrier = self.sh/4.0
		self.AimY = 0
		
		#Images
		self.Muted = 'ionicons-ios7-mic-off-256'
		self.Unmuted = 'ionicons-ios7-mic-256'
		self.ShareImage = 'ionicons-share-256'
		self.EditImage = 'ionicons-navicon-round-256'
		self.Valuez = load_image_file('ImageFiles/Imported/Insults.png')
		self.CloseButton = 'ionicons-close-round-256'
		self.FB = 'ionicons-social-facebook-256'
		self.TW = 'ionicons-social-twitter-256'
		self.TX = 'ionicons-ios7-chatboxes-256'
		self.EM = 'ionicons-email-256'
	
	def draw(self):
		background(0.75, 0.75, 0.75)
		no_tint()
		image(self.Valuez, 10, 10, self.sw-20, self.sh-90)
		
		if self.Dragging:
			self.tX -= (self.tX-self.AimY)*0.25
		if not self.Dragging and self.Stage != 'Share':
			if self.Stage == 'Insult':
				self.tX -= (self.tX * 0.1)
			else:
				self.tX += ((self.sh-70)-self.tX) * 0.1
		
		push_matrix()
		translate(0, self.tX)
		stroke_weight(1)
		for ij in range(10):
			stroke(0.2, 0.2, 0.2, (1-ij/10.0)/2.0)
			line(0, -ij, self.sw, -ij)
		fill(0.8, 0.8, 0.8)
		no_stroke()
		rect(0, 0, self.sw, self.sh)
		
		if self.Randum > 0:
			self.Randum -= 1
			self.Randomize()
		elif self.Randum > -10:
			self.Randum -= 1
			if self.Randum % 2 == 0:
				self.Randomize()
		elif self.Randum > -20:
			self.Randum -= 1
			if self.Randum % 3 == 0:
				self.Randomize()
		elif self.Randum > -30:
			self.Randum -= 1
			if self.Randum % 4 == 0:
				self.Randomize()
		elif self.Randum > -40:
			self.Randum -= 1
			if self.Randum % 5 == 0:
				self.Randomize()
		elif not self.Dunn:
			self.Dunn = True
			self.Full = self.FirstDisplay + ' ' + self.SecondDisplay + ' ' + self.ThirdDisplay
			if self.SpeechEnabled:
				speech.stop()
				if not self.Full[0] in ('A','E','I','O','U'):
					speech.say('You are a '+self.Full, 'en-US', 0.15)
				else:
					speech.say('You are an '+self.Full, 'en-US', 0.15)
		
		tint(1, 1, 1)
		text(self.Display, 'Noteworthy-Bold', 18, self.sw/2.0+2, self.sh/2.0-2, 5)
		tint(0, 0, 0)
		text(self.Display, 'Noteworthy-Bold', 18, self.sw/2.0, self.sh/2.0, 5)
		
		tint(0, 0, 0, 0.5)
		if self.Display == '':
			try:
				if not self.Full[0] in ('A','E','I','O','U'):
					text('You are a...', 'SourceSansPro-Bold', 42, self.sw/2.0-1, self.sh/4.0*3+1, 5)
				else:
					text('You are an...', 'SourceSansPro-Bold', 42, self.sw/2.0-1, self.sh/4.0*3+1, 5)
			except:
				text('You are a...', 'SourceSansPro-Bold', 42, self.sw/2.0-1, self.sh/4.0*3+1, 5)
		text(self.FirstDisplay, 'SourceSansPro-Bold', 26, self.sw/2.0-0.5, self.sh/8.0*5+0.5, 5)
		text(self.SecondDisplay, 'SourceSansPro-Bold', 26, self.sw/2.0-0.5, self.sh/2.0+0.5, 5)
		text(self.ThirdDisplay, 'SourceSansPro-Bold', 26, self.sw/2.0-0.5, self.sh/8.0*3+0.5, 5)
		tint(0, 0, 0, 0.5-(self.tX/(self.sh-70))/2.0)
		#text(self.Full, 'Noteworthy-Bold', 18, self.sw/2.0-1, 51, 8)
		tint(1, 1, 1)
		if self.Display == '':
			try:
				if not self.Full[0] in ('A','E','I','O','U'):
					text('You are a...', 'SourceSansPro-Bold', 42, self.sw/2.0+1, self.sh/4.0*3-1, 5)
				else:
					text('You are an...', 'SourceSansPro-Bold', 42, self.sw/2.0+1, self.sh/4.0*3-1, 5)
			except:
				text('You are a...', 'SourceSansPro-Bold', 42, self.sw/2.0+1, self.sh/4.0*3-1, 5)
		text(self.FirstDisplay, 'SourceSansPro-Bold', 26, self.sw/2.0+1, self.sh/8.0*5-1, 5)
		text(self.SecondDisplay, 'SourceSansPro-Bold', 26, self.sw/2.0+1, self.sh/2.0-1, 5)
		text(self.ThirdDisplay, 'SourceSansPro-Bold', 26, self.sw/2.0+1, self.sh/8.0*3-1, 5)
		tint(1, 1, 1, 1-(self.tX/(self.sh-70)))
		text(self.Full, 'Noteworthy-Bold', 18, self.sw/2.0+2, 48, 8)
		tint(0.2, 0.4, 0.9, 0.75)
		text(self.FirstDisplay, 'SourceSansPro-Bold', 26, self.sw/2.0, self.sh/8.0*5, 5)
		text(self.SecondDisplay, 'SourceSansPro-Bold', 26, self.sw/2.0, self.sh/2.0, 5)
		text(self.ThirdDisplay, 'SourceSansPro-Bold', 26, self.sw/2.0, self.sh/8.0*3, 5)
		tint(0, 0.3, 0.6, 1-(self.tX/(self.sh-70)))
		text(self.Full, 'Noteworthy-Bold', 18, self.sw/2.0, 50, 8)
		tint(0.3, 0.3, 0.3)
		if self.Display == '':
			try:
				if not self.Full[0] in ('A','E','I','O','U'):
					text('You are a...', 'SourceSansPro-Bold', 42, self.sw/2.0, self.sh/4.0*3, 5)
				else:
					text('You are an...', 'SourceSansPro-Bold', 42, self.sw/2.0, self.sh/4.0*3, 5)
			except:
				text('You are a...', 'SourceSansPro-Bold', 42, self.sw/2.0, self.sh/4.0*3, 5)
		
		tint(0.2, 0.2, 0.2, 1-self.tX/(self.sh-50))
		image(self.Unmuted if self.SpeechEnabled else self.Muted, 5, 5, 40, 40)
		if self.Full == '':
			tint(0.2, 0.2, 0.2, 0.25-self.tX/(self.sh-50)/4.0)
		image(self.ShareImage, self.sw-45, 5, 40, 40)
		tint(0.2, 0.2, 0.2)
		image(self.EditImage, self.sw/2.0-20, 5, 40, 40)
		
		#Help
		if self.Display != '':
			tint(1, 1, 1, 1-(self.tX/(self.sh-70)))
			text('Text-to-speech', 'Noteworthy-Bold', 14, 7, 48, 9)
			text('Share', 'Noteworthy-Bold', 14, self.sw-5, 48, 7)
			text('List', 'Noteworthy-Bold', 14, self.sw/2.0+2, 48, 8)
			tint(0, 0, 0, 1-(self.tX/(self.sh-70)))
			text('Text-to-speech', 'Noteworthy-Bold', 14, 5, 50, 9)
			text('Share', 'Noteworthy-Bold', 14, self.sw-7, 50, 7)
			text('List', 'Noteworthy-Bold', 14, self.sw/2.0, 50, 8)
		
		pop_matrix()
		
		if self.Stage == 'Share':
			fill(0, 0, 0, 0.8)
			no_stroke()
			rect(0, 0, self.sw, self.sh)
			fill(0.8, 0.8, 0.8)
			rect(25, 35, self.sw-50, self.sh-90)
			rect(35, 25, self.sw-70, self.sh-70)
			ellipse(25, self.sh-65, 20, 20)
			ellipse(self.sw-45, self.sh-65, 20, 20)
			ellipse(25, 25, 20, 20)
			ellipse(self.sw-45, 25, 20, 20)
			tint(1, 1, 1)
			if not self.Full[0] in ('A','E','I','O','U'):
				text('You know what? You\'re a', 'Noteworthy-Bold', 18, self.sw/2.0+2, self.sh-98, 2)
			else:
				text('You know what? You\'re an', 'Noteworthy-Bold', 18, self.sw/2.0+2, self.sh-98, 2)
			text(self.Full, 'Noteworthy-Bold', 18, self.sw/2.0+2, self.sh-122, 2)
			tint(0.2, 0.2, 0.2)
			if not self.Full[0] in ('A','E','I','O','U'):
				text('You know what? You\'re a', 'Noteworthy-Bold', 18, self.sw/2.0, self.sh-98, 2)
			else:
				text('You know what? You\'re an', 'Noteworthy-Bold', 18, self.sw/2.0, self.sh-98, 2)
			text('Share by Email:', 'SourceSansPro-Bold', 18, self.sw/2.0, self.sh-180, 2)
			tint(0.2, 0.2, 1)
			text(self.Full, 'Noteworthy-Bold', 18, self.sw/2.0, self.sh-120, 2)
			
			no_tint()
			image(self.CloseButton, 30, self.sh-90, 40, 40)
			image(self.EM, self.sw/2.0-25, self.sh-255-25, 50, 50)
		
	def touch_began(self, touch):
		TouchX, TouchY = touch.location.x, touch.location.y
		self.Dragging = False
		if self.Stage == 'Insult':
			if TouchY < 70:
				self.ButtonPressed = True
				if TouchX < self.sw/4.0:
					self.SpeechEnabled = not self.SpeechEnabled
					speech.stop()
					speech.stop()
					speech.stop()
				elif TouchX > self.sw-(self.sw/4.0):
					if self.Full != '':
						self.Stage = 'Share'
				else:
					self.Dragging = True
					self.AimY = TouchY
					self.tX = 20
					self.Barrier = self.sh/4.0
			else:
				self.ButtonPressed = False 
			if self.Dunn and not self.ButtonPressed:
				self.Display = ''
				self.Randum = 25
				self.Dunn = False
		elif self.Stage == 'Edit':
			if TouchY > self.sh-70:
				self.Dragging = True
				self.AimY = TouchY
				self.tX = self.sh-90
				self.Barrier = self.sh/4.0*3
			else:
				pass #Edit values
		else:
			if TouchX < 80 and TouchY > self.sh-100:
				self.Stage = 'Insult'
			if TouchY > self.sh-280 and TouchY < self.sh-180:
				if TouchX < self.sw/2.0+50 and TouchX > self.sw/2.0-50:
					if string.find(self.FirstDisplay, ' ') > -1:
						self.FirstDisplay2 = string.join(string.split(self.FirstDisplay, ' '), '%20')
					else:
						self.FirstDisplay2 = self.FirstDisplay
					if not self.Full[0] in ('A','E','I','O','U'):
						openUrl = 'mailto:?subject=The%20Ultimate%20Insult%20Creator%20for%20iOS&body=You%20know%20what?%20You\'re%20nothing%20but%20a%20'+self.FirstDisplay2+'%20'+self.SecondDisplay+'%20'+self.ThirdDisplay+'!'
					else:
						openUrl = 'mailto:?subject=The%20Ultimate%20Insult%20Creator%20for%20iOS&body=You%20know%20what?%20You\'re%20nothing%20but%20an%20'+self.FirstDisplay2+'%20'+self.SecondDisplay+'%20'+self.ThirdDisplay+'!'
					webbrowser.open(openUrl)
	
	def touch_moved(self, touch):
		if self.Dragging:
			#self.tX -= touch.prev_location.y - touch.location.y
			self.AimY = touch.location.y
	
	def touch_ended(self, touch):
		self.Dragging = False
		if self.Stage != 'Share':
			if self.tX > self.Barrier:
				self.Stage = 'Edit'
			else:
				self.Stage = 'Insult'
	
	def Randomize(self):
		if self.Randum > -40:
			sound.play_effect('Click_1', ((self.Randum+40.0)/65.0), 3+(self.Randum/15.0))
		else:
			sound.play_effect('Ding_3', 1.5, 0.9)
		self.FirstDisplay = random.choice(self.First)
		self.SecondDisplay = random.choice(self.Second)
		self.ThirdDisplay = random.choice(self.Third)
	
	def pause(self):
		for ij in range(10):
			speech.stop()
			
	def resume(self):
		for ij in range(10):
			speech.stop()


class SceneViewer(ui.View):
	def __init__(self, in_scene):
		self.present('full_screen', hide_title_bar = True)
		scene_view = scene.SceneView(frame=self.frame)
		scene_view.scene = in_scene
		self.add_subview(scene_view)
		self.add_subview(self.close_button())

	def close_action(self, sender):
		self.close()

	def close_button(self):
		the_button = ui.Button(title='X')
		the_button.x = self.width - the_button.width
		the_button.y = the_button.height / 2
		the_button.action = self.close_action
		the_button.font=('<system-bold>', 20)
		return the_button


if __name__ == '__main__':
	SceneViewer(InsultGenerator())
