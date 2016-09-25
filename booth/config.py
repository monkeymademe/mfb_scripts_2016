# Tumblr Setup
# Replace the values with your information
# OAuth keys can be generated from https://api.tumblr.com/console/calls/user/info
consumer_key="PN3YXMR86ghPYc10TpBGYtGeN"
consumer_secret="94kONvgFeuSTZeyeJvJpGZjXD6m323nOiijDtUD0CySdkzxwRU"

access_token="2570783839-E32l7bAv6MGJGu1C6zkaOZQsUfKl5cSG03uKgqW"
access_token_secret="j09Yyhffn9IoraJkj4shfN1AygnklLduMHQuNMMgokamf"

tumblr_blog = 'TUMBLR_BLOG' # replace with your tumblr account name without .tumblr.com
tagsForTumblr = "MyTagsHere" # change to tags you want, separated with commas

#Config settings to change behavior of photobooth
file_path = '/home/pi/photobooth/pics/' # path to save images
clear_on_startup = False # True will clear previously stored photos as the program launches. False will leave all previous photos.
debounce = 0.3 # how long to debounce the button. Add more time if the button triggers too many times.
post_online = True  # True to upload images. False to store locally only.
hi_res_pics = False # True to save high res pics from camera.
                    # If also uploading, the program will also convert each image to a smaller image before making the gif.
                    # False to first capture low res pics. False is faster.
monitor_w = 1280     # width of the display monitor
monitor_h = 800     # height of the display monitor
