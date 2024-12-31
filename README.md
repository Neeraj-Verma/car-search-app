
# Car Search App

This is a Python-based application that combines a **FastAPI** backend and a **Streamlit** frontend for searching and visualizing car data.

## Features

- Filter cars by:
  - **Length** (meters)
  - **Weight** (kg)
  - **Velocity** (km/h)
  - **Color**
- View results in a table on the frontend.
- Download search results or the complete dataset as **XML**.
- Swagger UI available for API testing.

---

## Getting Started

### Prerequisites

1. **Python 3.9+**:
   - Download and install Python from [python.org](https://www.python.org/downloads/).
2. **Git** (Optional):
   - Install Git for cloning the repository.

---

## Installation and Usage

### Step 1: Clone the Repository

If you haven't already, clone the repository:

```bash
git clone https://github.com/Neeraj-Verma/car-search-app.git
cd car-search-app
```

---

### Step 2: Set Up a Virtual Environment

1. Create and activate a virtual environment:
   - On Linux/Mac:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

### Step 3: Create and Populate the Database

Run the database creation script:

```bash
python create_db.py
```

This script creates an SQLite database (`cars.db`) and populates it with sample car data.

---

### Step 4: Start the Backend (FastAPI)

Run the FastAPI backend server:

```bash
uvicorn backend:app --reload
```

The backend will be accessible at:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- OpenAPI JSON: [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)

---

### Step 5: Start the Frontend (Streamlit)

Open a new terminal (keep the backend running) and start the Streamlit app:

```bash
streamlit run frontend.py
```

The frontend will be accessible at:

- [http://127.0.0.1:8501](http://127.0.0.1:8501)

---

## How to Use

### Search for Cars
1. Open the **Streamlit frontend** at [http://127.0.0.1:8501](http://127.0.0.1:8501).
2. Use the sidebar to filter cars by:
   - Length
   - Weight
   - Velocity
   - Color
3. View the results in a table.
4. Download the search results or all cars as **XML** using the provided buttons.

---

### Test the API
Use the **Swagger UI** to test API endpoints:

- **Search Cars**: `/search_cars`
- **View All Cars**: `/all_cars`

Access the Swagger UI at:
- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Example Output

### Search Results (Table in Streamlit)
| ID  | Length | Weight | Velocity | Color  |
|-----|--------|--------|----------|--------|
| 1   | 4.5    | 1200   | 150      | red    |

### Search Results (XML)
```xml
<cars>
    <car>
        <id>1</id>
        <length>4.5</length>
        <weight>1200</weight>
        <velocity>150</velocity>
        <color>red</color>
    </car>
</cars>
```

---

## Acknowledgments

- Built using [FastAPI](https://fastapi.tiangolo.com/) and [Streamlit](https://streamlit.io/).
- Designed by [Neeraj Verma](https://github.com/Neeraj-Verma).
