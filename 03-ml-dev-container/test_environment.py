"""
Sample ML script to verify your dev container setup.
This script trains a simple classifier on the iris dataset.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd


def main():
    print("🌸 Loading Iris dataset...")
    iris = load_iris()
    X, y = iris.data, iris.target
    
    print(f"📊 Dataset shape: {X.shape}")
    print(f"🎯 Classes: {iris.target_names}")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print(f"\n🔄 Training Random Forest classifier...")
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    # Predictions
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\n✅ Model trained successfully!")
    print(f"🎯 Accuracy: {accuracy:.2%}")
    
    print(f"\n📋 Classification Report:")
    print(classification_report(y_test, y_pred, target_names=iris.target_names))
    
    # Feature importance
    feature_importance = pd.DataFrame({
        'feature': iris.feature_names,
        'importance': clf.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print(f"\n🔍 Feature Importance:")
    print(feature_importance.to_string(index=False))
    
    print(f"\n🎉 Dev container is working correctly!")


if __name__ == "__main__":
    main()
