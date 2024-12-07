# Stable Marriage Algorithm Project

## **Overview**
This project implements and analyzes the **Stable Marriage Algorithm** (also known as the Gale-Shapley algorithm) and its variations. The goal is to explore the concept of stable matching, measure satisfaction for both candidates and establishments, and extend the algorithm to support incomplete preferences and compact representations.

---

## **Features**
- **Core Algorithm**: Implementation of the Gale-Shapley stable matching algorithm.
- **Satisfaction Measurement**:
  - Individual satisfaction for candidates and establishments.
  - Overall satisfaction score for a matching.
- **Preference Management**:
  - Generate random preferences for candidates and establishments.
  - Load and manipulate preferences from external files (JSON format).
- **Algorithm Variants**:
  - Support for incomplete preferences and ties in preference rankings.
  - Extension for compact or weighted preferences.
- **Testing**:
  - Unit tests to validate the correctness of algorithms and satisfaction calculations.

---

## **Project Structure**
/mariage_stable
├── main.py # Main script to run the project
├── algorithms/ # Core algorithms and utilities 
  ├── init.py # Package initialization │
  ├── stable_matching.py # Stable marriage algorithm and its variants │
  ├── satisfaction.py # Satisfaction calculation functions │
  ├── preferences.py # Functions to generate/load preferences 
├── data/ # Example data for testing │
  ├── preferences.json # Sample preferences for candidates and establishments 
├── tests/ # Unit tests for the project 
  ├── test_algorithms.py # Tests for stable matching algorithms │
  ├── test_satisfaction.py # Tests for satisfaction calculations │
├── requirements.txt # Project dependencies 
└── README.md # Project documentation

---

## **Getting Started**

### **Prerequisites**
- Python 3.8 or higher
- Recommended: A virtual environment to manage dependencies

### **Setup**
1. Clone the repository:
   ```
   bash
   git clone <repository-url>
   cd mariage_stable
   ```
2. Install the required dependencies:
    ```
    pip install -r requirements.txt
    ```

### **Running the Project**
- To generate random preferences and run the stable matching algorithm, execute:
    ```
    python main.py
    ```


### Testing

### Future Enhancements
- Add visualization for preferences and matchings.
- Optimize the algorithm for large-scale datasets.
- Implement other stable matching algorithms (e.g., hospitals-residents problem).


### Acknowledgments
This project is based on the classic Stable Marriage Problem introduced by David Gale and Lloyd Shapley in 1962.

