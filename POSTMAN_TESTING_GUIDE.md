# Testing Rainfall API Kenya in Postman

## What is Postman?

Postman is a tool that lets you test APIs without writing code. Think of it as a "conversation starter" with your API - you send requests and see the responses.

## Step 1: Install Postman

1. Download from: [https://www.postman.com/downloads/](https://www.postman.com/downloads/)
2. Install and open it
3. Create a free account (optional but helpful)

## Step 2: Create a New Collection

A Collection is like a folder that holds all your API tests.

1. Click **"Collections"** on the left sidebar
2. Click **"+ New Collection"**
3. Name it: `Rainfall API Kenya`
4. Click **Create**

## Step 3: Set Up Base URL (Environment Variable)

This saves you from typing the full address each time.

1. Click **Environments** (left sidebar)
2. Click **+ Create New Environment**
3. Name it: `Rainfall API Local`
4. Add this variable:
   - **Variable Name**: `base_url`
   - **Initial Value**: `http://127.0.0.1:8000`
   - **Current Value**: `http://127.0.0.1:8000`
5. Click **Save**
6. Select this environment from the dropdown (top right)

## Step 4: Test All Endpoints

### TEST 1: Health Check (No Authentication Needed)

**What it does**: Checks if the API is running

1. Click **"+" tab** to create a new request
2. Fill in the details:
   - **Method**: `GET`
   - **URL**: `{{base_url}}/`
   - **Name**: `Health Check`

3. Click **Send**
4. You should see:
   ```json
   {
     "status": "ok",
     "message": "Rainfall API is running"
   }
   ```

**If you see this, your API is working!**

---

### TEST 2: Register a New User

**What it does**: Creates a new account

1. Create a new request in your collection
2. Fill in:
   - **Method**: `POST`
   - **URL**: `{{base_url}}/users/register/`
   - **Name**: `Register User`

3. Go to **Body** tab → Select **raw** → Choose **JSON**
4. Paste this (change the values):
   ```json
   {
     "username": "testuserA123",
     "email": "testuserA@example.com",
     "password": "Pass123!@#"
   }
   ```

5. Click **Send**
6. You should see:
   ```json
   {
     "username": "testuserA123",
     "email": "testuserA@example.com"
   }
   ```

**User created successfully!**

---

### TEST 3: Get Login Token (Authentication)

**What it does**: Gives you a token to access protected endpoints

1. Create a new request
2. Fill in:
   - **Method**: `POST`
   - **URL**: `{{base_url}}/api/token/`
   - **Name**: `Get Token`

3. Go to **Body** tab → Select **raw** → Choose **JSON**
4. Paste this (use your username and password from TEST 2):
   ```json
   {
     "username": "testuserA123",
     "password": "Pass123!@#"
   }
   ```

5. Click **Send**
6. You'll get a response like:
   ```json
   {
     "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
   }
   ```

7. **SAVE THE ACCESS TOKEN** - Copy the `access` value (you'll need this!)

**Token obtained!**

---

### TEST 4: View Your Profile

**What it does**: Shows your account information

1. Create a new request
2. Fill in:
   - **Method**: `GET`
   - **URL**: `{{base_url}}/users/me/`
   - **Name**: `View Profile`

3. Go to **Headers** tab
4. Add a new header:
   - **Key**: `Authorization`
   - **Value**: `Bearer YOUR_ACCESS_TOKEN` (paste your token from TEST 3)

5. Click **Send**
6. You should see:
   ```json
   {
     "username": "testuserA123",
     "email": "testuserA@example.com"
   }
   ```

**Authentication works!**

---

### TEST 5: Add a Location (by Name)

**What it does**: Saves a location using its name

1. Create a new request
2. Fill in:
   - **Method**: `POST`
   - **URL**: `{{base_url}}/api/locations/`
   - **Name**: `Add Location by Name`

3. Go to **Headers** tab
4. Add authorization header (same as TEST 4):
   - **Key**: `Authorization`
   - **Value**: `Bearer YOUR_ACCESS_TOKEN`

5. Go to **Body** tab → **raw** → **JSON**
6. Paste this:
   ```json
   {
     "name": "Nairobi"
   }
   ```

7. Click **Send**
8. You'll get:
   ```json
   {
     "id": 1,
     "name": "Nairobi",
     "latitude": -1.2865,
     "longitude": 36.8172,
     "created_at": "2025-12-20T23:45:00Z"
   }
   ```

**Location saved! Note the ID (you'll need it next)**

---

### TEST 6: Add a Location (by Coordinates)

**What it does**: Saves a location using GPS coordinates

1. Create a new request
2. Fill in:
   - **Method**: `POST`
   - **URL**: `{{base_url}}/api/locations/`
   - **Name**: `Add Location by Coordinates`

3. Add authorization header (from TEST 4)
4. Go to **Body** → **raw** → **JSON**
5. Paste this:
   ```json
   {
     "latitude": "-0.3531",
     "longitude": "36.0800"
   }
   ```

6. Click **Send**
7. The system will find the location name automatically!

**Location created from coordinates!**

---

### TEST 7: View All Your Locations

**What it does**: Lists all locations you've saved

1. Create a new request
2. Fill in:
   - **Method**: `GET`
   - **URL**: `{{base_url}}/api/locations/`
   - **Name**: `View All Locations`

3. Add authorization header
4. Click **Send**
5. You'll see all your saved locations:
   ```json
   [
     {
       "id": 1,
       "name": "Nairobi",
       "latitude": -1.2865,
       "longitude": 36.8172,
       "created_at": "2025-12-20T23:45:00Z"
     }
   ]
   ```

**All locations displayed!**

---

### TEST 8: Get Rainfall Data

**What it does**: Shows rainfall information for a location

1. Create a new request
2. Fill in:
   - **Method**: `GET`
   - **URL**: `{{base_url}}/api/rainfall/1/` (replace 1 with your location ID from TEST 5)
   - **Name**: `Get Rainfall Data`

3. Add authorization header
4. Click **Send**
5. You'll get rainfall information:
   ```json
   {
     "id": 1,
     "user": 1,
     "location": 1,
     "daily_rain_sum": [0.0, 0.2, 0.1, ...],
     "precipitation_hours": [0, 1, 2, ...],
     "hourly_rain": [0.0, 0.05, 0.0, ...],
     "created_at": "2025-12-20T23:50:00Z"
   }
   ```

**Rainfall data retrieved!**

---

### TEST 9: Update a Location

**What it does**: Changes location details

1. Create a new request
2. Fill in:
   - **Method**: `PUT`
   - **URL**: `{{base_url}}/api/locations/1/` (replace 1 with your location ID)
   - **Name**: `Update Location`

3. Add authorization header
4. Go to **Body** → **raw** → **JSON**
5. Paste this:
   ```json
   {
     "name": "Nairobi Central"
   }
   ```

6. Click **Send**

**Location updated!**

---

### TEST 10: Delete a Location

**What it does**: Removes a saved location

1. Create a new request
2. Fill in:
   - **Method**: `DELETE`
   - **URL**: `{{base_url}}/api/locations/1/` (replace 1 with your location ID)
   - **Name**: `Delete Location`

3. Add authorization header
4. Click **Send**
5. You should get status 204 (successful deletion)

**Location deleted!**

---

### TEST 11: View API Logs (Admin Only)

**What it does**: Shows all API activity (requires admin account)

1. Create a new request
2. Fill in:
   - **Method**: `GET`
   - **URL**: `{{base_url}}/api/logs/`
   - **Name**: `View API Logs`

3. Add authorization header
4. Click **Send**
5. If you're an admin, you'll see all logged requests

**Note**: Only admin users can access this endpoint

---

## Quick Testing Flow

Follow this order for a complete test:

1. Health Check (TEST 1)
2. Register User (TEST 2)
3. Get Token (TEST 3)
4. View Profile (TEST 4)
5. Add Location (TEST 5)
6. View Locations (TEST 7)
7. Get Rainfall (TEST 8)
8. Update Location (TEST 9)
9. Delete Location (TEST 10)

## Common Issues & Solutions

### "401 Unauthorized"
- **Problem**: Missing or invalid token
- **Solution**: Make sure you added the Authorization header with your token

### "404 Not Found"
- **Problem**: Wrong URL or location ID doesn't exist
- **Solution**: Check the URL spelling and make sure you're using the correct location ID

### "400 Bad Request"
- **Problem**: Missing required fields or wrong data format
- **Solution**: Check your JSON body - make sure all required fields are included

### "Cannot connect to server"
- **Problem**: API isn't running
- **Solution**: Start the server with `.\env\Scripts\python.exe .\manage.py runserver`

## Pro Tips

**Save Your Token**: Create a Postman Environment variable to store your token
- Click **Environments** → **Rainfall API Local**
- Add: `token` = `your_access_token`
- Use in headers: `Bearer {{token}}`

**Use Pre-request Scripts**: Automatically get a new token before each request
- Click on request → **Pre-request Script** tab
- Add script to fetch fresh token

**Collection Variables**: Store user IDs and location IDs for easy reference

## Checklist

- Postman installed
- Collection created
- Environment set up
- All 11 tests completed
- API working perfectly!

---

