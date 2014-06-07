
import bpy

################################################################################
### Render Configuration
################################################################################

# GPU vs CPU rendering
use_gpu       = 0

# Cameras to render, list of camera names
# cameras       = [ 'Camera1’, ‘Camera2’, ‘Camera3’ ]
cameras       = [‘Camera’]

# Dimensions
samples       =  100
res_x         = 1920
res_y         = 1080
res_p         =   20

# Lights Paths 
bnc_max       =  8
bnc_min       =  3
bnc_trasp_max =  8
bnc_trasp_min =  8
bnc_diff      = 128
bnc_glos      = 128
bnc_tran      = 128
no_caustics   = True

# Rendering engine parameters (for performances)
tile_gpu_x    =  128
tile_gpu_y    =  128
tile_cpu_x    =   32
tile_cpu_y    =   32
tile_order    = 'CENTER'

# Scene to render
scene         = 'Scene'
# Filename for the image to produce
image_name    = 'Render_0001'



################################################################################
### Do not touch under this line
################################################################################

def dumpRenderSettings():
    print('Compute device type: ', bpy.context.user_preferences.system.compute_device_type)
    print('Compute device     : ', bpy.context.user_preferences.system.compute_device)
    print('Render Configuration')
    print('  Engine      : ', bpy.data.scenes[scene].render.engine)
    print('  ResolutionX : ', bpy.data.scenes[scene].render.resolution_x)
    print('  ResolutionY : ', bpy.data.scenes[scene].render.resolution_y)
    print('  Resolution% : ', bpy.data.scenes[scene].render.resolution_percentage)
    print('  Tile Size X : ', bpy.data.scenes[scene].render.tile_x)
    print('  Tile Size Y : ', bpy.data.scenes[scene].render.tile_y)
    print('Blender Cycles Configuration')
    print('  Device      : ', bpy.data.scenes[scene].cycles.device)
    print('  Samples     : ', bpy.data.scenes[scene].cycles.samples)
    print('  Tile order  : ', bpy.data.scenes[scene].cycles.tile_order)
    print('  No Caustics : ', bpy.data.scenes[scene].cycles.no_caustics)
    print(' Bounces Max  : ', bpy.data.scenes[scene].cycles.max_bounces)
    print('    "    Min  : ', bpy.data.scenes[scene].cycles.min_bounces)
    print('    "    TMax : ', bpy.data.scenes[scene].cycles.transparent_max_bounces)
    print('    "    TMin : ', bpy.data.scenes[scene].cycles.transparent_min_bounces)
    print('    "    Diff : ', bpy.data.scenes[scene].cycles.diffuse_bounces)
    print('    "    Glsy : ', bpy.data.scenes[scene].cycles.glossy_bounces)
    print('    "    Tran : ', bpy.data.scenes[scene].cycles.transmission_bounces)

print('*** Initial configuration')
dumpRenderSettings()

print('*** Compute Device Selection [CUDA: ', use_gpu, ']')
if use_gpu:
    bpy.context.user_preferences.system.compute_device_type = 'CUDA'
    bpy.context.user_preferences.system.compute_device = 'CUDA_0'
    bpy.data.scenes[scene].cycles.device = 'GPU'
    bpy.data.scenes[scene].render.tile_x = tile_gpu_x
    bpy.data.scenes[scene].render.tile_y = tile_gpu_y
else:
    bpy.context.user_preferences.system.compute_device_type = 'NONE'
    bpy.context.user_preferences.system.compute_device = 'CPU'
    bpy.data.scenes[scene].cycles.device = 'CPU'
    bpy.data.scenes[scene].render.tile_x = tile_cpu_x
    bpy.data.scenes[scene].render.tile_y = tile_cpu_y
bpy.data.scenes[scene].render.engine = 'CYCLES'
bpy.data.scenes[scene].render.resolution_x = res_x
bpy.data.scenes[scene].render.resolution_y = res_y
bpy.data.scenes[scene].render.resolution_percentage = res_p
bpy.data.scenes[scene].cycles.samples = samples
bpy.data.scenes[scene].cycles.tile_order = tile_order
bpy.data.scenes[scene].cycles.no_caustics = no_caustics
bpy.data.scenes[scene].cycles.max_bounces = bnc_max
bpy.data.scenes[scene].cycles.min_bounces = bnc_min
bpy.data.scenes[scene].cycles.transparent_max_bounces = bnc_trasp_max
bpy.data.scenes[scene].cycles.transparent_min_bounces = bnc_trasp_min
bpy.data.scenes[scene].cycles.diffuse_bounces = bnc_diff
bpy.data.scenes[scene].cycles.glossy_bounces = bnc_glos
bpy.data.scenes[scene].cycles.transmission_bounces = bnc_tran

print('*** Saving User-Settings...')
bpy.ops.wm.save_userpref()
dumpRenderSettings()

for camera_name in cameras:

	# Consider just real camera object
	if (bpy.data.objects[camera_name].type !=  'CAMERA'):
		continue
	
	# Setup next camera
	bpy.context.scene.camera = bpy.data.objects[camera_name]
	
	# Start rendering
	print('*** Rendering [' + camera_name + ']... ')
	bpy.ops.render.render(write_still=True)
	rendered_image = bpy.data.images['Render Result']
	
	# Save render image and a copy based on camera name
	rendered_image.save_render(filepath=image_name + '.png')
	rendered_image.save_render(filepath=image_name + '_' + camera_name + '.png')



