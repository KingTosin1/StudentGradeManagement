# Student Grade Management System with GPA Calculator

## Project Overview

The Student Grade Management System with GPA Calculator is a Python desktop application designed to streamline the management of student records, courses, and grades in an academic setting. It provides a user-friendly interface for administrators to add, edit, and delete student information, manage courses with credit units, enter grades, and automatically calculate GPA (Grade Point Average) and CGPA (Cumulative Grade Point Average). The application uses the Nigerian university grading system and supports data persistence, visualization, and report generation.

## Features

- **Student Management**: Add, edit, delete, and view student records including ID, name, and email
- **Course Management**: Create and manage courses with unique codes, names, credit units, and semesters
- **Grade Entry and Validation**: Input grades for students per course per semester with built-in validation
- **Automatic GPA and CGPA Calculation**: Real-time calculation using the Nigerian grading scale
- **Data Persistence**: Automatic saving and loading of all data using CSV files
- **Data Visualization**: Interactive charts showing GPA trends and grade distributions
- **PDF Grade Report Generation**: Export detailed student reports as PDF documents
- **Simple Login System**: Basic authentication for admin access
- **User-Friendly Desktop GUI**: Modern interface built with CustomTkinter for intuitive navigation

## Technologies Used

- **Python 3.13+**: Core programming language for the application
- **Tkinter / CustomTkinter**: GUI framework for creating the desktop interface with modern styling
- **NumPy**: Numerical computations for GPA calculations
- **Pandas**: Data manipulation and CSV file handling
- **Matplotlib & Seaborn**: Data visualization libraries for creating charts and graphs
- **ReportLab**: PDF generation library for creating grade reports
- **Git & GitHub**: Version control and collaborative development platform

## GPA Calculation Method

The application uses the standard Nigerian university GPA calculation method. Grades are assigned point values as follows:

- A = 5 points
- B = 4 points
- C = 3 points
- D = 2 points
- E = 1 point
- F = 0 points

The GPA formula calculates a weighted average:

```
GPA = Σ(grade_point × credit_unit) / Σ(credit_units)
```

Where:

- `grade_point` is the point value for the grade received
- `credit_unit` is the number of credit units for the course
- The summation is performed over all courses in a semester

CGPA is calculated similarly but across all semesters for the student's entire academic record.

## Project Structure

```
StudentGradeSystem/
├── main.py                    # Main entry point and application launcher
├── requirements.txt           # Python dependencies list
├── assets/
│   └── icons/                 # Application icons and images
├── data/
│   ├── students.csv           # Student records storage
│   ├── courses.csv            # Course information storage
│   └── grades.csv             # Grade entries storage
├── src/
│   ├── student.py             # Student data model
│   ├── course.py              # Course data model
│   ├── grade.py               # Grade data model
│   ├── gpa_calculator.py      # GPA calculation logic
│   ├── storage.py             # Data persistence functions
│   ├── charts.py              # Chart generation functions
│   ├── pdf_report.py          # PDF report generation
│   ├── login_window.py        # Login interface
│   ├── dashboard_window.py    # Main dashboard
│   ├── student_management_window.py  # Student CRUD interface
│   ├── course_management_window.py   # Course CRUD interface
│   ├── grade_entry_window.py  # Grade entry interface
│   ├── gpa_display_window.py  # GPA display interface
│   ├── charts_window.py       # Charts display interface
│   └── pdf_export_dialog.py   # PDF export interface
├── docs/
│   └── user_manual.pdf        # User documentation
├── README.md                  # Project documentation
├── LICENSE                    # MIT License
└── report.pdf                 # Academic project report structure
```

## Installation & Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/StudentGradeManagementSystem.git
   cd StudentGradeManagementSystem
   ```

2. **Create and Activate Virtual Environment**

   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python main.py
   ```

## Usage Instructions

1. **Login**: Launch the application and log in with username "admin" and password "password"

2. **Dashboard Navigation**: Use the main dashboard to access different features:

   - Manage Students: Add, edit, or delete student records
   - Manage Courses: Create and modify course information
   - Enter Grades: Record grades for students in specific courses and semesters
   - View GPA/CGPA: Display calculated GPA and CGPA for selected students
   - View Charts: Visualize GPA trends and grade distributions
   - Export PDF: Generate and save PDF reports for students

3. **Adding Data**:

   - Students require unique ID, name, and email
   - Courses need unique code, name, credit units (1-6), and semester
   - Grades are entered per student, course, and semester

4. **Viewing Results**: Select a student to view their GPA breakdown by semester and overall CGPA

5. **Exporting Reports**: Choose a student and export their complete grade report as a PDF

## Screenshots / Demo

### Screenshots

- ![Login Screen](assets/screenshots/login.png)
- ![Dashboard](assets/screenshots/dashboard.png)
- ![Student Management](assets/screenshots/student_management.png)
- ![GPA Display](assets/screenshots/gpa_display.png)
- ![Charts](assets/screenshots/charts.png)

### Demo

A short demonstration video (20 seconds) showing the main features is available at: `assets/demo/demo.mp4`

## Contribution Guidelines

This project welcomes contributions from team members and the open-source community. To contribute:

1. Fork the repository on GitHub
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Submit a pull request for review

Please ensure all contributions follow the project's coding standards and include appropriate documentation. Use GitHub Issues for bug reports and feature requests.

## Academic Compliance

This project was developed as part of the ICT323 Software Development course at the university level. All code is original and developed by the project team. The implementation follows academic integrity guidelines, with proper citation of external libraries and resources. AI tools were used only for debugging assistance and learning support, not for code generation.

## Future Improvements

- **Web-Based Version**: Develop a web application using Flask or Django
- **Database Integration**: Replace CSV files with a relational database like SQLite or PostgreSQL
- **Mobile Application**: Create Android/iOS apps for mobile access
- **Advanced Analytics**: Add more detailed performance analytics and predictions
- **Multi-User Support**: Implement role-based access for different user types
- **Cloud Storage**: Enable data synchronization across devices

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
