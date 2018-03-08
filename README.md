# Project Seminar: Voicebuilding for TTS
##### University of Saarland 
##### WS 2017-18

In this project we build a unit-selection and HMM text-to-speech system trained on our recordings of the first 330 prompts on the Arctic 
dataset using a MaryTTS v5.2 voice builder. 

It is necessary to use the flac file containing the actual 3-channel recording (headset, microphone and HDMI) to generate voices recorded by our group.
The annonations of the recordings (a TextGrid file generated in Praat) is manually edited to capture the duration of the correct utterance of each prompt.
The TextGrid is then converted to a chronological Table format and uploaded in the repository. 

### Requirements
- SoX
- Python 2.7 or higher
- Gradle v4.6

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
./gradlew packageData
```
### 2. Run voicebuilding
From the voice-2018-voicebuilding-group1 folder run the follwing gradle command to unpack data and build the voices for MaryTTS
```
../gradlew legacyInit
../gradlew build
```

### 3. Train HMM


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
```