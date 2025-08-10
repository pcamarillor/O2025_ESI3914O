#  Repository of Big Data subject (Autumn 2025)

Welcome to the repository for submitting lab code and projects for the **Big Data Course - O2025_ESI3914B**. This repository is designed to organize and track your coursework throughout the duration of the class.

## Table of Contents

- [Repository Structure](#repository-structure)
- [How to Submit Assignments](#how-to-submit-assignments)


## Repository Structure

The repository is organized into the following folders:

    ├── collaborators/
    ├── spark/
    │ ├── INSTALL_AND_CONFIGURE_SPARK.md 
    │ ├── notebooks/
    │ │ ├── labs/
    │ │ └── examples
    │ │ └── lib/
    │ ├── data/
    │ ├── docker/
    │ ├── build-images.sh
    │ └── docker-compose.yml 
    └── README.md


## How to Submit Assignments

1. **Clone the Repository**: If you haven't already, clone the repository to your local machine:
    ```bash
    git clone https://github.com/pcamarillor/O2025_ESI3914B.git
    ``` 

2. **Create a branch for each submission**
    ```
    git checkout -b <team_name{# two digits lab number}>
    ```

3. **Add your changes**

4. **Commit your change**
    ```
    git add --all
    git commit -m "Submission Lab{# two digits lab number}"
    ```

5. **Push your changes**
    ```
    git push origin <firstName_LastName_Lab{# two digits lab number}> 
    ```

6. **Create a Pull Request**
    Go to the repository on GitHub and create a pull request from your branch to the main branch.

7. **Submit the Pull Request (PR) URL in Canvas**
    Go to the corresponing to each lab code assigment in Canvas and submit the PR URL.


