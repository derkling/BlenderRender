#!/bin/bash

# The blender build to use
BLENDER=blender

# The folder containing this script
RDIR="`find $PWD`/`dirname $0`"

# Local project configuration file for the render
BSETUP=./BlenderSetup.py

# Do nothing if blender is already running
RUNNING=`ps aux | grep blender | grep -v grep | wc -l`
[ $RUNNING -eq 0 ] || exit 0

cd
find . -name ToRender.blend > FilesToRender.txt

for FILE in `cat FilesToRender.txt`; do
  #echo "Checking for renders in [$HOME/$FILE]..."
  cd $HOME/`dirname "$FILE"`

  # Do nothing if the rendered file has not been removed
  [ -f RenderStarted ] && continue

  # Setup Blender configuration
  [ -f $BSETUP ] ||  BSETUP=$RDIR/BlenderSetup.py

  # Display command to run
  touch RenderStarted
  echo "Start render in [`pwd`]..."
  echo "Command: nice $BLENDER -b ToRender.blend -P $BSETUP 2>&1 | bzip2 > Render.txt.bz2"

  # Run Blender...
  nice $BLENDER -b ToRender.blend \
    -P ./BlenderSetup.py \
    2>&1 | bzip2 > Render.txt.bz2

  touch RenderEnded

done

