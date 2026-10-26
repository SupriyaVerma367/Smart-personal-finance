# Smart Personal Finance Management System

A full-stack personal finance management application designed to help users track income and expenses, monitor their balance, and gain better visibility into their financial activities.

**Project Status:** In Progress

## Overview

Managing personal finances requires tracking transactions, understanding spending patterns, and monitoring available balances. The Smart Personal Finance Management System aims to simplify these activities through a mobile application backed by a Django REST API.

The project combines a Flutter-based mobile frontend with a Django backend to support transaction management and financial summaries. Further integration and feature development are ongoing.

## Key Features

- **User Authentication:** Login functionality connected to the backend authentication API.
- **Transaction Management:** Backend APIs for managing income and expense transactions.
- **Financial Summary:** API support for calculating total income, expenses, and balance.
- **Mobile Dashboard:** Flutter interface displaying a financial overview and recent transactions.
- **Transaction Categories:** Organizing financial activities by categories.
- **Scalable Architecture:** Separate frontend and backend components for easier development and maintenance.

*Note: Some features are still under development. The dashboard currently contains sample financial figures, and complete frontend-backend integration is in progress.*

## Technology Stack

| Component | Technologies |
|---|---|
| Mobile Frontend | Flutter, Dart |
| Backend | Python, Django, Django REST Framework |
| Database | SQLite during development |
| API Communication | REST APIs, JSON, HTTP |
| Version Control | Git, GitHub |

## Project Architecture

The application follows a frontend-backend architecture.

1. **Flutter Frontend:** Provides the mobile user interface for authentication and financial information.
2. **Django Backend:** Handles API requests, authentication, transaction data, and financial summaries.
3. **Database:** Stores application data through Django's database layer.
4. **REST API Communication:** Allows the frontend to communicate with the backend through HTTP requests and JSON responses.

## Backend Implementation

The backend development includes:

- Transaction data modelling.
- Serializers for converting transaction data to and from JSON.
- API views and endpoints for transaction operations.
- Authentication and permission checks.
- User-specific transaction filtering.
- Transaction summary calculations.
- API testing using HTTP requests.

## Repository Structure

```text
Smart-personal-finance/
├── backend/       # Django backend and REST APIs
├── frontend/      # Flutter mobile application
├── ml/            # Machine learning components
├── docs/          # Project documentation
└── README.md
```

The machine learning component is part of the project structure; its current implementation status should be verified separately.

## Getting Started

### Prerequisites

- Python and pip
- Flutter SDK and Dart
- Android Studio or another configured Flutter development environment
- Git

### 1. Clone the repository

```bash
git clone https://github.com/SupriyaVerma367/Smart-personal-finance.git
cd Smart-personal-finance
```

### 2. Set up the Django backend

Navigate to the backend directory and activate your Python virtual environment.

```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

If the backend dependency file is located elsewhere, use the corresponding path. Configure any required environment variables before running the application.

### 3. Set up the Flutter frontend

Open a separate terminal and navigate to the frontend directory.

```bash
cd frontend
flutter pub get
flutter run
```

Ensure the frontend API base URL points to the correct backend address for your emulator or physical device. The local development URL may need to be changed from `127.0.0.1` depending on the device.


## Current Limitations and Future Improvements

- Complete integration of Flutter screens with backend APIs.
- Replace sample dashboard figures with live API data.
- Implement functional navigation for transactions, insights, and profile screens.
- Improve token persistence and authenticated API requests.
- Add transaction creation, editing, and deletion through the mobile interface.
- Add spending charts and financial insights.
- Expand automated tests and improve error handling.

## Project Repository

GitHub: https://github.com/SupriyaVerma367/Smart-personal-finance

## Acknowledgements

Developed collaboratively as an ongoing academic software project, with contributions across backend and mobile frontend development.
