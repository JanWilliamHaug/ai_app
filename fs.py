def areaover():

    from sklearn.ensemble import RandomForestClassifier
    from sklearn.datasets import make_classification

    # Importing necessary libraries
    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import confusion_matrix
    import seaborn as sns
    import matplotlib.pyplot as plt

    # Reading the dataset
    #df = pd.read_csv("creditcard.csv")
    #url='https://drive.google.com/file/d/1KZjzaMNSOkUTfLZWqA70wY4H-34i5jon/view?usp=sharing'
    #url='https://drive.google.com/uc?id=' + url.split('/')[-2]
    #df = pd.read_csv(url)

    
    df = pd.read_csv("creditcard.csv)
    
    # calculate the correlation matrix
    corr = df.corr()

    plt.figure(figsize=(19.5,9))
    sns.heatmap(df.corr(),annot=True,cmap='coolwarm',mask=np.triu(np.ones(df.corr().shape)),fmt='.2f',linewidths=.05)

    # display the correlation matrix
    print(corr)


    # Splitting the data into features and labels
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values

    # Splitting the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

    # Training the model
    classifier = DecisionTreeClassifier()
    classifier.fit(X_train, y_train)

    # Making predictions on the test set
    y_pred = classifier.predict(X_test)

    # Evaluating the model
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy:", accuracy)

    confusion_matrix = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:", confusion_matrix)

    # Create the histogram
    plt.hist(df, bins=20)

    # # # Add a title and labels
    plt.title("Fraudulent System histogram data")
    plt.xlabel("Data values")
    plt.ylabel("Frequency")

    # # Show the plot
    plt.show()
