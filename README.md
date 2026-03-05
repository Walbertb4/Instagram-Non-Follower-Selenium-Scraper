# Instagram Unfollower Tracker

This **Python** project uses the **Selenium** and **BeautifulSoup** libraries to automatically log into Instagram, scrape your followers and following lists, and identify the users who do not follow you back. It features a custom, color-coded terminal interface and saves your scraped data locally.

---

## Features

* **Secure Terminal Login:** Securely prompts for your Instagram username and password directly in the console with a clean UI.
* **2FA Detection:** Automatically detects if Two-Factor Authentication (Authenticator app/SMS) is required, pauses the script, and waits for your manual intervention.
* **Automated List Scraping:** Opens the followers and following dialogs, automatically scrolls to the bottom using JavaScript, and parses the HTML to extract usernames.
* **Non-Follower Analysis:** Compares your lists to accurately pinpoint users you follow who don't follow you back.
* **Data Export:** Automatically exports and saves your followers, following, and non-followers to a local `instagramlist.txt` file.
* **Sleek Terminal UI:** Provides real-time, color-coded updates and ASCII borders right in your command line.

---

## Installation and Requirements

To run this project, you must have **Python 3.x** and the **Google Chrome** browser installed on your computer.

1. Clone this repository or download the project files.
2. Open a terminal in the project directory.
3. Install the required libraries by running the following command:

```bash
pip install -r requirements.txt
```

---

## Usage

1. Open your terminal and navigate to the folder containing the project.
2. Run the script:

```bash
python main.py
```

3. When the prompt appears in the terminal, enter your Instagram **Username** and **Password**.
4. **Important:** If you have Two-Factor Authentication enabled, solve the challenge in the opened Chrome window, then return to the terminal and press any key to continue.
5. Sit back and wait for the bot to finish scrolling. Your non-followers will be printed in the terminal and saved to the text file!

---

> **⚠️ Disclaimer:** This script is for educational purposes. Instagram frequently updates its web structure and actively monitors bot activity. Aggressive scraping may trigger temporary action blocks or require account verification. Please use responsibly.
