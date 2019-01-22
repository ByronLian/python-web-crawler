import requests
from bs4 import BeautifulSoup

# This function is used to get entire page from specific url
def get_html(url):
  # https://www.google.com/search?q=my+user+agent Find user agent
  headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    
  # http://docs.python-requests.org/en/master/user/quickstart/#make-a-request
  content = requests.get(url, headers = headers)
  return content.text


# This function is used to process stock info
def get_result_from_html(html, stock_no):
    html_content = BeautifulSoup(html, 'html.parser')
    
    # Processing HTML DOM data
    name = html_content.find('h3', class_='idx-name').get_text()
    bid_price = html_content.find('span', class_='price').get_text()
    change = html_content.find('span', class_='chg').get_text()

    # Save result
    final_result = "Stock Name: {}\n Bid Price: {}\n Change{}\n\n\n"
    save_final_result(final_result.format(name, bid_price, change))


# This function is used to save result to txt file
# Note: will change to Database later
def save_final_result(*args):
  try:
      for i in args:
        with open('stock_info.txt', 'a', encoding='utf-8') as file:
          file.write(i)
  except:
      print('something wrong')
  finally:
      file.close()

def main():
  stock_ary = ['0050', '2330'] # Stock serial number
  stock_ary_length = len(stock_ary)

  for i in range(0, stock_ary_length):
    url = 'https://www.wantgoo.com/stock/' + stock_ary[i]
    html = get_html(url)
    get_result_from_html(html, stock_ary[i])


if __name__ == '__main__':
  main()