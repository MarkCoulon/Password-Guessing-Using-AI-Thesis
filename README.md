# Password-Guessing-Using-AI-Thesis
All of the files for the GAN came from this git repository: https://github.com/d4ichi/PassGAN
However they were updated to work with the newest versions of python and tensorflow which are in this file. In case it does not work, download the files from the above repository.

The new files for the evaluation were removeBad, which removes bad characters from the passwords, configureTxt, which removes passwords greater than 10 characters. Also the newStrengthDetermination, which calculates the strength of a dataset and plots it. Finally passwordEvalNew which compares the similarity of two datasets.

The flow of the program should run as follows:
- first download a dataset
- Then run the removeBad and configureTxt scripts on it, making note you may need to change some of the fileNames inside the program so it saves in the correct place.
- after that running train.py with whatever parameters are decided
- then running sample.py with parameters
- then running passwordEvalNew with the datasets you want compared
- then downlading zxcvbn
- then running newStrengthDetermination.py to get the strengths
- also running cosine_similar.py to get the cosine similarity
