<div align="center">

# 🏨 Hotel Management System

![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
![Express.js](https://img.shields.io/badge/Express.js-000000?style=for-the-badge&logo=express&logoColor=white)
![React](https://img.shields.io/badge/React-17.0.2-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-Auth-black?style=for-the-badge&logo=jsonwebtokens&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-Tests-43B02A?style=for-the-badge&logo=selenium&logoColor=white)

**A full-stack hotel management system with 6 integrated modules — room booking, customer portal, employee & payroll management, inventory tracking, and supplier management. Built with the MERN stack.**

[Features](#-features) · [Architecture](#-architecture) · [Tech Stack](#-tech-stack) · [Getting Started](#-getting-started) · [API Reference](#-api-reference) · [Screenshots](#-screenshots)

</div>

---

## 📋 Table of Contents

- [Features](#-features)
- [Screenshots](#-screenshots)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Environment Variables](#-environment-variables)
- [API Reference](#-api-reference)
- [Project Structure](#-project-structure)
- [Testing](#-testing)
- [Security](#-security)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🚀 Features

### Customer Portal
| Feature | Description |
|---------|-------------|
| **User Registration** | Customer sign-up with name, email, phone, and password |
| **Authentication** | Login system with email/password verification |
| **Room Browsing** | Browse available rooms by type, capacity, and pricing |
| **Room Booking** | Book rooms with guest details, check-in/out dates |
| **Room Filtering** | Filter rooms by type (Single, Double, Superior), capacity, and price range |

### Admin Dashboard
| Module | Features |
|--------|----------|
| **Room Management** | Add, view, update, and delete room listings with type, capacity, and pricing |
| **Employee Management** | Complete employee CRUD with department, designation, and contact details |
| **Payroll System** | Record and track salary payments with employee linkage |
| **Inventory Management** | Track hotel inventory items with quantity, restock alerts, and history |
| **Supplier Management** | Manage suppliers with contact info and full purchase history tracking |
| **Booking Management** | View and manage all room bookings with guest information |

### Technical Highlights
- **JWT-based admin authentication** with bcrypt password hashing
- **RESTful API** design with modular Express route groups
- **PDF report generation** using jsPDF with auto-table support
- **Responsive UI** with Bootstrap 5 and styled-components
- **Selenium test suite** with automated login flow testing

---

## 📸 Screenshots

<div align="center">

| Customer Portal | Room Browsing |
|:-:|:-:|
| ![Customer Portal](image.png) | ![Room Browsing](image-1.png) |

| Admin Dashboard | Management Panel |
|:-:|:-:|
| ![Admin Dashboard](image-2.png) | ![Management](image-3.png) |

</div>

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        CLIENT (React)                        │
│                      localhost:3000                           │
│                                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │ Customer  │  │  Room    │  │ Employee │  │ Inventory│    │
│  │ Portal    │  │ Booking  │  │ Manager  │  │ Manager  │    │
│  └─────┬────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘    │
│        │            │              │              │           │
│  ┌─────┴────┐  ┌────┴─────┐  ┌────┴─────┐  ┌────┴─────┐    │
│  │ Supplier │  │  Admin   │  │Dashboard │  │  Auth    │    │
│  │ Manager  │  │  Login   │  │          │  │  System  │    │
│  └─────┬────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘    │
├────────┴────────────┴──────────────┴──────────────┴──────────┤
│                      Axios HTTP Client                        │
│                    (REST API Requests)                        │
└──────────────────────────┬───────────────────────────────────┘
                           │ HTTP (JSON)
┌──────────────────────────▼───────────────────────────────────┐
│                     SERVER (Express.js)                        │
│                      localhost:5000                            │
│                                                               │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │                    Middleware Layer                       │  │
│  │  CORS │ cookie-parser │ express.json │ JWT Verify       │  │
│  └─────────────────────────┬───────────────────────────────┘  │
│                             │                                  │
│  ┌──────────┬──────────┬───┴──────┬──────────┬──────────┐    │
│  │/customer │/booking  │/room     │/employees│/inventory│    │
│  │/supplier │/adminlog │/supplier │/paidsalar│          │    │
│  │          │          │ history  │ ies      │          │    │
│  └──────────┴──────────┴──────────┴──────────┴──────────┘    │
│                             │                                  │
│  ┌──────────────────────────▼──────────────────────────────┐  │
│  │              Mongoose ODM (Schema + Models)              │  │
│  └──────────────────────────┬──────────────────────────────┘  │
└─────────────────────────────┼────────────────────────────────┘
                              │ MongoDB Driver
┌─────────────────────────────▼────────────────────────────────┐
│                    MongoDB Atlas (Cloud)                       │
│                                                               │
│  Collections:                                                 │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐        │
│  │customers │ │rooms     │ │bookings  │ │employees │        │
│  │adminlogin│ │inventory │ │suppliers │ │paidsalar │        │
│  │          │ │          │ │supplier  │ │ ies      │        │
│  │          │ │          │ │ history  │ │          │        │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘        │
└──────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

### Backend

| Technology | Version | Role |
|-----------|---------|------|
| **Node.js** | ≥ 14 | JavaScript runtime |
| **Express.js** | 4.17 | Web framework & REST API routing |
| **Mongoose** | 8.19 | MongoDB ODM with schema validation |
| **MongoDB Atlas** | — | Cloud-hosted NoSQL database |
| **JWT** | 9.0 | JSON Web Token authentication |
| **bcrypt.js** | 2.4 | Password hashing (salted) |
| **cookie-parser** | 1.4 | HTTP cookie handling |
| **CORS** | 2.8 | Cross-Origin Resource Sharing |
| **dotenv** | 10.0 | Environment variable management |
| **nodemon** | 2.0 | Hot-reload development server |
| **concurrently** | 6.2 | Run backend + frontend simultaneously |

### Frontend

| Technology | Version | Role |
|-----------|---------|------|
| **React** | 17.0.2 | UI component framework |
| **React Router DOM** | 5.2 | Client-side routing (Switch/Route) |
| **Axios** | 0.21 | HTTP client for API communication |
| **Bootstrap** | 5.1 | Responsive CSS framework |
| **Bootstrap Icons** | 1.5 | Icon library |
| **styled-components** | 5.3 | CSS-in-JS component styling |
| **jsPDF + AutoTable** | 2.3 / 3.5 | PDF report generation and export |
| **React Icons** | 4.3 | Icon components (FontAwesome, etc.) |
| **validator** | 13.6 | Input validation (email, phone) |
| **SoloAlert** | 1.1 | Custom alert/notification popups |

### Testing

| Technology | Role |
|-----------|------|
| **Selenium WebDriver** | Browser automation for E2E tests |
| **pytest** | Python test runner with fixtures |
| **Chrome DevTools** | Screenshot capture on test pass/fail |

---

## 📦 Getting Started

### Prerequisites

- **Node.js** ≥ 14 and **npm** ≥ 6
- **MongoDB Atlas** account (free tier works) or local MongoDB instance
- **Python 3.8+** (only for Selenium tests)

### Installation

```bash
# Clone the repository
git clone https://github.com/cazy8/Hotel-Management-System-Mern-Stack.git
cd Hotel-Management-System-Mern-Stack
```

### Backend Setup

```bash
cd backend
npm install

# Create environment file (see Environment Variables section)
cp .env.example .env
# Edit .env with your MongoDB URI and JWT secret

# Start backend server (with hot-reload)
npm run dev
```

> Backend runs on **http://localhost:5000**

### Frontend Setup

```bash
cd frontend
npm install

# Start React development server
npm start
```

> Frontend runs on **http://localhost:3000**

### Run Both Simultaneously

```bash
# From the backend directory
npm run dev
# This uses concurrently to launch both servers
```

---

## 🔐 Environment Variables

Create a `backend/.env` file using the provided template:

```bash
cp backend/.env.example backend/.env
```

| Variable | Description | Example |
|----------|-------------|---------|
| `MONGO_CONNECT` | MongoDB Atlas connection string | `mongodb+srv://<user>:<pass>@cluster.mongodb.net/Hotel_DB` |
| `JWT_SECRET` | Secret key for signing JWT tokens | Any random 64+ character string |
| `PORT` | Backend server port (optional) | `5000` |

### Generate a Secure JWT Secret

```bash
node -e "console.log(require('crypto').randomBytes(64).toString('hex'))"
```

> ⚠️ **Never commit `.env` files to version control.** The `.gitignore` is configured to exclude them.

---

## 📡 API Reference

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/adminlogin/add` | Register new admin |
| `GET` | `/adminlogin/retrieve` | Get all admin records |
| `POST` | `/adminlogin/login` | Admin login |

### Customer Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/customer/register` | Customer registration |
| `POST` | `/customer/login` | Customer login |

### Room Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/room/add` | Add new room |
| `GET` | `/room/` | Get all rooms |
| `GET` | `/room/:id` | Get room by ID |
| `PUT` | `/room/update/:id` | Update room details |
| `DELETE` | `/room/delete/:id` | Delete room |

### Room Booking

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/booking/add` | Create new booking |
| `GET` | `/booking/` | Get all bookings |
| `GET` | `/booking/:id` | Get booking by ID |
| `DELETE` | `/booking/delete/:id` | Cancel booking |

### Employee Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/employees/add` | Add employee |
| `GET` | `/employees/` | Get all employees |
| `GET` | `/employees/:id` | Get employee by ID |
| `PUT` | `/employees/update/:id` | Update employee |
| `DELETE` | `/employees/delete/:id` | Delete employee |

### Payroll

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/paidsalaries/add` | Record salary payment |
| `GET` | `/paidsalaries/` | Get all salary records |

### Inventory Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/inventory/add` | Add inventory item |
| `GET` | `/inventory/` | Get all inventory |
| `GET` | `/inventory/:id` | Get item by ID |
| `PUT` | `/inventory/update/:id` | Update item |
| `DELETE` | `/inventory/delete/:id` | Delete item |

### Supplier Management

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/supplier/add` | Add supplier |
| `GET` | `/supplier/` | Get all suppliers |
| `GET` | `/supplier/:id` | Get supplier by ID |
| `PUT` | `/supplier/update/:id` | Update supplier |
| `DELETE` | `/supplier/delete/:id` | Delete supplier |
| `POST` | `/supplierhistory/add` | Add supplier history record |
| `GET` | `/supplierhistory/` | Get all history records |

---

## 📁 Project Structure

```
Hotel-Management-System-Mern-Stack/
│
├── backend/                          # Express.js API Server
│   ├── server.js                     # Entry point — Express app, MongoDB connection, route mounting
│   ├── package.json                  # Backend dependencies and scripts
│   ├── .env.example                  # Environment variable template
│   │
│   ├── models/                       # Mongoose schemas & models
│   │   ├── adminlogin.js             # Admin user schema (username, password, role)
│   │   ├── rooms.js                  # Room model
│   │   ├── customer/
│   │   │   └── customerModel.js      # Customer schema (name, email, phone, password)
│   │   ├── room-booking/
│   │   │   └── bookingModel.js       # Booking schema (guest info, room type, dates)
│   │   ├── emp-manager/
│   │   │   ├── employees.js          # Employee schema (name, dept, designation, salary)
│   │   │   └── paidsalaries.js       # Salary payment records
│   │   ├── employee-manager/
│   │   │   └── roomModel.js          # Room schema (type, capacity, price, description)
│   │   ├── inventory-manager/
│   │   │   └── inventoryModel.js     # Inventory schema (item, quantity, restock level)
│   │   └── supplier-manager/
│   │       ├── suppliermodel.js      # Supplier schema (name, contact, items supplied)
│   │       └── supplierhistorymodel.js # Supplier transaction history
│   │
│   └── routes/                       # Express route handlers
│       ├── adminlogin.js             # Admin auth routes (register, login, retrieve)
│       ├── rooms.js                  # Room routes
│       ├── customer/
│       │   └── customerRoute.js      # Customer registration & login
│       ├── room-booking/
│       │   └── bookingRoute.js       # Booking CRUD
│       ├── emp-manager/
│       │   ├── employees.js          # Employee CRUD
│       │   └── paidsalaries.js       # Salary records
│       ├── employee-manager/
│       │   └── RoomRoute.js          # Room CRUD
│       ├── inventory-manager/
│       │   └── inventoryRoute.js     # Inventory CRUD
│       └── supplier-manager/
│           ├── supplierRoute.js      # Supplier CRUD
│           └── supplierhistoryRoute.js # Supplier history
│
├── frontend/                         # React Application
│   ├── package.json                  # Frontend dependencies and scripts
│   ├── public/
│   │   ├── index.html                # HTML entry point
│   │   ├── favicon.ico               # Browser tab icon
│   │   ├── cover.jpeg               # Hotel cover image
│   │   └── logo.png                  # Hotel logo
│   │
│   └── src/
│       ├── App.js                    # Root component — React Router configuration
│       ├── index.js                  # ReactDOM entry point
│       ├── App.css                   # Global styles
│       ├── context.js                # React Context for room data
│       ├── data.js                   # Static room data
│       ├── Contentful.js             # Contentful CMS integration
│       │
│       ├── components/
│       │   ├── auth/                 # Authentication
│       │   │   ├── cusLogin.js       # Customer login form
│       │   │   ├── CusRegister.js    # Customer registration form
│       │   │   └── adminRegister.js  # Admin registration
│       │   │
│       │   ├── room/                 # Room Management (Admin)
│       │   │   ├── AddRoom.js        # Add new room form
│       │   │   ├── ViewAllRooms.js   # Room listing table
│       │   │   ├── ViewOneRoom.js    # Single room details + edit
│       │   │   ├── RoomBookings.js   # Create booking form
│       │   │   └── ViewAllRoomBookings.js # All bookings list
│       │   │
│       │   ├── employee/             # Employee Management
│       │   │   ├── AddEmployee.js    # Add employee form
│       │   │   ├── ViewEmployee.js   # Employee listing
│       │   │   ├── ViewOneEmployee.js # Employee details + edit
│       │   │   ├── AddPaidSalary.js  # Record salary payment
│       │   │   └── ViewPaidSalary.js # Salary payment history
│       │   │
│       │   ├── inventory/            # Inventory Management
│       │   │   ├── AddInventory.js   # Add inventory item
│       │   │   ├── ViewAllInventory.js # Inventory listing
│       │   │   ├── ViewOneInventory.js # Item details + edit
│       │   │   └── RestockInventory.js # Restock existing items
│       │   │
│       │   ├── supplier/             # Supplier Management
│       │   │   ├── AddSupplier.js    # Add supplier form
│       │   │   ├── ViewAllSuppliers.js # Supplier listing
│       │   │   ├── ViewOneSupplier.js # Supplier details + edit
│       │   │   ├── ViewAllSupplierHistoryRecords.js # Purchase history
│       │   │   └── ViewOneSupplierHistoryRecords.js # Single record
│       │   │
│       │   ├── layouts/              # Shared Layout Components
│       │   │   ├── topnav.js         # Top navigation bar
│       │   │   ├── Navbar.js         # Customer navigation
│       │   │   ├── EMPsidenav.js     # Employee section sidebar
│       │   │   ├── EmpDetailsSideNav.js # Employee details sidebar
│       │   │   ├── Roomsidenav.js    # Room management sidebar
│       │   │   ├── InventorySideNav.js # Inventory sidebar
│       │   │   └── Supsidenav.js     # Supplier sidebar
│       │   │
│       │   ├── Dashboard.js          # Admin dashboard overview
│       │   ├── Banner.js             # Hero banner component
│       │   ├── FeaturedRooms.js      # Featured rooms carousel
│       │   ├── Hero.js               # Hero section
│       │   ├── Navbar.js             # Main navigation
│       │   ├── Room.js               # Room card component
│       │   ├── RoomsContainer.js     # Room list container
│       │   ├── RoomsFilter.js        # Room filtering controls
│       │   ├── RoomsList.js          # Room grid layout
│       │   ├── Services.js           # Hotel services section
│       │   ├── StyledHero.js         # Styled hero with background
│       │   ├── Title.js              # Section title component
│       │   └── Loading.js            # Loading spinner
│       │
│       ├── pages/                    # Page-level components
│       │   ├── Home.js               # Landing page
│       │   ├── Rooms.js              # All rooms page
│       │   ├── SingleRoom.js         # Individual room page
│       │   └── Error.js              # 404 error page
│       │
│       └── images/                   # Static assets (room images, logos, GIFs)
│
├── frontend/tests/                   # E2E Test Suite
│   └── selenium/python/
│       ├── conftest.py               # pytest fixtures (driver, test user creation)
│       ├── pytest.ini                # pytest configuration
│       ├── requirements.txt          # Test dependencies (selenium, pytest)
│       ├── test_cases.md             # Test case documentation
│       └── tests/
│           └── test_login.py         # Login flow tests (valid + invalid)
│
├── image.png                         # Screenshot — Customer portal
├── image-1.png                       # Screenshot — Room browsing
├── image-2.png                       # Screenshot — Admin dashboard
├── image-3.png                       # Screenshot — Management panel
├── .gitignore                        # Git ignore rules
├── LICENSE                           # MIT License
└── README.md                         # This file
```

---

## 🧪 Testing

### Selenium E2E Tests

The project includes automated browser tests for the login workflow:

```bash
cd frontend/tests/selenium/python

# Install test dependencies
pip install -r requirements.txt

# Run tests (both servers must be running)
pytest tests/ -v

# Run in headless mode
HEADLESS=1 pytest tests/ -v
```

| Test Case | Description | Expected Result |
|-----------|-------------|-----------------|
| TC-001 | Login with valid credentials | Redirects to `/rooms` or `/dashboard` |
| TC-002 | Login with invalid password | Alert shown, stays on login page |

### Environment Variables for Tests

| Variable | Default | Description |
|----------|---------|-------------|
| `BASE_URL` | `http://localhost:3000` | Frontend URL |
| `BACKEND_URL` | `http://localhost:5000` | Backend API URL |
| `HEADLESS` | `0` | Set to `1` for headless Chrome |
| `SCREENSHOT_DIR` | `./screenshots` | Screenshot output directory |

---

## 🔒 Security

This project follows security best practices:

- ✅ **Environment Variables** — All secrets (MongoDB URI, JWT key) stored in `.env`, never in source code
- ✅ **`.gitignore` configured** — `.env` files excluded from version control
- ✅ **bcrypt password hashing** — User passwords hashed with salt before storage
- ✅ **JWT authentication** — Stateless token-based auth for admin routes
- ✅ **CORS restricted** — Only `localhost:3000` allowed in development
- ✅ **Clean git history** — No credentials in commit history

### Production Recommendations

| Area | Recommendation |
|------|---------------|
| **Database** | Create restricted Atlas user (not admin), whitelist specific IPs |
| **JWT** | Use RS256 algorithm with key rotation |
| **HTTPS** | Enable TLS for all traffic in production |
| **Rate Limiting** | Add `express-rate-limit` middleware |
| **Input Validation** | Add server-side validation with `express-validator` |
| **Helmet** | Add `helmet` middleware for security headers |

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 👤 Author

**Harsh Gupta** — [@cazy8](https://github.com/cazy8) · [LinkedIn](https://www.linkedin.com/in/h4rshg/)

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**If you found this useful, consider giving it a ⭐**

</div>
