#!/bin/bash
image=$1
title=$2

convert "$image" -gravity south \
          -strokewidth 1 -annotate 0 "$title" \
          -stroke  none   -fill black -annotate 0 "$title" \
          $image
