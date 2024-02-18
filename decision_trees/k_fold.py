"""Decision Tree Classifier using k-fold cross validation"""
from numpy import mean
from pandas import DataFrame
from sklearn.metrics import accuracy_score
from sklearn.model_selection import KFold
from sklearn.tree import DecisionTreeClassifier
from data.col_names import TransformedColumns



def decision_tree_classifier_k_fold(
    data_frame: DataFrame,
    features: list[TransformedColumns],
    predicator: TransformedColumns,
) -> None:
    """decision tree classifier using k-fold cross validation"""
    print("""
    ===============================================
    | Decision Tree Classifier with k-fold     |
    ===============================================
    \n""")

    features_str = [str(f) for f in features]
    predicator_str = str(predicator)

    X = data_frame[features_str]
    y = data_frame[predicator_str]

    split_amount = int(
        input("Enter amount of folds that your data frame will be dived into: ")
    )
    k_fold = KFold(
        split_amount,
        shuffle=True,
    ).split(X)

    decision_tree = DecisionTreeClassifier(random_state=2000)

    accuracies = []
    for train_index, test_index in k_fold:
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]

        X_train.columns = X_train.columns.map(str)
        X_test.columns = X_test.columns.map(str)

        decision_tree.fit(X_train, y_train)
        predictions = decision_tree.predict(X_test)

        accuracies.append(accuracy_score(y_test, predictions))

    mean_accuracy = mean(accuracies)

    print(f"Mean accuracy: {mean_accuracy}")
    print(f"Highest accuracy: {max(accuracies)}")
    print(f"Lowest accuracy: {min(accuracies)}")
    
    
