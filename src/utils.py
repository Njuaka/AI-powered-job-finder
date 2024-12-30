import os
import csv
import pandas as pd
import numpy as np  


def get_root_dir():
    """
    Get the root directory of the project

    Returns:
        _type_: str
    """
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return root_dir



# Save results to CSV
def save_to_csv(results, file_path):
    """

    Args:
        results (_type_): job search results
        file_path (_type_): path to save the results
    """
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Company Name", "Registration Number", "Job Source", "Job Title/Info", "Job Link"])
        writer.writerows(results)