import requests
import folium
                                
def get_location(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"  # Using ip-api.com for demonstration
    response = requests.get(url)
    data = response.json()
    return data

def display_map(latitude, longitude):
    m = folium.Map(location=[latitude, longitude], zoom_start=10)
    folium.Marker([latitude, longitude], popup='Your Location').add_to(m)
    m.save('Task5_GeolocationTracker/location_map.html')
    print("Map generated. Check 'location_map.html'.")

if __name__ == "__main__":
    ip_address = input("Enter IP Address: ")  # Enter the IP address you want to track
    location_data = get_location(ip_address)

    if location_data['status'] == 'success':
        latitude = location_data['lat']
        longitude = location_data['lon']
        display_map(latitude, longitude)
    else:
        print("Failed to fetch location data.")
