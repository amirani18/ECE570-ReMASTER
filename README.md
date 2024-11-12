# ReadMe 

Hello and welcome to a stock price analysis for an artificial intelligence - focused  project.

[[Video Demo]](https://drive.google.com/drive/folders/1hnWdFJcDBQ5Fogpza14HEd3GIJqucHD_?usp=sharing)

This is the official code for the extension of the AAAI-2024 paper: **MASTER: Market-Guided Stock Transformer for Stock Price Forecasting**. [[Paper]](https://ojs.aaai.org/index.php/AAAI/article/view/27767)  [[ArXiv preprint]](https://arxiv.org/abs/2312.15235) 
[[GitHub]](https://github.com/SJTU-DMTai/MASTER/tree/master)

MASTER is a stock transformer for stock price forecasting, which models the momentary and cross-time stock correlation and guides feature selection with market information.

![MASTER framework](images/framework.png)

MASTER's original experiments were conducted in a complex business codebase developed based on Qlib. The original code is confidential and exhaustive. In order to enable anyone to quickly use MASTER and reproduce the paper's results, here the authors publish their well-processed data and core code. 

## Usage for ReMASTER
1. Run this command to install dependencies.
- <code>!pip freeze > requirements.txt</code>

2. Download data from one of the following links (the data files are the same) and unpack it into <code> data/ </code> The data used for this experiment is the NASDAQ 100 5-year data including datetime information over a five-year period. 
- [NASDAQ100 link](https://www.kaggle.com/datasets/salaheddineelkhirani/5-year-data-for-s-and-p-500-and-nasdaq-100?resource=download&select=NQ_5Years_8_11_2024.csv)

3. Run all code in the ReMASTER_final.ipynb.

4. I provide a trained model: <code> model/NQ100master_0.pkl</code>

## Dataset
### Form
The downloaded data is split into training, validation, and test sets, with earlier years as training, a few months for validation, and later years for testing. Note the NASDAQ100 data is a subset of the NASDAQ data.
You can use the following code to investigate the **datetime, instrument, and feature formulation**. This process is loaded in for you in <code> data_processing/examine_.pkl</code>
```python
with open('data/NQ100/NQ100_dl_train.pkl', 'rb') as f:
    dl_train = pickle.load(f)
```
In my code, the data will be gathered chronically and then grouped by prediction dates. the <code> data </code> iterated by the data loader is of shape (N, T, F), where:
- N - number of stocks. For NQ100, N is around 100 on each prediction date.
- T - length of lookback_window, T=8.
- F - 29 in total, including 22 factors, 6 market information, and 1 label.  

### Preprocessing
The published data went through the following necessary preprocessing. 
1. Drop NA features, and perform robust daily Z-score normalization on each feature dimension.
2. Drop NA labels and 5% of the most extreme labels, and perform **daily Z-score normalization** on labels. 
- Daily Z-score normalization is a common practice in Qlib to standardize the labels for stock price forecasting. To mitigate the difference between a normal distribution and groundtruth distribution, we filtered out 5\% of most extreme labels in training. Note that the reported RankIC compares the output ranking with the groundtruth, whose value is not affected by the label normalization.

### Testing
The NASDAQ100 dataset is split into training, validation, and test sets based on a time-based split. Earlier dates are used for training and more recent dates are used for testing. They are then converted to .pkl files.


## Usage for MASTER
1. Install dependencies.
- pandas == 1.5.3
- torch == 1.11.0

2. Install [Qlib](https://github.com/microsoft/qlib). We have minimized the reliance on Qlib, and you can simply install it by
- <code>pip install pyqlib </code> (Pip installation only supports python 3.7 and 3.8, please refer to its Readme.md.)
- pylib == 0.9.1.99

3. Download data from one of the following links (the data files are the same) and unpack it into <code> data/ </code>
- [OneDrive link](https://1drv.ms/f/c/652674690cc447e6/Eu8Kxv4xxTFMtDQqTW0IU0UB8rnpjACA5twMi8BA_PfbSA?e=ooc0za)
- [MEGA link](https://mega.nz/file/4OE0jK4I#h-LG7OjFnncbL_YGoSx5c0W604OdFMgALTYFcoDvgfw)
- [Baidu link](https://pan.baidu.com/s/1Wv_nzmw6vlexqZinV_zLtA?pwd=hrrl). 

5. Run main.py.

6. We provide two trained models: <code> model/csi300master_0.pkl, model/csi800master_0.pkl</code>

## Dataset
### Form
The downloaded data is split into training, validation, and test sets, with two stock universes. Note the csi300 data is a subset of the csi800 data.
You can use the following code to investigate the **datetime, instrument, and feature formulation**.
```python
with open(f'data/csi300/csi300_dl_train.pkl', 'rb') as f:
    dl_train = pickle.load(f)
    dl_train.data # a Pandas dataframe
```
In our code, the data will be gathered chronically and then grouped by prediction dates. the <code> data </code> iterated by the data loader is of shape (N, T, F), where:
- N - number of stocks. For CSI300, N is around 300 on each prediction date; For CSI800, N is around 800 on each prediction date.
- T - length of lookback_window, T=8.
- F - 222 in total, including 158 factors, 63 market information, and 1 label.        

### Market information
For convenient reference, we extract and organize market information from the published data into <code>data/csi_market_information.csv</code>.
You can check the **datetime and feature formulation** in the file. Note that m is shared by all stocks.
The market data is generated by the following pseudo-code.

```python
m = []
for S in csi300, csi500, csi800:
  m += [market_index(S,-1)]
  for d in [5, 10, 20, 30, 60]:
    m += [historical_market_index_mean(S, d), historical_market_index_std(S, d)]
    m += [historical_amount_mean(S, d), historical_amount_std(S, d)]
```

### Preprocessing
The published data went through the following necessary preprocessing. 
1. Drop NA features, and perform robust daily Z-score normalization on each feature dimension.
2. Drop NA labels and 5% of the most extreme labels, and perform **daily Z-score normalization** on labels. 
- Daily Z-score normalization is a common practice in Qlib to standardize the labels for stock price forecasting. To mitigate the difference between a normal distribution and groundtruth distribution, we filtered out 5\% of most extreme labels in training. Note that the reported RankIC compares the output ranking with the groundtruth, whose value is not affected by the label normalization.

## Cite
If you use the data or the code, please cite our work! :smile:
```latex
@inproceedings{li2024master,
  title={Master: Market-guided stock transformer for stock price forecasting},
  author={Li, Tong and Liu, Zhaoyang and Shen, Yanyan and Wang, Xue and Chen, Haokun and Huang, Sen},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  volume={38},
  number={1},
  pages={162--170},
  year={2024}
}
```


