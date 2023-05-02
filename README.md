# Sentiment Analysis on GAN Generated Videos

This repository includes an implementation of a sentiment analysis on GAN generated videos. The implementation takes inspiration from both Matt Siegelman's (2019) "Deep Music Visualizer" [repo](https://github.com/msieg/deep-music-visualizer/blob/master/README.md) and Fabio Carrara's "Visual Sentiment Analysis" [repo](https://github.com/fabiocarrara/visual-sentiment-analysis). 

## Usage 
To run this project, first you will have to generate a video from input audio, then run the sentiment analysis to get the sentiment of the generated video. 

0. Install requirements in `music-visualizer/requirements.txt`, and install PyTorch. 

### Music video generation 
1. ```cd music-visualizer```
2. ```python visualize.py --resolution 128 --duration 60 --song song_name.mp3 --pitch_sensitivity 220 --tempo_sensitivity 0.25 --mood mood```
    Note here that we are limiting our settings to resolution = 128 and duration to 1 minute. The pitch sensitivity and the tempo sensitivity are the two parameters we are experimenting with. The audio file name and the mood should also be specified. 

    For example, to generate a video for `calm.mp3`, with `pitch_sensitivity = 220` and `tempo_sensitivity = 0.25`, you can run:

    ```python visualize.py --resolution 128 --duration 60 --song calm.mp3 --pitch_sensitivity 220 --tempo_sensitivity 0.25 --mood calm```

This module will ensure the videos are generated to the correct path for the sentiment analysis module.

### Sentiment analysis
Once we have generated videos, we will perform sentiment analysis on the video by performing iamge sentiment analysis from all the frames in the video.

3. ```cd sentiment-analysis```
4. ```python frame_extract.py calm 220,25```
    This command extracts the frames from the video. The first positional command line argument specifies the mood (`calm`) and the second argument will be 2 parameter settings, separated by a comma.

5. ```python predict.py calm_220_25.txt --model vgg19_finetuned_all --batch-size 64 > calm_220_25.csv```
    This command runs the sentiment analysis prediction of the extracted frames from a video. The input `.txt` file generated from 4. should contain the paths to extracted frames. User must specify an output CSV file name. The naming convention for both files is `{mood}_{pitch_sensitivity}_{tempo_sensitivity}`

6. ```python parse_predictions.py calm_220_25.csv```
    This command outputs the final sentiment prediction of the video. The possible predictions are 'Negative', 'Neutral' and 'Positive'.
