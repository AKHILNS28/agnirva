This code creates a website called "Agnirva Natural Disaster Tracker" that allows users to view and track recent natural disaster events on an interactive map. The page includes controls where users can select the type of disaster they're interested in (like wildfires, severe storms, or volcanoes) and specify how many past days they want to look back. Once the user makes their selections and clicks the "Fetch Events" button, the map updates to show markers indicating where these disasters have occurred. Clicking on a marker provides more details about the specific event.

Here's a breakdown of how the website works:

1. **Page Layout:**
   - **Header Section (`<head>`):** Sets up the page with necessary information like character encoding, title, and links to external stylesheets. It includes Leaflet's CSS for map styling and some custom CSS to style the page elements.
   - **Body Section (`<body>`):** Divided into two main parts:
     - **Controls Panel (`#controls`):** Located at the top, this area contains dropdown menus and input fields where users can select the type of natural disaster and the number of past days to view. There's also a "Fetch Events" button to initiate the search.
     - **Map Area (`#map`):** Occupies most of the page, displaying an interactive map where disaster events will be marked.

2. **Styling (`<style>`):**
   - **Basic Styles:** Sets the font to Arial, removes default margins and padding, and defines background colors.
   - **Controls Panel:** Styled with padding and a light gray background to distinguish it from the map area.
   - **Map Area:** Sized to take up 90% of the viewport height, ensuring it's prominently displayed.
   - **Control Groups:** Each group of controls (like selecting a category or number of days) has spacing to keep the layout clean.
   - **Labels:** Positioned with some margin to align neatly with their corresponding input fields.

3. **Interactive Map (Leaflet.js):**
   - **Initialization:** The map is centered at latitude 20 and longitude 0 with a zoom level of 2, providing a global view.
   - **Tile Layer:** Uses OpenStreetMap tiles to display the map, giving users a detailed and navigable map interface.

4. **Fetching and Displaying Disaster Events:**
   - **Fetching Data:**
     - When the user clicks the "Fetch Events" button, the website sends a request to NASA's EONET (Earth Observatory Natural Event Tracker) API.
     - The request includes parameters based on the user's selections: the category of disaster (like wildfires or volcanoes) and the number of past days to look back.
     - If a specific category is selected, the code maps the user-friendly category name to an internal category ID required by the API.
   - **Handling the Response:**
     - Upon receiving the data, the website processes each disaster event.
     - For each event, it checks the type of geographic data provided (like points or polygons) and places a marker on the map at the event's location.
     - Each marker includes a popup that displays the event's title, date, and a description if available.
   - **Clearing Previous Data:**
     - Before displaying new events, any existing markers from previous searches are removed to keep the map current and uncluttered.

5. **User Interaction:**
   - **Selecting Categories and Days:**
     - Users can choose from predefined disaster categories or leave it as "All" to view all types.
     - They can also specify how many past days they want to include, with a default of 30 days and a range from 1 to 365 days.
   - **Fetching Events:**
     - Clicking the "Fetch Events" button triggers the data retrieval and updates the map with the latest information.
     - If there's an issue fetching data (like network problems), the website alerts the user with an error message.
   - **Viewing Event Details:**
     - Clicking on any marker on the map opens a popup with more information about that specific disaster event.

6. **Technical Components:**
   - **Leaflet.js:** A JavaScript library used to create the interactive map, handle map tiles, and manage markers.
   - **NASA's EONET API:** Provides real-time data on various natural disaster events, which the website fetches and displays.
   - **JavaScript Functions:**
     - **`AgnirvafetchAndDisplayEvents`:** Handles fetching data from the API based on user input and calls functions to display the events.
     - **`AgnirvadisplayEventsOnMap`:** Processes the fetched events and places markers on the map.
     - **`AgnirvaaddMarker`:** Adds individual markers to the map with popups containing event details.
     - **Event Listeners:** Set up to respond to user actions, such as clicking the "Fetch Events" button.

7. **User Experience Enhancements:**
   - **Default Data Load:** When the page first loads, it automatically fetches and displays the latest 30 days of all disaster events, giving users immediate insight without needing to make a selection.
   - **Error Handling:** If there's a problem fetching data, users are notified with an alert, ensuring they understand that something went wrong.
   - **Clean Interface:** By clearing previous markers before displaying new ones, the map remains organized and easy to navigate.

**In Summary:**
The "Agnirva Natural Disaster Tracker" website leverages mapping technology and real-time data from NASA to provide users with an up-to-date view of natural disasters around the world. Its intuitive interface allows users to filter events by category and time frame, making it a valuable tool for monitoring and understanding global natural events. Whether you're interested in tracking wildfires, storms, or volcanic activity, this website offers a clear and interactive way to stay informed.
