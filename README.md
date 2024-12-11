# GitHub Repository Analyzer

# Overview

This project is a Python-based tool designed to fetch and analyze GitHub repository data for one or more GitHub users. The tool retrieves important repository metrics such as the number of stars, forks, open issues, and the last commit date. It provides the analyzed data in a tabular format and visualizes it using bar graphs to aid in understanding trends and repository activities.

#Features

Fetches repositories for given GitHub usernames using the GitHub API.
Retrieves and analyzes key metrics for each repository, including:
Repository Name
Number of Stars
Number of Forks
Open Issues
Last Commit Date
Saves the analyzed data to a CSV file (github_repos_analysis.csv).
Visualizes the "Last Commit Date" for repositories using a horizontal bar graph.
Supports sorting repositories by the last commit date for better visualization

# Requirements

Python 3.7 or above
GitHub Personal Access Token (for authenticated API access to avoid rate limits)

# Python Libraries Used

requests: To fetch data from the GitHub API.
pandas: To process and structure the data.
matplotlib: To visualize repository metrics.

# Visualization

A horizontal bar graph visualizing the "Last Commit Date" for each repository is saved as an image.

# Future Improvements

Add support for reading usernames from a file.
Enhance visualizations with more metrics (e.g., stars, forks).
Implement asynchronous API calls for improved performance with large user lists.

# Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests.
