import numpy as np
import pandas as pd
import matplotlib.pyplot as mp
import seaborn as sbn

#visualition


plt.figure(figsize=(12, 6))

plt.title('Number of World Cup Matches Hosted by Country')
plt.xlabel('Country')
plt.ylabel('Number of Matches')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
