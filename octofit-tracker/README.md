# OctoFit Tracker

A fitness tracking application for students to log activities, form teams, and compete on leaderboards.

## Features
- User authentication and profiles
- Activity logging and tracking
- Team creation and management
- Competitive leaderboard
- Personalized workout suggestions

## Tech Stack
- **Backend**: Django REST Framework with MongoDB (Djongo)
- **Frontend**: React.js with Bootstrap
- **Database**: MongoDB

## Setup

### Prerequisites
- Python 3.8+
- Node.js 14+
- MongoDB

### Backend Setup
1. Navigate to `octofit-tracker/backend/`
2. Create virtual environment: `python3 -m venv venv`
3. Activate: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Run migrations: `python manage.py migrate`
6. Start server: `python manage.py runserver`

### Frontend Setup
1. Navigate to `octofit-tracker/frontend/`
2. Install dependencies: `npm install`
3. Start development server: `npm start`

### Database
Ensure MongoDB is running on localhost:27017.

## API Endpoints
- `/api/activities/` - Activity logging
- `/api/teams/` - Team management
- `/api/team-members/` - Team membership
- `/api/workout-suggestions/` - Workout suggestions

## Development
- Backend runs on http://localhost:8000
- Frontend runs on http://localhost:3000