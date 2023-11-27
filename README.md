# flipkart-web-scraping-python-project

**Overview**

This Python script is designed to scrape laptop data from Flipkart's website using the BeautifulSoup package and the requests library. The scraped data is then stored in a CSV file named flipkart_data.csv.

**Prerequisites**

Before running the script, ensure that you have the following dependencies installed:

    Python 3.x
    bs4 library for BeautifulSoup
    Requests library

You can install the required packages using the following command:

    pip install bs4
    pip install requests
  
**Usage**

Clone the repository to your local machine:

    git clone https://github.com/sb21feb/flipkart-web-scraping-python-project.git

The script will start scraping list of laptops with their data and will display the progress on the console. Once the scraping is complete, the data will be saved to a file named flipkart_data.csv in the same directory.

**Configuration**

You can customize the script by modifying the following parameters in the main.py file:

https://www.flipkart.com/laptops/pr?sid=6bo,b5g&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_48b7db82-1162-4e18-9fd7-7e0e47dad627_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker=hp_rich_navigation_8_1.navigationCard.RICH_NAVIGATION_Electronics~Laptop%2Band%2BDesktop_34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_8_L1_view-all&cid=34WHNYFH5V2Y : The URL of the Amazon page containing the list of laptops.
User-Agent: The name of the User Agent. It is removed from file for security purposes

**Disclaimer**

This script is intended for educational and personal use only.

**Contributing**

If you encounter any issues, feel free to open an issue on the GitHub repository. Contributions are welcome!

**License**

This project is licensed under the MIT License - see the LICENSE file for details.
