"""Decision Tree Classifier basic and max depth analysis"""
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    classification_report,
    confusion_matrix as sklearn_confusion_matrix,
    accuracy_score,
)
from sklearn.tree import DecisionTreeClassifier
from data.col_names import TransformedColumns
from decision_trees.plot import create_plot



def decision_tree_classifier_basic(
    data_frame: DataFrame,
    features: list[TransformedColumns],
    predicator: TransformedColumns,
) -> None:
    """basic version of decision tree classifier"""
    print(
        """
    ===============================================
    | Decision Tree Classifier basic              |
    ===============================================
    \n"""
    )
    (X_train, X_test, y_train, y_test) = train_test_split(
        data_frame[features], data_frame[predicator], test_size=0.2
    )

    X_train.columns = X_train.columns.map(str)
    X_test.columns = X_test.columns.map(str)

    max_depth = int(input("Enter the depth tree number: "))
    show_plot = input("Do you want to see the plot with all tree depths comparison? (y/n): ")
    
    if show_plot.lower() == "y":
        decision_tree_classifier_max_depths(max_depth, X_train, y_train, X_test, y_test, predicator)

    decision_tree = DecisionTreeClassifier(max_depth=max_depth, random_state=2000)

    decision_tree.fit(X_train, y_train)

    predictions = decision_tree.predict(X_test)

    # EVALUATION METRICS
    classification_report_showcase(y_test, predictions)
    confusion_matrix_showcase(y_test, predictions)
    general_accuracy_showcase(y_test, predictions)


def decision_tree_classifier_max_depths(
    max_depth: int,
    X_train: DataFrame,
    y_train: DataFrame,
    X_test: DataFrame,
    y_test: DataFrame,
    col_name: str,
) -> None:
    """Analyzes Decision Tree Classifier performance over a range of tree depths"""
    print(
        """
    =================================================
    | Decision Tree Depth Analysis                  |
    =================================================
    \n"""
    )

    accuracies = []

    for depth in range(1, (max_depth + 1)):
        decision_tree = DecisionTreeClassifier(max_depth=depth, random_state=2000)
        decision_tree.fit(X_train, y_train)
        predictions = decision_tree.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        accuracies.append(accuracy)
        
    create_plot(f"{col_name}_max_depth", max_depth, accuracies)


def confusion_matrix_showcase(y_test, predictions) -> None:
    """function to showcase the confusion matrix"""
    confusion_matrix = sklearn_confusion_matrix(y_test, predictions)

    TP = confusion_matrix[1][1]
    TN = confusion_matrix[0][0]
    FP = confusion_matrix[0][1]
    FN = confusion_matrix[1][0]

    print(
        f"""
        Confusion Matrix:
        
        {confusion_matrix}
        That is:
        True Positive (TP): {TP}
        True Negative: (TN) {TN}
        False Positive: (FP) {FP}
        False Negative: (FN) {FN}
        
        The equation for the confusion matrix is as follows:
        Precision = TP / (TP + FP)
        which is:
        Precision = {round(TP/(TP + FP), 3)}
    """
    )


def general_accuracy_showcase(y_test, predictions) -> None:
    """function to showcase the general accuracy"""
    accuracy = accuracy_score(y_test, predictions)
    print(
        f"""Accuracy: 
          {accuracy}
          The accuracy value ranges from 0 to 1, where 1 is the best possible value, and 0- the worst one.
          """
    )


def classification_report_showcase(y_test, predictions) -> None:
    """function to showcase the classification report"""
    print(
        f"""Classification Report:
          {classification_report(y_test, predictions)}
          """
    )
