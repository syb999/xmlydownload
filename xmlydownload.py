import cv2
import numpy as np
import pyautogui
import time
import PySimpleGUI as sg

position = None
count = 0  
y_step = 21

def find_image_on_screen(template_path, threshold=0.8):
	screenshot = pyautogui.screenshot()
	screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
	
	template = cv2.imread(template_path)
	if template is None:
		raise FileNotFoundError(f"PNG not found")
	
	h, w = template.shape[:-1]
	
	res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
	
	if max_val >= threshold:
		center_x = max_loc[0] + w // 2
		center_y = max_loc[1] + h // 2
		return (center_x, center_y)
	else:
		return None

def click_on_image(template_path, threshold=0.8):
	d_position = find_image_on_screen(template_path, threshold)
	if d_position:
		pyautogui.moveTo(d_position[0], d_position[1])
		pyautogui.click()
		time.sleep(1)
		return True
	return False

def doubleclick_on_image(template_path, threshold=0.8):
	global position, height
	global height
	if position == None:
		position = find_image_on_screen(template_path, threshold)
	else:
		if height == 768:
			if count < 18:
				position = (position[0], position[1] + y_step)
			else:
				position = (position[0], position[1])
		else:
			if count < 24:
				position = (position[0], position[1] + y_step)
			else:
				position = (position[0], position[1])
	if position:
		pyautogui.moveTo(position[0], position[1])
		time.sleep(1)		
		pyautogui.doubleClick()
		time.sleep(1)
		return True
	return False

def main_script(nums):
	global count

	while count < nums:
		time.sleep(1)
		
		if click_on_image("./png/pop.png"):
			if click_on_image("./png/x.png"):
				time.sleep(1)
		elif doubleclick_on_image("./png/play.png"):
			count += 1
			time.sleep(1)
			if click_on_image("./png/menu.png"):
				if click_on_image("./png/dl.png"):
					time.sleep(1)
					pyautogui.hotkey('ctrl', 'w')
					time.sleep(1)
					click_on_image("./png/next.png")
					time.sleep(2)
		elif click_on_image("./png/wait.png"):
			click_on_image("./png/next.png")
			time.sleep(2)
		elif click_on_image("./png/next.png"):
			time.sleep(2)
		else:
			pyautogui.moveTo(1, 1)
			print("未发现目标")



layout = [
	[sg.Text("下载总集数:"), sg.InputText(default_text="10", key='-NUMS-', size=(10,1))],
	[sg.Button("运行"), sg.Button("关闭")]
]

window = sg.Window("喜马拉雅自动下载工具", layout)

while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED or event == "关闭":
		break
	elif event == "运行":
		count = 0
		height = pyautogui.size().height
		time.sleep(2)

		try:
			nums = int(values['-NUMS-'])
			main_script(nums)
			sg.popup("下载完成！")
		except ValueError:
			sg.popup_error("请输入有效的数字！")

window.close()
