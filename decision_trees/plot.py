import matplotlib.pyplot as plot

def create_plot(plot_name: str, max_range: int, accuracies: list) -> None:
    plot_range = range(1, (max_range + 1)) 
    path = f"data/decision_tree_{plot_name}.png"
    
    plot.figure(figsize=(10, 6))
    plot.plot(plot_range, accuracies, marker="o", linestyle="-", color="blue")
    plot.title(f"Decision Tree Accuracy vs. {plot_name}")
    plot.xlabel("Max Depth/Folds of Tree")
    plot.ylabel("Accuracy")
    plot.xticks(plot_range)
    plot.grid(True)
    plot.savefig(path)
    plot.show()

    print(f"Plot saved to {path}")