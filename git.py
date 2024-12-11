import requests
import pandas as pd
import matplotlib.pyplot as plt

BASE_URL = "https://api.github.com"
TOKEN = "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"  
def fetch_repos(username):
    """Fetch repositories for a given GitHub username."""
    url = f"{BASE_URL}/users/{username}/repos"
    headers = {"Authorization": f"token {TOKEN}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch repos for {username}: {response.status_code}")
        return []

def analyze_repo(repo):
    """Analyze a single repository."""
    return {
        "Repo Name": repo["name"],
        "Stars": repo["stargazers_count"],
        "Forks": repo["forks_count"],
        "Open Issues": repo["open_issues_count"],
        "Last Commit Date": repo["updated_at"],
    }

def analyze_user_repos(usernames):
    """Analyze repositories for multiple GitHub usernames."""
    results = []
    for username in usernames:
        print(f"Fetching repositories for {username}...")
        repos = fetch_repos(username)
        for repo in repos:
            results.append(analyze_repo(repo))
    return results

def plot_data(df):
    """Plot data using matplotlib."""
    df["Last Commit Date"] = pd.to_datetime(df["Last Commit Date"], errors="coerce")

    df = df.sort_values("Last Commit Date", ascending=True)

    plt.figure(figsize=(10, 6))
    plt.barh(df["Repo Name"], df["Last Commit Date"].astype(str), color="skyblue")

    plt.xlabel("Last Commit Date")
    plt.ylabel("Repository Name")
    plt.title("Last Commit Date by Repository")
    plt.tight_layout()
    plt.xticks(rotation=45)

    plt.savefig("last_commit_date_visualization.png")
    print("Bar graph saved as 'last_commit_date_visualization.png'")

    plt.show()

def main():
    usernames = ["rn-harsh04"]  

    data = analyze_user_repos(usernames)

    df = pd.DataFrame(data)
    print(df)

    df.to_csv("github_repos_analysis.csv", index=False)
    print("Data saved to github_repos_analysis.csv")

    if not df.empty:
        plot_data(df)

if __name__ == "__main__":
    main()
