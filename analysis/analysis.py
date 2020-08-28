import pandas as pd
import os, sys
from preprocessor.paths import (PATH_TO_CONSUMER_1)
from preprocessor.preprocessor_customer import CustomerPreprocessor

customer1_preprocessor = CustomerPreprocessor(path_to_data=PATH_TO_CONSUMER_1)
customer1_preprocessor = customer1_preprocessor.data_prepared
