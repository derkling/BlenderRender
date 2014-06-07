
Blender Remote Render
=====================

This is a simple script which could be used to render Blender 3D models on a
remote  machine. The synchronization with the remote machine is done via
DropBox. This script must be deployed on the remote machine and a cron job
should be configured to periodically start a remote render.

Setup
=====

1. Clone this project on the remote machine:
  cd && git clone https://github.com/derkling/BlenderRender.git

2. Setup a chro job
  crontab -e

  Add this line to check fro new render once every minutes:
*/1 * * * * ~/BlenderRenderer/BlenderRender.sh

3. Setup Dropbox (DB) on the target machine.
Hereafter, ~/Dropbox is the main DB folder


Usage
=====

1. Build a new dropbox folder for this render, e.g. ~/Dropbox/RenderDir

2. Copy the file BlenderRender/BlenderSetup.py into the render folder

3. Customize the parameter to be used for this render by opening the BlenderSetup.py
   file you copied in step 2 and editing the variables definition at the top of
   this file.

   Some example paramters are:

# Render devive: 1 GPU, 0 CPU
use_gpu       = 0

# Comma separated list of names of the cameras to be render,
# each camera name must be enclosed by quotes:
cameras       = ['Camera']

# Name of the scene to render
scene         = 'Scene'

# Name of the image to produce
image_name    = 'Render_0001'

4. Export your blender project and copy it into the DB RenderDir folder
   NOTE: This file MUST be named ToRender.blend

5. Wait for the render to complete.
Once the render start a file named RenderStarted is created
Once the render completed a file named RenderEnded is created


NOTE: A new render is triggered only if a RenderStarted file is not present.
To re-start a new render, e.g. with a new model and/or parameters:
a) repeat steps 2-4
b) remove files RenderEnded and RenderStarted

NOTE: the file ToRender.blend MUST embedd all the external reference required within the
same filder or anyway they must be reachable via relative paths on the remote machine.

