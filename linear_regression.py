import csv

def load_column_pair(path, col_x, col_y):
    xs, ys = [], []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            xs.append(row[col_x])
            ys.append(row[col_y])
    return xs, ys

def clean_data(xs, ys):
    clean_x, clean_y = [], []
    for x_raw, y_raw in zip(xs, ys):
        if x_raw == "" or y_raw == "":
            continue
        try:
            clean_x.append(float(x_raw))
            clean_y.append(float(y_raw))
        except ValueError:
            continue
    return clean_x, clean_y

def linear_regression(x, y):
    n = len(x)
    x_mean = sum(x) / n
    y_mean = sum(y) / n

    numerateur = sum((x[i] - x_mean) * (y[i] - y_mean) for i in range(n))
    denominateur = sum((x[i] - x_mean) ** 2 for i in range(n))

    a = numerateur / denominateur
    b = y_mean - a * x_mean
    return a, b

def predict(x_val, a, b):
    return a * x_val + b

if __name__ == "__main__":
    COL_X = "History of Magic"
    COL_Y = "Flying"

    xs_raw, ys_raw = load_column_pair("dataset_train.csv", COL_X, COL_Y)
    x, y = clean_data(xs_raw, ys_raw)

    a, b = linear_regression(x, y)
    print(f"y = {a:.4f}x + {b:.4f}")

    exemple = x[0]
    print(f"predict({exemple:.2f}) = {predict(exemple, a, b):.4f}")