import os

input_image = 'profile_image.jpg' # use appropriate image file name accordingly
style_image_list=['block.jpg',   # choose the required styles
                  'forest.jpg',
                  #'gothic.jpg',
                  'marilyn.jpg',
                  'picasso.jpg',
                  'scream.jpg',
                  'starry_night.jpg',
                  'van_gough.jpg',
                   'wave.jpg'
                  ]

for style_image in style_image_list:
    output_image = input_image.split('.jpg', 1)[0] + '_' + style_image.split('.jpg', 1)[0]+'.jpg'
    python_exe = "python style_transfer.py " + input_image + " " + style_image + " " + output_image
    print (python_exe)

    os.system(python_exe)


