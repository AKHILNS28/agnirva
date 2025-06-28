To run the **Agnirva Natural Disaster Tracker**, follow these comprehensive step-by-step instructions. This guide is crafted for individuals with no prior experience in coding or running web applications. By the end of this guide, you will have a fully functional webpage that displays various natural disaster events on an interactive map using NASA's EONET API.

---

### **1. Ensure You Have the Necessary Equipment**

Before we begin, make sure you have the following:

- **A Computer**: This can be a desktop or laptop running Windows, macOS, or Linux.
- **Internet Connection**: Required to fetch data from NASA's EONET API and load external resources like Leaflet.
- **Web Browser**: Such as Google Chrome, Mozilla Firefox, Microsoft Edge, or Safari.
- **Text Editor**: A program to write and edit code. Common text editors include:
  - **Windows**: Notepad (pre-installed)
  - **Mac**: TextEdit (pre-installed) – *ensure it's set to plain text*
  - **Cross-Platform**: [Visual Studio Code](https://code.visualstudio.com/), [Sublime Text](https://www.sublimetext.com/), or [Atom](https://atom.io/) (optional but recommended for better features)

---

### **2. Open Your Text Editor**

We'll use the text editor to create an HTML file that contains the code for the Natural Disaster Tracker.

- **On Windows**:
  1. Click the **Start** button.
  2. Type **Notepad** in the search bar and press **Enter**.

- **On Mac**:
  1. Open **Finder**.
  2. Navigate to the **Applications** folder.
  3. Open **TextEdit**.
  4. Once open, go to the top menu and select **Format > Make Plain Text** to ensure the file saves correctly.

- **Using a Code Editor (Optional)**:
  - If you have Visual Studio Code, Sublime Text, or Atom installed, you can open it for a more enhanced coding experience.

---

### **3. Copy the Provided Code**

You will be provided with a block of code (HTML, CSS, and JavaScript). Follow these steps to copy it:

1. **Select the Code**:
   - Click and drag your mouse cursor over the entire code block to highlight it.

2. **Copy the Code**:
   - **Right-Click Method**:
     - Right-click on the highlighted text and select **Copy**.
   - **Keyboard Shortcut**:
     - Press `Ctrl+C` on Windows or `Command+C` on Mac.

*Ensure you copy all the code provided, starting with `<!DOCTYPE html>` and ending with `</html>`.*

---

### **4. Paste the Code into the Text Editor**

With your text editor open and ready:

1. **Click Inside the Text Editor**:
   - Ensure your cursor is active within the blank document.

2. **Paste the Code**:
   - **Right-Click Method**:
     - Right-click and select **Paste**.
   - **Keyboard Shortcut**:
     - Press `Ctrl+V` on Windows or `Command+V` on Mac.

*The entire code should now appear in your text editor.*

---

### **5. Save the File as an HTML Document**

Saving the file correctly is crucial for your web browser to recognize and display it properly.

- **On Windows (Using Notepad)**:
  1. Click on **File** in the top-left corner.
  2. Select **Save As**.
  3. **Choose a Location**:
     - For easy access, select the **Desktop**.
  4. **Name the File**:
     - Enter `natural_disaster_tracker.html` in the **File name** field.
  5. **Set File Type**:
     - In the **Save as type** dropdown, select **All Files**.
  6. **Encoding**:
     - Ensure **UTF-8** is selected to support all characters.
  7. Click **Save**.

- **On Mac (Using TextEdit)**:
  1. Click on **File** in the top menu.
  2. Select **Save**.
  3. **Choose a Location**:
     - For easy access, select the **Desktop**.
  4. **Name the File**:
     - Enter `natural_disaster_tracker.html` in the **Save As** field.
  5. **Ensure Correct Format**:
     - Make sure the file is being saved as **Plain Text**.
  6. Click **Save**.

- **Using a Code Editor (Optional)**:
  - Follow similar steps as above to save the file with a `.html` extension.

---

### **6. Open the HTML File in Your Web Browser**

Now, let's view your Natural Disaster Tracker in action.

1. **Navigate to the Saved File**:
   - Go to the location where you saved `natural_disaster_tracker.html` (e.g., Desktop).

2. **Open the File**:
   - **Double-Click Method**:
     - Double-click on `natural_disaster_tracker.html`. It should automatically open in your default web browser.
   - **Right-Click Method**:
     - Right-click on `natural_disaster_tracker.html`.
     - Select **Open With** and choose your preferred web browser (e.g., Google Chrome, Firefox).

3. **What You Should See**:
   - A webpage titled **"Agnirva Natural Disaster Tracker"** with a control panel at the top and an interactive map below.
   - The control panel includes options to select the **Event Category**, specify the **Past Days**, and a **Fetch Events** button.
   - The map covers most of the page, displaying markers for various natural disaster events based on your selections.

---

### **7. Using the Natural Disaster Tracker Application**

Interact with the application to explore recent natural disaster events around the world.

1. **Select an Event Category**:
   - At the top of the page, find the **"Event Category"** dropdown menu.
   - Click on it and choose a specific category, such as **Wildfires**, **Severe Storms**, or **Volcanoes**.
   - *If you want to view all event categories, select **All**.*

2. **Specify the Number of Past Days**:
   - Next to the **"Past Days"** label, there's a number input box.
   - Enter the number of past days you want to look back for events. For example, entering **30** will fetch events from the last 30 days.
   - *You can enter a value between **1** and **365**.*

3. **Fetch Events**:
   - After selecting your desired category and number of days, click the **"Fetch Events"** button.
   - The application will process your request and display relevant events on the map.

4. **Viewing Events on the Map**:
   - Markers will appear on the map indicating the locations of the selected natural disaster events.
   - **Click on a Marker**:
     - When you click on a marker, a popup will display:
       - **Title**: Name of the event.
       - **Date**: When the event occurred.
       - **Description**: Additional details about the event.

5. **Interacting with the Map**:
   - **Zoom In/Out**: Use your mouse scroll or the zoom buttons on the map to get a closer or broader view.
   - **Pan Around**: Click and drag the map to move to different regions.

6. **Fetch New Events**:
   - To view different events, change the **Event Category** or **Past Days** and click **"Fetch Events"** again.

---

### **8. Understanding the Application Interface**

Here's a breakdown of the application's main components:

- **Header Section**:
  - Displays the title **"Agnirva Natural Disaster Tracker"**.

- **Control Panel (`#controls`)**:
  - **Event Category Dropdown**:
    - Allows you to filter events by category (e.g., Wildfires, Severe Storms, Volcanoes).
  - **Past Days Input**:
    - Lets you specify how many days back you want to search for events.
  - **Fetch Events Button**:
    - Initiates the retrieval and display of events based on your selections.

- **Map Area (`#map`)**:
  - An interactive map powered by **Leaflet** and **OpenStreetMap** tiles.
  - Displays markers for each natural disaster event fetched from NASA's EONET API.

---

### **9. Responsive Design for Mobile Users**

The application is designed to be responsive, meaning it adapts to different screen sizes for optimal viewing on various devices.

- **On Smartphones and Tablets**:
  - The control panel stacks vertically for easier navigation.
  - The map remains fully interactive and adjusts to fit the screen.

- **On Smaller Screens**:
  - Text sizes and input fields resize to fit the screen without requiring horizontal scrolling.

*This ensures that whether you're using a desktop, laptop, tablet, or smartphone, the application remains user-friendly and accessible.*

---

### **10. Troubleshooting Common Issues**

If you encounter any problems while running the application, try the following solutions:

- **Events Not Loading or Showing Errors**:
  - **Check Internet Connection**: Ensure your device is connected to the internet.
  - **API Endpoint Changes**:
    - NASA's EONET API endpoint might have changed. Verify the API URL in the code or check [NASA's EONET API Documentation](https://eonet.gsfc.nasa.gov/) for updates.
  
- **Markers Not Appearing on the Map**:
  - **Incorrect API Response**:
    - The API might not be returning data in the expected format. Open the browser's developer console (usually by pressing `F12` or `Ctrl+Shift+I`) to check for any JavaScript errors.
  - **Event Categories Mapping**:
    - Ensure that the category mappings in the code match the current category IDs from the EONET API. Categories may be updated or changed over time.

- **Styling Issues**:
  - **External Resources Not Loading**:
    - The application relies on external URLs for Leaflet's CSS and JavaScript. Ensure your internet connection is active.
    - If the map or styles aren't loading, try refreshing the page or checking your internet connection.

- **Browser Compatibility**:
  - **Outdated Browser**:
    - Ensure you are using an up-to-date version of your web browser for the best experience.
  - **JavaScript Disabled**:
    - The application uses JavaScript to fetch and display data. Make sure JavaScript is enabled in your browser settings.

- **Date Input Issues**:
  - **Invalid Date Range**:
    - Ensure that the number of past days entered does not exceed the API's limits (if any) and is within the allowed range (1-365).

---

### **11. Reopening and Using the Application Again**

To use the Natural Disaster Tracker application in the future:

1. **Locate the File**:
   - Find `natural_disaster_tracker.html` on your computer (e.g., Desktop).

2. **Open the File**:
   - **Double-Click Method**:
     - Double-click the file to launch it in your web browser.
   - **Right-Click Method**:
     - Right-click on `natural_disaster_tracker.html`.
     - Select **Open With** and choose your preferred web browser.

3. **Interact as Needed**:
   - View recent natural disaster events by selecting different categories and date ranges.
   - Click **"Fetch Events"** to update the map with new data.

---

### **12. Understanding the Code Structure (Optional)**

While not required to run the application, understanding the basics can be helpful:

- **HTML**:
  - Structures the webpage elements like headers, controls, and the map container.

- **CSS**:
  - Styles the appearance of the webpage, including layout, colors, and responsiveness.

- **JavaScript**:
  - Handles the dynamic fetching of data from NASA's EONET API based on user interactions.
  - Utilizes **Leaflet** to render the interactive map and place markers for each event.

*Feel free to explore and modify the code to customize the application further!*


---

By following these steps, you can successfully run the **Agnirva Natural Disaster Tracker** on your computer. This application provides a real-time view of various natural disaster events worldwide, helping you stay informed and aware of significant environmental occurrences. Enjoy exploring and monitoring natural disasters with this interactive tool!