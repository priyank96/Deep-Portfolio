## Getting Started

1. Download the dataset and save the files in a folder name RAW inside the makeDataset package

2. Run _makeDataset/pandafy/pandafy.py_ to generate `data_raw.pkl`

3. Run _makeDataset/pandafy/normalise.py_ to generate `data.pkl`

4. Run _makeDataset/companyWise/makeRawDataset.py_ to generate  `CompanyWiseDict.pkl`

5. Run _makeDataset/companyWise/normalise.py_ to generate `NormalisedCompanyWiseDict.pkl`

6. Run _makeDataset/companyWise/DatasetInputFormatter.py_ to generate `NormalisedCompanyWiseDict.pkl`

7. Run _autoEncoder/autoEncoder.py_ to train the Stacked LSTM Auto-Encoder on the dataset!


## Note

Do not commit any of the raw dataset and generated .pkl files!
