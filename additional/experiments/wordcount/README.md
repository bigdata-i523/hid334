### Word Count ###

#### Description ###
This program will allow the user to find word frequency in a piece of text. The script takes two inputs - full text in the first argument and excluded words in the second argument. 

### Example ###
The Fed releases a high-level assessment of the economy semi-annually called the "Monetary Policy Report". https://www.federalreserve.gov/monetarypolicy/2017-07-mpr-summary.htm

Using the script ``data_extract.py``, the script pieces together all of the sections together to get an overview of key words. In its current form, the program looks for paragraph tags to extract the data, but the user can modify this as needed in the script for a particular site. Once this data is extracted, a local text file is created that is used for the main program ``wordcount.py``.

Excluded words were ['the', 'of', 'and', 'has', 'are', 'in'].
### Example Results ###

![fed_words_output](https://user-images.githubusercontent.com/31293179/31894678-199b7e3a-b7dd-11e7-9b37-9b9f002b5c46.png)

![fed_words_count](https://user-images.githubusercontent.com/31293179/31894676-198d5db4-b7dd-11e7-8f7a-01bce0b8d905.png)


Top 50 Words: 

|     Word     | Count | Percent |
|:------------:|:-----:|:-------:|
|    percent   |  122  |   1.09  |
|     have     |  110  |   0.98  |
|    policy    |  109  |   0.97  |
|     year     |   94  |   0.84  |
|  projections |   92  |   0.82  |
|     funds    |   89  |   0.80  |
|      be      |   86  |   0.77  |
|    federal   |   85  |   0.76  |
|       2      |   76  |   0.68  |
|   economic   |   76  |   0.68  |
|     from     |   75  |   0.67  |
|     2017     |   74  |   0.66  |
|      its     |   70  |   0.63  |
|    market    |   63  |   0.56  |
|       4      |   62  |   0.55  |
| unemployment |   60  |   0.54  |
|      was     |   58  |   0.52  |
|       1      |   56  |   0.50  |
|    return    |   54  |   0.48  |
|     real     |   54  |   0.48  |
|     been     |   51  |   0.46  |
|     level    |   48  |   0.43  |
|     text     |   48  |   0.43  |
|     would    |   47  |   0.42  |
|   committee  |   47  |   0.42  |
|      not     |   46  |   0.41  |
|     which    |   45  |   0.40  |
|    quarter   |   44  |   0.39  |
|     years    |   42  |   0.38  |
|      gdp     |   40  |   0.36  |
|     2016     |   40  |   0.36  |
|     fomc     |   40  |   0.36  |
|     rates    |   39  |   0.35  |
|      up      |   38  |   0.34  |
|     price    |   38  |   0.34  |
|   continued  |   37  |   0.33  |
|       3      |   37  |   0.33  |
|     range    |   36  |   0.32  |
|     below    |   36  |   0.32  |
|       a      |   35  |   0.31  |
|      low     |   35  |   0.31  |
|     march    |   35  |   0.31  |
|      for     |   34  |   0.30  |
|      run     |   34  |   0.30  |
|     labor    |   34  |   0.30  |
|   interest   |   34  |   0.30  |
|       &      |   34  |   0.30  |
|     other    |   34  |   0.30  |
|     time     |   33  |   0.29  |
|     june     |   32  |   0.29  |


