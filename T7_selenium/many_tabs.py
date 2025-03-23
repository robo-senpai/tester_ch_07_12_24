from selenium import webdriver
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Wait for elements to appear on the page for a maximum of 5 seconds
driver.implicitly_wait(5)

# Open multiple tabs
driver.get("https://www.google.com")  # First tab
driver.execute_script("window.open('https://www.bing.com');")  # Second tab
driver.execute_script("window.open('https://www.yahoo.com');")  # Third tab

# Wait for the tabs to load
time.sleep(5)

# Print the window handles for debugging
print("Window Handles:", driver.window_handles)

# Dictionary to store tabs with titles as keys
tabs_dict = {}

# Store tab handles with page titles as keys
for tab in driver.window_handles:
    driver.switch_to.window(tab)
    title = driver.title.lower().replace(" ", "_").strip()  # Convert title into a valid key

    # Avoid using empty or invalid titles
    if title:  
        tabs_dict[title] = tab
    else:
        # If the title is empty or invalid, skip this tab or handle it differently
        print("Empty or invalid title:", tab)

# Print stored tab handles
print("Tabs Dictionary:", tabs_dict)

# Switch to Bing tab using the dictionary (example)
bing_tab = tabs_dict.get("bing")
if bing_tab:
    driver.switch_to.window(bing_tab)
    print("Switched to Bing tab:", driver.title)
else:
    print("Bing tab not found!")

# Stop to see the result
time.sleep(3)

# Cleanup
driver.quit()