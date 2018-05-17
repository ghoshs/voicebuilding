# Project Seminar: Voicebuilding for TTS
##### University of Saarland 
##### WS 2017-18


In this project we build a unit-selection and HMM text-to-speech system trained on our recordings of the first 330 prompts on the Arctic 
dataset using a MaryTTS v5.2 voice builder. 

### Requirements

- [SoX](http://sox.sourceforge.net/) 
- [Praat](http://www.fon.hum.uva.nl/praat/) (*optional, to modify the flac file, speech alignments or the annotations file*)
- Python 2.7 or higher (to run the data pre-processing scripts)
- Gradle v4.6 (to run MaryTTS and other Gradle projects)
- Docker (to build HMM voice)
- [Edinburgh Speech Tools](http://www.cstr.ed.ac.uk/projects/speech_tools/)
- An [HTK account](http://htk.eng.cam.ac.uk/register.shtml)
- Java 7 or higher 


### Download items for speech synthesis:

Download the audio file in the `2018-voicebuilding-group1-data` folder.
- [Audio File](https://bitbucket.org/lenakmeth/2018-voicebuilding-group1/downloads/2018-voicebuilding-group1-raw-audio.flac) 


### 1. Generate and package data for voicebuilding

The `build.gradle` runs the Python preprocessing files for generating individual text and wav files for each of the 330 prompts. Then the forced alignner
is executed to generate the label files for the prompts. Finally, the text, wav and lab files are packaged as a zip file in build/distributions directory.
From the `2018-voicebuilding-group1-data` directory run the following gradle script:
```
gradle packageData
```
or use the gradle wrapper command if Gradle is not installed.
```
../gradlew packageData
```

### 2. Run Unit Selection voicebuilding

From the `voice-2018-voicebuilding-group1` directory run the following gradle command to unpack data and build the voices for MaryTTS:
```
../gradlew legacyInit
../gradlew build
```


### 3. Install voice component on MaryTTS

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
Navigate to `localhost:59125` on your browser. MaryTTS runs on the port 59125. Select *my_voice* from the available voices and use the interface to listen to the synthesized audio or have a look at the maryxml file.


### 4. *Optional:* HMM based voicebuilding

#### a. Create a custom container

The instructions were originally posted [here](http://www.coli.uni-saarland.de/~steiner/teaching/2017/winter/voicebuilding/slides/index.html#/hts-voicebuilding-with-docker):
- Install Docker
- Create a fresh directory and download [this Dockerfile](https://raw.githubusercontent.com/psibre/marytts-dockerfiles/master/marytts-builder-hsmm/Dockerfile)
- Run:
```
docker build \
--build-arg HTKUSER=***** \
--build-arg HTKPASSWORD=***** \
-t marytts-builder-hsmm .
```
where `HTKUSER` and `HTKPASSWORD` are the credentials for your HTK account.

*Note-* Build the docker container inside the voicebuilding build directory, *i.e.,* inside `voice-2018-voicebuilding-group1/build/`


#### b. Pre-requisites for HMM voice features

The instructions were originally posted [here](http://www.coli.uni-saarland.de/~steiner/teaching/2017/winter/voicebuilding/slides/index.html#/prepare-for-hts-voicebuilding) 
Download (or build from source) the MaryTTS Builder and unpack it to some location
Run the some location/bin/voiceimport.sh script from within your voicebuilding project’s build directory
Click “Settings” in the GUI and set the `db.marybase` to `\marytts` in the *database.config* file. 
*NB:* Check whether the filepaths in the *database.config* point to exixting filepaths.
Run the “HMMVoiceFeatureSelection” component, confirm the dialog


#### c. Run the docker

Depending on how Docker is installed, you may or may not run it with `sudo`. 
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

Copy the buildscript from [here](http://www.coli.uni-saarland.de/~steiner/teaching/2017/winter/voicebuilding/slides/index.html#/assemble-the-hts-voice) into 
the generated Maven project directory and run `gradle build` or `gradle run`. Navigate to `localhost:59125` on your browser to listen to the synthesized audio
and download it, or have a look at the maryxml file.

## Authors

* **Shrestha Ghosh** - *Team member* - [s8shghos](https://bitbucket.org/s8shghos/)
* **Aikaterini Azoidou** - *Team member* - [Watermelonweather](https://bitbucket.org/Watermelonweather/)
* **Eleni Metheniti** - *Team member* - [lenakmeth](https://bitbucket.org/lenakmeth/)
* **Ingmar Steiner**- *Project seminar professor* - [psibre](https://bitbucket.org/psibre/)

## Acknowledgments

Thanks to Katherine Dunfield for her help as studio operator.

## License

This project is licensed under the CC-BY-4.0 - see the [LICENSE.txt](LICENSE.txt) file for details
