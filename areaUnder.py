
def areaunder2():
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
    df = pd.read_csv("creditcard.csv")


    # calculate the correlation matrix
    corr = df.corr()


    plt.figure(figsize=(15,8))

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

    from sklearn.metrics import precision_recall_curve
    from sklearn.metrics import auc
    import matplotlib.pyplot as plt

    # Make predictions
    y_pred = classifier.predict(X_test)

    # Create precision-recall curve
    precision, recall, thresholds = precision_recall_curve(y_test, y_pred)

    # Calculate AUC
    auc_value = auc(recall, precision)

    # Plot the precision-recall curve
    plt.plot(recall, precision, label='AUC={0:0.2f}'.format(auc_value))
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curve')
    plt.legend()
    plt.show()

    # An area under the precision-recall curve (AUC-PR) of 0.78 means that the model has a good ability to distinguish between 
    # the positive class (fraud) and the negative class (not fraud) in the data. 
    # A value of 1 represents a perfect model, and a value of 0.5 represents a model that is no better than random. 
    # So, AUC-PR of 0.78 implies that the model has a relatively good performance in identifying fraudulent transactions.
