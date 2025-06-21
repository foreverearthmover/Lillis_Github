
## Code Reading Exercise

1. #### Where did you find the code and why did you choose it?

Link: https://github.com/AlexanderFarrell/adventure_game_python  
I found the code on GitHub by searching up "python adventure game" which is the kind of thing I want to do for my final  
project. I chose the sprite.py file in the adventure_game_python/src/components path because I want to create a  
graphical interface as well as add simple animation. The code at hand seems to be very well optimized to handle the  
loading of sprites/image frames by having a modular construction of classes that build up on each other and by  
using caching. It's also not very old, maintained and has a few stars.

---
2. #### What does the program do? What's the general structure?  
  
The program uses pygame, engine (src/core/engine.py) and camera (src/core/camera, used for  
drawing relative to the screen) to handle the animation of sprites.  
It's dictionary loaded caches loaded images.
It defines three main classes:  
- Sprite: loads, draws to the screen (either as part of the game world or UI)  
and transforms images, uses cache (loaded)
- Atlas: inherits from Sprite, creates sub-images from a sprite sheet
- and Animation: inherits from Atlas, animates (who would have guessed)  
by cycling through sub-images  

Sprites automatically register to engine.drawables/ui_drawables and animations to engine.active_objs in engine.py


---
3. #### Function analysis
    What does this function do?  
    What are the inputs and outputs?  
    How does it work (step by step)?  
    
Sprite Class:  

__init\__()  
- inits a sprite and registers it to the game engine  
- inputs: image (filename), is_ui (boolean)
- outputs: no output
- imports engine from core.engine, saves is_ui flag, checks if image is in  
loaded cache (yes: reuses cached image, no: loads image from disk and caches it),  
sets self.width and self.height to image size, if is_ui adds to engine.ui_drawables  
if otherwise, adds to engine.drawables

set_image()  
- changes the sprite's image dynamically  
- inputs: image (new filename)  
- outputs: none, but replaces self.image 
- checks whether image is cached (yes: use cached version, no: load it and store in loaded),  
sets self.image to the loaded image

rotate()/scale()  
- rotates/resizes sprite image  
- input: amo (degrees to rotate)/x_scale (width), y_scale (height)
- outputs: no output, but updates image  
- uses pygame methods to rotate/resize, overwrites prior self.image  

breakdown()  
- removes sprite from engine's drawable list
- inputs: none
- outputs: none, but removes image  
- imports engine, removes self from engine.(ui).drawables (depending on is_ui)

draw()  
- draws image onto screen surface
- inputs: screen 
- outputs: none, but blits self.image onto screen if within bounds of camera
- calculates position (if ui: absolute to camera, if not: relative to camera),  
checks if object is inside camera view if outside: skip drawing,  
screen.blit draws the image to calculated position  
  
Atlas Class:  
  
__init\__()  
- loads an image with a table of several sub-images inside it  
- inputs: image, cell_width, cell_height, start_x, start_y, is_ui
- outputs: none, but loads sheets, creates surface and calls self.switch_to  
- calls super().__init\__() to ensure the full image is loaded and registered, saves full image  
as self.base_image, stores cell (sub-image) size and initial coordinates, creates a new surface with cell's size,  
calls self.switch_to to copy sub-images from the image table  

switch_to()  
- displays a specific sub-image from sprite sheet
- input: cell (sub-image) position in the grid  
- outputs: none, but updates self.image
- saves initial cell position, calculates coordinates (in full image) in pixels, clears  
current image surface, blits the selected sub-image copied from base_image to self_image

set_image()  
- replaces the base image while keeping sub-image coordinates  
- inputs: image (filename of sprite sheet)
- outputs: none, but changes base_image, updates frame
- loads and stores image if not cached, sets self.base_image to new image, reapplies  
current sub-image by calling switch_to()

Animation Class:  
  
__init\__  
  
- inits an animated sprite by cycling through frames
- inputs: image (sprite sheet filename), cell_width, cell_height, frame_coords, frames_per_image, is_ui
- outputs: none  
- makes sure that frame_coords isn't empty, gets starting sub.image from first coordinate, inits Atlas, calls  
super().__init\__() to init both parent classes, stores frame_coords, frames_per_image, current_image and ticks and  
adds self to engine.active_objs so update() is called and animation is updated
  
set_frame_coords()  
- replaces animation sequence with a new set of frames (for different animations on same sprite sheet)  
- inputs: frame_coords
- outputs: none, but resets animation for a new sequence
- resets everything to the first image in the new frame coords list: sets new frame_coords, resets animation state  
  (ticks and current image) and calls switch_to to go back to the first frame  

update()  
- animates frames over time
- inputs: none
- outputs: none, but updates frame after enough ticks
- increases ticks, resets ticks if enough ticks have gone by (as many ticks as frames), advances to the next frame,  
past last image, loop back to first frame, sets the position of the next image, updates current sub-image with switch_to()


---
4. #### Takeaways: is there anything you can learn from the code?
There are definitely some things I could learn from the code. Before, I really only knew that sprite sheets existed but  
wasn't aware how they are specifically used. It makes sense now that you have to individually extract sub-images and  
cycle through those but I wouldn't have known how to do that well beforehand. I think it's really clever how the  
person who coded this used base and subclasses for this process and the way the entirety of the code in the repository  
is modularized. Maybe I can use some of these functions when trying to make my own sprite management system.

---
5. #### What parts of the code were confusing or difficult to understand at the beginning?  
    Were you able to understand what it's doing after your own research?  
  
In general, because the code is very advanced and draws on multiple other classes outside the file,  
I had to look at other components in the repository to understand what methods were used.  
Also, although I roughly knew what sprites are and what you do to animate things, it was kinda tough to keep track of   
the different image files, where they are registered and how they are transformed.  
I also learned that you can also use "\\\" at the end of a statement (i.e. line 48) to increase readability if it  
otherwise extends to the next line.
The code also served as a practical example of super().__init\__() to inherit a class's constructor. 

---
_Extra Notes_  
-_none_-
