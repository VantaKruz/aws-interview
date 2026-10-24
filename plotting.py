plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
sns.scatterplot(x=y_test, y=y_pred, alpha=0.8, color='#2b5c8f', s=60)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2, label='Perfect Fit')
plt.xlabel('Actual Price ($)')
plt.ylabel('Predicted Price ($)')
plt.title('Actual vs Predicted Prices')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

plt.subplot(1, 2, 2)
sns.histplot(df_clean['price_usd'], kde=True, color='#2b8f62', bins=20)
plt.xlabel('Price ($)')
plt.title('Price Distribution')
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()

X_train_b = np.c_[np.ones((len(X_train), 1)), X_train]
theta_best = np.linalg.inv(X_train_b.T.dot(X_train_b)).dot(X_train_b.T).dot(y_train)

print("\n--- Normal Equation vs Scikit-Learn Comparison ---")
print("Normal Equation Coefficients:", np.round(theta_best, 2))
print("Scikit-learn Intercept & Coefs:", np.round([model.intercept_] + list(model.coef_), 2))