from moviepy.editor import ImageSequenceClip
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
print("Please Enter The Path WITHOUT QUOTES. ")
ip = input("PATH : ")
duration = 3

output_folder = os.path.join(os.path.expanduser("~"), "Desktop", "GIF_OUTPUTS")
os.makedirs(output_folder, exist_ok=True)

output_number = 1
while True:
    gif_filename = os.path.join(output_folder, f'outputgif{output_number}.gif')
    if not os.path.exists(gif_filename):
        break
    output_number += 1

img = ImageSequenceClip([mpimg.imread(ip)], fps=10)


img = img.set_duration(duration)


img.write_gif(gif_filename, fps=10, loop=0)

print(f'GIF created: {gif_filename}')
