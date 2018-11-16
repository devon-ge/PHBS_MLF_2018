# How to replicate this project

## Steps for replication

1. Install the dependencies. All site-package dependencies are listed in the `pip requirement` [file](requirements.txt). Run `$ python -m pip install-r requirements.txt` in this directory. If you use Anaconda distribution, all the dependencies used in this project should be installed by default.

2. Edit the config file. To avoid overwriting the pictures we use to train the model, in step 1, please edit [`settings.py`](tooopen_img\tooopen_img\settings.py) and set variable `IMAGES_STORE` (should be in line `75`) to another folder, for example, `../pictures` (we use `images`). Due to the potential change in [Tooopen](http://www.tooopen.com/img/87.aspx), you may not get the same pictures as ours.

3. Run the spider in [`tooopen_img`](tooopen_img). The recommended way to run a scrapy spider is command line tools. See the [spider README](tooopen_img\README.md) for details.

4. Open [`gray2lab.ipynb`](Gray2Lab\gray2lab.ipynb) in jupyter notebook and follow the instruction within.