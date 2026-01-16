# Save Luna! – Stereo Depth Map Generation

**Author:** Dev Patel
**Task:** Generate a depth map from stereo images to help a robot (Luna) avoid obstacles.

This project implements a **stereo vision pipeline** that converts a pair of images captured by left and right cameras into a **colorized depth map**. Nearby objects appear in **red**, while distant regions appear in **blue**, enabling Luna to perceive her environment and navigate safely.

The solution is written in **Python using OpenCV**, and compares multiple disparity estimation approaches before selecting **StereoSGBM** for the final implementation.

---

## 🧠 Problem Overview

Luna is a wheeled robot equipped with two horizontally separated cameras. She can *see* her environment but cannot yet *understand depth*. Your task is to teach Luna to perceive distance by:

1. Taking `left.png` and `right.png` images.
2. Computing pixel-wise **disparity**.
3. Converting disparity into a **depth map**.
4. Visualizing depth as a **heatmap**:

   * **Red** → Near objects
   * **Blue** → Far objects

This allows Luna to detect obstacles and make safe movement decisions.

---

## 🔬 Methodology

### 1. Initial Attempts

* **SSD (Sum of Squared Differences)**

  * Accurate but extremely slow.
* **StereoBM (Block Matching)**

  * Fast but noisy and inaccurate in complex regions.

### 2. Final Approach – StereoSGBM

The final solution uses **OpenCV’s StereoSGBM (Semi-Global Block Matching)** algorithm, which:

* Computes matching cost for multiple disparities
* Aggregates costs along multiple paths for smoothness
* Applies:

  * Uniqueness checks
  * Sub-pixel refinement
  * Occlusion handling

This balances **accuracy** and **speed**, producing clean and reliable depth maps.

---

## 📦 Features

* Reads stereo image pairs (`left.png`, `right.png`)
* Computes dense disparity using **StereoSGBM**
* Normalizes and colorizes the disparity map
* Saves the final output as `depth.png`
* Includes comparison with SSD and StereoBM


## 📊 Results

* Clear separation between near and far regions
* Red regions correspond to obstacles close to Luna
* Blue regions indicate background and free space

Comparison:

| Method     | Speed (FPS) | Accuracy | Noise |
| ---------- | ----------- | -------- | ----- |
| SSD        | Very Low    | Medium   | Low   |
| StereoBM   | High        | Low      | High  |
| StereoSGBM | Medium      | High     | Low   |

StereoSGBM offers the best trade-off for real-world robotics.

---

## 🔮 Future Work

* Implement SGBM from scratch for deeper understanding
* Auto-tune parameters based on scene complexity
* Integrate with path-planning and obstacle avoidance
* Explore deep-learning-based disparity (e.g., DispNet)

---

## 🎯 Conclusion

This project successfully teaches Luna to *see in 3D*:

> Two cameras → Compare images → Compute disparity → Generate depth → Colorize → Luna navigates safely

The system forms a strong foundation for autonomous perception in robotics.
