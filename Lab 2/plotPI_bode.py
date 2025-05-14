import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, bode

# Define PI controller: C_PI(s) = (s + z_PI) / s
z_PI = 10
numerator = [1, z_PI]  # (s + z_PI)
denominator = [1, 0]    # (s)

# Create transfer function
C_PI = TransferFunction(numerator, denominator)

# Frequency range
w = np.logspace(-2, 4, 1000)  # Log scale from 0.01 to 100 rad/s

# Compute Bode magnitude and phase
w, mag, phase = bode(C_PI, w)

# Plot Bode magnitude
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.semilogx(w, mag)  # Magnitude plot (dB scale)
plt.xlabel("Frequency (rad/s)")
plt.ylabel("Magnitude (dB)")
plt.title("Bode Plot of PI Controller, $z_{PI} = 10$")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

# Plot Bode phase
plt.subplot(2, 1, 2)
plt.semilogx(w, phase)  # Phase plot (degrees)
plt.xlabel("Frequency (rad/s)")
plt.ylabel("Phase (degrees)")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.savefig("PI_bode.png")
plt.tight_layout()
plt.show()
