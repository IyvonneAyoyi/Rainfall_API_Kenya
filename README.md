# Rainfall API Kenya

## What is This?

The **Rainfall API Kenya** is a web service that helps you track and access rainfall data for different locations across Kenya. Think of it as a digital weather assistant that remembers the locations you care about and gives you detailed rainfall information whenever you need it.

## What Does It Do?

### 🎯 Main Features

1. **Save Your Locations**
   - Add places you care about (home, farm, office, etc.)
   - Simply provide a location name or GPS coordinates
   - The system automatically finds the exact location details

2. **Get Rainfall Data**
   - Check how much rain fell in any location
   - See hourly and daily rainfall patterns
   - Access precipitation forecasts

3. **Keep Track of Everything**
   - All your activities are logged automatically
   - See who accessed what and when
   - Build a complete history of rainfall data requests

## How Does It Work?

### The Information Flow

```
You (User) → Create Account → Add Locations → Get Rainfall Data → View Results
```

### Data We Use

- **User Information**: Username, email, password (kept secure)
- **Location Data**: Place names, latitude/longitude coordinates
- **Rainfall Data**: Hourly rain amounts, daily totals, precipitation hours
- **Activity Logs**: Request timestamps, IP addresses, user actions

## Getting Started

### 1. Create an Account
```
POST /users/register/
Send: username, email, password
```

### 2. Get a Login Token
```
POST /api/token/
Send: username, password
Receive: Access token for authentication
```

### 3. Add a Location
```
POST /api/locations/
Provide either:
  - Location name (e.g., "Nairobi") → System finds coordinates
  - GPS coordinates → System finds location name
```

### 4. Check Rainfall Data
```
GET /api/rainfall/{location_id}/
Returns: Hourly rain, daily totals, precipitation hours
```

### 5. View Your Profile
```
GET /users/me/
Shows: Your username and email
```

## API Endpoints at a Glance

| Feature | Endpoint | What It Does |
|---------|----------|-------------|
| Register | `POST /users/register/` | Create a new account |
| Login | `POST /api/token/` | Get access token |
| Refresh Login | `POST /api/token/refresh/` | Extend your session |
| View Profile | `GET /users/me/` | See your account info |
| View Locations | `GET /api/locations/` | List all your saved places |
| Add Location | `POST /api/locations/` | Save a new place |
| Edit Location | `PUT /api/locations/{id}/` | Update location details |
| Delete Location | `DELETE /api/locations/{id}/` | Remove a saved place |
| Get Rainfall | `GET /api/rainfall/{location_id}/` | Check rain data for a place |
| View Logs | `GET /api/logs/` | See activity history (admin only) |
| Health Check | `GET /` | Check if system is running |

## Data Sources

- **Rainfall Data**: [Open-Meteo API](https://open-meteo.com/) - A free, global weather data service
- **Location Data**: [Nominatim](https://nominatim.openstreetmap.org/) - Converts addresses to coordinates and vice versa(reverse geocoding)

## Who Can Use This?

- Farmers monitoring their land's rainfall
- Weather researchers collecting data
- City planners analyzing rainfall patterns
- Anyone interested in weather tracking

## Security

- All passwords are encrypted and never stored in plain text
- Only authenticated users can see their own data
- Admin users can view activity logs
- Each action is timestamped and logged

## Technology Stack

- **Backend**: Django (Python web framework)
- **Database**: PostgreSQL
- **API Style**: REST (simple web requests)
- **Authentication**: JWT tokens (industry standard)

## Need Help?

- Ensure you're using the correct location format
- Login token expires after 30 minutes (refresh to extend)
- Check that all required fields are filled when adding locations
- Contact your system administrator for access issues

## Current Status

 **Live and Ready to Use** - All systems operational
