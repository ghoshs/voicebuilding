# Project Seminar: Voicebuilding for TTS
##### University of Saarland 
##### WS 2017-18

In this project we build a unit-selection and HMM text-to-speech system trained on our recordings of the first 330 prompts on the Arctic 
dataset using a MaryTTS v5.2 voice builder. 

It is necessary to use the flac file containing the actual 3-channel recording (headset, microphone and HDMI) to generate voices recorded by our group.
The annonations of the recordings (a TextGrid file generated in Praat) is manually edited to capture the duration of the correct utterance of each prompt.
The TextGrid is then converted to a chronological Table format and uploaded in the repository. 

### Requirements
<<<<<<< HEAD
- SoX (to process the audio file)
- Praat (*optional, if yu want to modify the flac file, speech alignments or the TextGrid*)
- Python 2.7 or higher (to run the data pre-processing scripts)
- Gradle v4.6 (to run MaryTTS and other Gradle projects)
- Docker (to build HMM voice)
- HTK account
- Java 7 or higher 
=======
- SoX
- Python 2.7 or higher
- Gradle v4.6
>>>>>>> new_update

### Download items for speech synthesis:
Inside the 2018-voicebuilding-group1-data folder download the audio file.
- [Audio File](https://bitbucket.org/lenakmeth/2018-voicebuilding-group1/downloads/2018-voicebuilding-group1-raw-audio.flac) 

### 1. Generate and package data for voicebuilding
The build.gradle runs the Python preprocessing files for generating individual text and wav files for each of the 330 prompts. Then the forced alignner
is executed to generate the label files for the prompts. Finally, the text, wav and lab files are packaged as a zip file in build/distributions directory.
From inside the 2018-voicebuilding-group1-data folder run the following gradle script
```
gradle packageData
```
or use the gradle wrapper command if Gradle is not installed.
```
<<<<<<< HEAD
../gradlew packageData
=======
./gradlew packageData
>>>>>>> new_update
```
### 2. Run voicebuilding
From the voice-2018-voicebuilding-group1 folder run the follwing gradle command to unpack data and build the voices for MaryTTS
```
../gradlew legacyInit
../gradlew build
```

<<<<<<< HEAD
### 3. HMM based voice 
We use the [HTS](http://htk.eng.cam.ac.uk/extensions/index.shtml) voicebuilder toolkit provided by [HTK](http://htk.eng.cam.ac.uk/) to build HMM based voice.
This part is run a docker container. We refer to these [slides](http://www.coli.uni-saarland.de/~steiner/teaching/2016/winter/voicebuilding/slides/index.html#/devops)
for this part.
#### a. Create a custom container
Follow the instructions [here](http://www.coli.uni-saarland.de/~steiner/teaching/2016/winter/voicebuilding/slides/index.html#/hts-voicebuilding-with-docker) to
create a container from a docker file.
#### b. Prepare HMM voice features
Run [these](http://www.coli.uni-saarland.de/~steiner/teaching/2016/winter/voicebuilding/slides/index.html#/prepare-for-hts-voicebuilding) pre-requiesites
before we start the docker
#### c. Run the docker
Depending on hoe you have installed docker, you may or may not run it with sudo
```
sudo docker run -v $PWD:$PWD -it marytts-builder-hsmm bash -c \
"cd $PWD; \
/marytts/target/marytts-builder-5.2/bin/voiceimport.sh \
HMMVoiceDataPreparation \
HMMVoiceConfigure \
HMMVoiceMakeData \
HMMVoiceMakeVoice"
```
#### d. Assemble the voice
```
sudo docker run -v $PWD:$PWD -it marytts-builder-hsmm bash -c \
"cd $PWD; \
/marytts/target/marytts-builder-5.2/bin/voiceimport.sh \
HMMVoiceCompiler"
```
Copy the buildscript from [here](http://www.coli.uni-saarland.de/~steiner/teaching/2016/winter/voicebuilding/slides/index.html#/assemble-the-hts-voice) into the 
generated Maven project directory and run `gradle build` or `gradle run`.
=======
### 3. Train HMM

>>>>>>> new_update

### 4. Listen to the voices on new text.
Clone the [MaryTTS v5.2](https://github.com/marytts/marytts) in the parent directory of this project and build the project using the command.
```
./gradlew build
```
Copy the zip and component descriptor xml files from the path voice-2018-voicebuilding-group1/build/distributions generated in 
both Step 2 and 3 and copy it to the download folder in marytts. 

Run the marytts component installer script inside the MaryTTS project.
```
./gradlew runInstallerGui

```
A GUI is launched where you can select the language in left column and the recently copied voice in the right and proceed. Once the component is installed
the voice will show as 'installed' instead of 'available' in the GUI right panel.

Run the MaryTTS server.
```
./gradlew run
```
or
```
./gradlew server
<<<<<<< HEAD
```
Naviagte to `localhost:59125` on your browser. MaryTTS runs on the port 59125. Select *my_voice* from the available voices and use the interface to listen
to the synthesized audio or have a look at the maryxml file.
=======
```
>>>>>>> new_update
