import numpy as np
from collections import deque
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense


class LSTMBrianV321:
    """
    v3.2.1 LSTM Forecast Brain
    - Learns sequential system behavior
    - Predicts next state from history
    """

    def __init__(self, window_size=5):
        self.window_size = window_size

        # sliding time window
        self.data = deque(maxlen=window_size)

        self.model = self._build_model()
        self.trained = False

    # -----------------------------
    # 🏗 MODEL BUILD
    # -----------------------------
    def _build_model(self):
        model = Sequential()

        model.add(LSTM(32, input_shape=(self.window_size, 1)))
        model.add(Dense(1))

        model.compile(optimizer="adam", loss="mse")

        return model

    # -----------------------------
    # 🧾 INGEST DATA
    # -----------------------------
    def ingest(self, value: float):
        """
        value: normalized metric (0-1)
        """
        self.data.append(value)

    # -----------------------------
    # 🧠 TRAIN MODEL
    # -----------------------------
    def train(self, epochs=10):

        if len(self.data) < self.window_size:
            return "Not enough data"

        X = []
        y = []

        data = list(self.data)

        for i in range(len(data) - self.window_size):
            X.append(data[i:i+self.window_size])
            y.append(data[i+self.window_size])

        X = np.array(X)
        y = np.array(y)

        X = X.reshape((X.shape[0], X.shape[1], 1))

        self.model.fit(X, y, epochs=epochs, verbose=0)

        self.trained = True

        return "LSTM trained"

    # -----------------------------
    # 🔮 PREDICT NEXT VALUE
    # -----------------------------
    def predict_next(self):

        if not self.trained or len(self.data) < self.window_size:
            return {"prediction": None}

        input_seq = np.array(list(self.data)[-self.window_size:])
        input_seq = input_seq.reshape((1, self.window_size, 1))

        pred = self.model.predict(input_seq, verbose=0)[0][0]

        return {
            "next_value": float(pred),
            "risk": "HIGH" if pred > 0.7 else "LOW"
        }

    # -----------------------------
    # 📊 TREND ANALYSIS
    # -----------------------------
    def trend(self):

        if len(self.data) < 2:
            return {"trend": "INSUFFICIENT DATA"}

        arr = np.array(self.data)

        diff = np.diff(arr)

        direction = "UPWARD" if diff.mean() > 0 else "DOWNWARD"

        return {
            "trend": direction,
            "volatility": float(np.std(diff))
        }

    # -----------------------------
    # 📡 REPORT
    # -----------------------------
    def report(self):

        return {
            "trained": self.trained,
            "data_points": len(self.data),
            "prediction": self.predict_next(),
            "trend": self.trend()
        }