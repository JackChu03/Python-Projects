import pandas as pd


def main():
    data = pd.read_csv('titanic_data/train.csv')
    data['Hypo'] = 0
    data.loc[data.Sex == 'female', 'Hypo'] = 1

    data['Result'] = 0
    data.loc[data.Survived == data.Hypo, 'Result'] = 1

    print(data.Result.value_counts(normalize=True))


if __name__ == '__main__':
    main()
