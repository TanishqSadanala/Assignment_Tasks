import requests
from bs4 import BeautifulSoup
import csv
from tabulate import tabulate


def fetch_html(url):
    '''
    fetching the data and checking the response status.
    '''
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(
            f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None


def extract_mobile_data(soup):
    '''
    all the data is sent into the mobile_data array.
    assert statements catch the assert_exceptional handling
    '''
    mobile_data = []

    mobile_div = soup.find('div', {'id': 'column-mobileMedian'})
    assert mobile_div, "Div with id 'column-mobileMedian' not found."

    table = mobile_div.find('table', {'class': 'list-results'})
    assert table, "Table with class 'list-results' not found in mobile_div."

    tbody = table.find('tbody')
    assert tbody, "Tbody not found within the table."

    rows = tbody.find_all('tr', {'class': 'data-result'})
    assert rows, "No rows with class 'data-result' found in tbody."

    for rank, row in enumerate(rows, start=1):
        country = row.find('td', {'class': 'country'}).text.strip()
        speed = row.find('td', {'class': 'speed'}).text.strip()
        mobile_data.append([rank, country, speed])

    return mobile_data


def extract_broadband_data(soup):
    '''
    all the data is sent into the broadband array.
    assert statements catch the assert_exceptional handling
    '''
    broadband_data = []

    broadband_div = soup.find('div', {'id': 'column-fixedMedian'})
    assert broadband_div, "Div with id 'column-fixedMedian' not found."

    table = broadband_div.find('table', {'class': 'list-results'})
    assert table, "Table with class 'list-results' not found in broadband_div."

    tbody = table.find('tbody')
    assert tbody, "Tbody not found within the table."

    rows = tbody.find_all('tr', {'class': 'data-result'})
    assert rows, "No rows with class 'data-result' found in tbody."

    for rank, row in enumerate(rows, start=1):
        country = row.find('td', {'class': 'country'}).text.strip()
        speed = row.find('td', {'class': 'speed'}).text.strip()
        broadband_data.append([rank, country, speed])

    return broadband_data


def save_to_csv(data, filename):
    '''
    method to save all the data in the csv file.
    '''
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def main():
    '''
    url parsing 
    Extract and save mobile data
    Extract and save broadband data
    Display data using tabulate
    '''
    url = "https://www.speedtest.net/global-index"
    html = fetch_html(url)

    if html:
        soup = BeautifulSoup(html, 'html.parser')

        mobile_data = extract_mobile_data(soup)
        mobile_rows = [['Rank', 'Country', 'Speed (Mbps)']] + mobile_data
        save_to_csv(mobile_rows, 'mobile_info.csv')

        broadband_data = extract_broadband_data(soup)
        broadband_rows = [['Rank', 'Country', 'Speed (Mbps)']] + broadband_data
        save_to_csv(broadband_rows, 'broadband_info.csv')

        print("Mobile Data:")
        print(tabulate(mobile_rows, headers="firstrow", tablefmt="grid"))

        print("\nFixed Broadband Data:")
        print(tabulate(broadband_rows, headers="firstrow", tablefmt="grid"))

        print("Data has been saved to 'mobile_info.csv' and 'broadband_info.csv'")


if __name__ == "__main__":
    main()
    