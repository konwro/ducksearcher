# Task: open web search results for keyword in .xlsx, .txt, .csv format in new tabs
# Step 0: imports
import pandas as pd
import webbrowser
import time

# Step 1: get list of keywords
keywords = pd.read_csv(r'filepath/file.txt')

print(keywords.shape)
print(keywords.head)

# Step 2: duckduckgo search operators - https://help.duckduckgo.com/duckduckgo-help-pages/results/syntax/
    # filetype:
    # site:
    # intitle:
    # news
    # map

# Step 3: get search results for target strings in web browser
results_urls = []

for key in keywords['column']:
    browse_url = 'https://duckduckgo.com/?q=' + str(key)
    # print(browse_url)
    results_urls.append(browse_url)

# # Step 4: open search results in firefox browser
c = webbrowser.get('firefox') 

for url in results_urls:
  c.open_new_tab(url)
  print(url)
  time.sleep(3)

# # Step 5: TBD/Finish
print('======================All URLs have been opened======================')



