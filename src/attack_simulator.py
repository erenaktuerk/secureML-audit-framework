from art.attacks.evasion import FastGradientMethod
from art.estimators.classification import SklearnClassifier
from art.attacks.inference.membership_inference import MembershipInferenceBlackBoxRuleBased
from sklearn.metrics import accuracy_score
import numpy as np

def run_adversarial_attack(model, X_test, y_test):
    classifier = SklearnClassifier(model=model)
    attack = FastGradientMethod(estimator=classifier, eps=0.2)

    X_adv = attack.generate(x=X_test)
    preds = np.argmax(classifier.predict(X_adv), axis=1)

    acc = accuracy_score(y_test, preds)
    print(f"Accuracy on adversarial examples: {acc:.2f}")

def run_model_inversion(model, X_train):
    print("Model inversion attack not implemented. Placeholder only.")

def prompt_injection_demo():
    print("Prompt injection demo requires OpenAI API setup. Placeholder only.")