from preprocessor.paths import (PATH_TO_CONSUMER_1,
                                PATH_TO_CONSUMER_2,
                                PATH_TO_CONSUMER_3,
                                PATH_TO_CONSUMER_4,
                                PATH_TO_CONSUMER_5,
                                PATH_TO_CONSUMER_6,
                                PATH_TO_CONSUMER_7,
                                PATH_TO_CONSUMER_8,
                                PATH_TO_CONSUMER_9)
from preprocessor.preprocessor_customer import CustomerPreprocessor
import matplotlib.pyplot as plt


customer1_preprocessor = CustomerPreprocessor(path_to_data=PATH_TO_CONSUMER_1)
customer1 = customer1_preprocessor.data_prepared

customer2_preprocessor = CustomerPreprocessor(path_to_data=PATH_TO_CONSUMER_2)
customer2 = customer2_preprocessor.data_prepared

customer2.resample("h").plot(y="leistung_kw")
plt.show()
