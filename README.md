# Sentiment Analysis on GAN Generated Videos

This repository includes an implementation of a sentiment analysis on GAN generated videos. The implementation takes inspiration from both Matt Siegelman's (2019) "Deep Music Visualizer" [repo](https://github.com/msieg/deep-music-visualizer) and Fabio Carrara's "Visual Sentiment Analysis" [repo](https://github.com/fabiocarrara/visual-sentiment-analysis). 

## Usage 
To run this project, first you will have to generate a video from input audio, then run the sentiment analysis to get the sentiment of the generated video. 

0. Install requirements in `music-visualizer/requirements.txt` (with Python 3.6), and install PyTorch. 

### Music video generation 
1. ```cd music-visualizer```
2. ```python visualize.py --resolution 128 --duration 60 --song song_name.mp3 --pitch_sensitivity 220 --tempo_sensitivity 0.25 --mood mood```
    Note here that we are limiting our settings to resolution = 128 and duration to 1 minute. The pitch sensitivity and the tempo sensitivity are the two parameters we are experimenting with. The audio file name and the mood should also be specified. 

    For example, to generate a video for `calm.mp3`, with `pitch_sensitivity = 220` and `tempo_sensitivity = 0.25`, you can run:

    ```python visualize.py --resolution 128 --duration 60 --song calm.mp3 --pitch_sensitivity 220 --tempo_sensitivity 0.25 --mood calm```

This module will ensure the videos are generated to the correct path for the sentiment analysis module.

### Sentiment analysis
Once we have generated videos, we will perform sentiment analysis on the video by performing image sentiment analysis from all the frames in the video.

3. ```cd sentiment-analysis```
4. Download the pretrained models:
    ```./download_models.sh```
5. Extract the frames from the video using `frame_extract.py`. For example, 
    ```python frame_extract.py calm 220,25```
    The first positional command line argument specifies the mood (`calm`) and the second argument will be 2 parameter settings, separated by a comma.

6. Run sentiment analysis prediction of the extracted frames using `predict.py`. For example,
    ```python predict.py calm_220_25.txt --model vgg19_finetuned_all --batch-size 64 > calm_220_25.csv```
   The input `.txt` file generated from 4. should contain the paths to extracted frames. User must specify an output CSV file name. The naming convention for both files is `{mood}_{pitch_sensitivity}_{tempo_sensitivity}`.
   Note that this step should be run on GPU. This can be achieved by running all command lines on Google Colab.

7. Run sentiment analysis prediction of the video using `parse_predictions.py` For example,  
    ```python parse_predictions.py calm_220_25.csv```
   The possible predictions are 'Negative', 'Neutral' and 'Positive'.
