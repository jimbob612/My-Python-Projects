from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import HealthBar
from ursina.input_handler import InputEvents
from ursina.prefabs.file_browser_save import FileBrowserSave
from ursina.mouse import *
from ursina.sequence import Wait
import datetime
from ursina.input_handler import InputEvents
from ursina.collider import Collider

app = Ursina()

block_pick = 1

def update():
    global block_pick

    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4
    if held_keys['5']: block_pick = 5
    if held_keys['6']: block_pick = 6
    if held_keys['7']: block_pick = 7

Sky()

print_on_screen('Use WASD to move around', position=(0,0), origin=(0,0), scale=2, duration=3)

x = datetime.datetime.now()
print(x.strftime("%A"))

grass_texture = load_texture('grass_block.jpeg')
stone_texture = load_texture('stone_block.jpeg')
SpiderBlock = load_texture('spider_block.jpg')
wood_texture = load_texture('wood_texture.jpg')
log_texture = load_texture('log_texture.jpg')
glass_texture = load_texture('glass_texture.png')
leaf_texture = load_texture('leaf_texture.png')

window.title = 'Scuffed Minecraft'
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True
camera.orthagraphic = True

def input(key):
    if key == 'escape':
        mouse.locked = False
        mouse.visible = True

from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton

DropdownMenu('File', buttons=(
    DropdownMenuButton('New'),
    DropdownMenuButton('Open'),
    DropdownMenu('Reopen Project', buttons=(
    DropdownMenuButton('Project 1'),
    DropdownMenuButton('Project 2'),
    )),
    DropdownMenuButton('Save'),
    DropdownMenu('Options', buttons=(
    DropdownMenuButton('Mouse Lock'),
    DropdownMenuButton('Modifications'),
    )),
    DropdownMenuButton('Exit'),
    ))

class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.8,1)),
            highlight_color = color.white)

    def input(self,key):
        if self.hovered:
            if key == 'right mouse down':
                if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = wood_texture)
                if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = log_texture)
                if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
                if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
                if block_pick == 5: voxel = Voxel(position = self.position + mouse.normal, texture = SpiderBlock)
                if block_pick == 6: voxel = Voxel(position = self.position + mouse.normal, texture = glass_texture)
                if block_pick == 7: voxel = Voxel(position = self.position + mouse.normal, texture = leaf_texture)
                    
            if key == 'left mouse down':
                    destroy(self)

for z in range(20):
    for x in range(20):
        for y in range(1):

            voxel = Voxel(position = (x,y,z))
player = FirstPersonController(speed=4.1, jump_height=1.3, jump_duration=0.2, origin_y=+1, air_time=0.2)

app.run()