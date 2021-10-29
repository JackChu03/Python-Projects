"""
Name: Jack Chu
"""

import pandas as pd
import matplotlib.pyplot as plt


def main():
	data = pd.read_csv('titanic_data/train.csv')
	print(data.head(6))
	print(data.count())

	plt.figure(figsize=(14, 7))
	#################################
	plt.subplot2grid((3, 4), (0, 0))
	data.Sex.value_counts(normalize=True).sort_index().plot(kind='bar')
	plt.title('Sex')

	plt.subplot2grid((3, 4), (0, 1))
	data.Pclass.value_counts(normalize=True).sort_index().plot(kind='hist')
	plt.title('Pclass')

	plt.subplot2grid((3, 4), (0, 2))
	data.Survived.value_counts(normalize=True).sort_index().plot(kind='bar', color='green')
	plt.title('Survived')

	plt.subplot2grid((3, 4), (1, 0))
	data.Survived[data.Sex == 'male'].value_counts(normalize=True).sort_index().plot(kind='bar', color='pink')
	plt.title('Survived, male')

	plt.subplot2grid((3, 4), (2, 0))
	data.Survived[data.Pclass == 3].value_counts(normalize=True).sort_index().plot(kind='bar', color='pink')
	plt.title('Survived, Pclass')

	plt.subplot2grid((3, 4), (0, 3))
	data.Survived[(data.Sex == 'female') & (data.Pclass == 1)].value_counts(normalize=True).sort_index().plot(kind='bar', color='pink')
	plt.title('Survived, female, rich')

	plt.subplot2grid((3, 4), (1, 3))
	data.Survived[(data.Sex == 'male') & (data.Pclass == 1)].value_counts(normalize=True).sort_index().plot(
		kind='bar', color='pink')
	plt.title('Survived, male, rich')

	##################################

	plt.show()


if __name__ == '__main__':
	main()
