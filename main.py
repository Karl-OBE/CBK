from fastapi import FastAPI
import random

app = FastAPI(title="O.M.L.I. Phase 1 - Tennis Prediction Engine")

@app.get("/")
def read_root():
    return {"status": "O.M.L.I. Tennis Engine is live!"}

    @app.get("/predict")
    def predict_outcome(player_a: str, player_b: str):
        """
            Simple mock prediction for now – generates a random win probability.
                This will later be replaced with real data and models.
                    """
                        confidence = round(random.uniform(0.85, 0.99), 3)
                            winner = player_a if confidence > 0.92 else player_b
                                return {
                                        "predicted_winner": winner,
                                                "confidence": f"{confidence * 100:.1f}%",
                                                        "player_a": player_a,
                                                                "player_b": player_b
                                                                    }