Prerequisites
  Python 3.x
  Flask (install with pip install Flask)

  
Getting Started
1. Clone the Repository
bash
Copy code
git clone https://github.com/yourusername/flask-routing-mini-project.git
cd flask-routing-mini-project


2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


3. Install Dependencies
pip install Flask


4. Run the application
   python app.py
   Access the application at http://localhost:5000.


5. Project Structure

flask-routing-mini-project/
│
├── templates/
│   ├── calculate.html
│   └── index.html
│   └── result.html
│
├── app.py
├── README.md
├── requirements.txt


6. Application Routes
/: Home page (GET)
/index: Index page (GET)
/success/<int:score>: Success page (GET)
/fail/<int:score>: Fail page (GET)
/calculate: Calculate page (GET, POST)


7. Templates
index.html: Template for the index page.
calculate.html: Form to input marks.
result.html: Displays the result.
