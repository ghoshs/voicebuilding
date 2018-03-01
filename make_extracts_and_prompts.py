#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VOICEBUILDING FOR TTS

Prerequisites:
    - .Table file from praat
    - .txt file with the prompts (cmu-arctic.data.txt)
    - .flac file with the recording or a .wav file
    - SoX for the sound segmentation

@author: lenakmeth
"""

import subprocess
import os, sys
import re


def read_boundaries(boundaries_table):
    """ Reads the .Table file and returns a list, in which each item is a
        list of the start and the end points for each prompt recording."""
    boundaries = []
    with open(boundaries_table, 'r', encoding = "utf-8") as f:
        for line in f:
            if not "tmin" in line:
                boundaries.append(line.strip().replace("\t", "").replace("\s", "").split("speech"))

    return boundaries


def read_prompts(prompts_file):
    """ Reads the .txt file with the prompts. """

    prompts = []
    with open(prompts_file, 'r', encoding = "utf-8") as f:
        for line in f:
            if "arctic" in line:
                prompts.append(re.search('"(.+)"', line).group(1))
                print(re.search('"(.+)"', line).group(1))

    return prompts


def segment_sounds(sound_file, boundaries_list):
    """ Uses SoX to extract each prompt recording from the audio file. Saves them
        in a new folder named 'extracts'. """

    newpath = 'build/extracts'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    counter = 0
    for b in boundaries_list:
        start = b[0]
        end = b[1]
        counter += 1

        p = subprocess.Popen(["sox " + sound_file + " -r 16k build/extracts/" + str(counter) + ".wav trim " + start + " =" + end], shell=True)
        p.wait()

    return None

def save_prompts(prompts_list):
    """ Creates a separate text file for every prompt in the prompts_list, and
        saves them in a new folder named 'prompts'."""

    newpath = 'build/prompts'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    counter = 0
    for p in prompts_list:
        counter += 1
        with open("build/prompts/" + str(counter)+".txt", 'w', encoding = "utf-8") as f:
            f.write(p)
            f.close()

    return None


if __name__ == "__main__":

    boundaries_file = sys.argv[1]
    prompts_file    = sys.argv[2]
    sound_file      = sys.argv[3]


    boundaries_list = read_boundaries(boundaries_file)
    prompts_list = read_prompts(prompts_file)[:len(boundaries_list)]
    print(prompts_list)

#    segment_sounds(sound_file, boundaries_list)
#    save_prompts(prompts_list)