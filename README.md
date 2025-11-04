# NMR_OTOC
Quantum NMR Spectroscopy for Molecular Structure Determination using Out-of-Time-Order Correlators (OTOCs)

**IBM Qiskit Fall Fest Hackathon 2025** | **IIT Roorkee**

This project explores quantum simulation of nuclear magnetic resonance (NMR) dynamics through echo protocols and OTOCs, measuring information scrambling in quantum systems to probe molecular structure.

## Overview

OTOCs (Out-of-Time-Order Correlators) measure information scrambling in quantum systems, providing unique insights into molecular geometry through dipolar-coupled spin dynamics. This implementation demonstrates forward–butterfly–reverse echo protocols on hydrogen networks (H2, H3 ring, H6 ring) in partially ordered media.

## Presentation
- **Slides:** [View Presentation](https://iitracin-my.sharepoint.com/:p:/g/personal/shiva_sj_ph_iitr_ac_in/ERkhWe-jWxNCmEImoXWziUgBUOuf1siH2w-72dLfArZW5Q)
- **Technical Report:** [Read Report](https://jajapuramshivasai.github.io/Quantum_Echo_NMR/)

## Key Features

- **Residual Dipolar Coupling (RDC) calculations** for molecular systems
- **Secular dipolar evolution circuits** using Trotterization
- **Loschmidt Echo (LE) and OTOC protocols** for structural sensitivity
- **FFT-based spectral analysis** with peak highlighting
- **3D molecular visualization** with coupling matrices
- **JSON serialization** for reproducibility

## Running the Notebook

Open and run [Main.ipynb](Main.ipynb) to explore:
- H2 (water-like) molecules
- H3 ring (ammonia-like) molecules  
- H6 ring (benzene-like) molecules

**View online:** [NBViewer](https://nbviewer.org/github/jajapuramshivasai/Quantum_Echo_NMR/blob/main/Main.ipynb)

Each system includes:
- 3D structure visualization
- Dipolar coupling network graphs
- LE/OTOC time traces
- Amplitude and power spectra with peak detection

## Setup Instructions

1. Create a Python virtual environment:
    ```bash
    python3 -m venv .venv
    ```

2. Activate the virtual environment:
    - On macOS/Linux:
      ```bash
      source .venv/bin/activate
      ```
    - On Windows:
      ```bash
      .venv\Scripts\activate
      ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## References

1. **Quantum computation of molecular geometry via nuclear spin echoes**  
   Google Quantum AI  
   [PDF Link](https://quantumai.google/static/site-assets/downloads/quantum-computation-molecular-geometry-via-nuclear-spin-echoes.pdf)

2. **Nature Publication (2025)**  
   [https://www.nature.com/articles/s41586-025-09526-6](https://www.nature.com/articles/s41586-025-09526-6)

## License

This project is developed for the IBM Qiskit Fall Fest Hackathon 2025 at IIT Roorkee.

---

**Author** Jajapuram Shiva Sai 

**Event:** IBM Qiskit Fall Fest Hackathon 2025  

**Institution:** IIT Roorkee
