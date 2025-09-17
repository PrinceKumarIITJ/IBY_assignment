# Multi Agent Researcher : Designing systems where agents think, act, and evolve together.

## 🚀 Workflow

The project follows a modular workflow:

1. **Environment Setup**  
   - Clone the repository.  
   - Install all required dependencies.  
   - Configure environment variables from the `.env.example` file.  

2. **Execution**  
   - Run `main.py` (the entry point).  
   - The script loads environment variables, initializes dependencies, and runs the assignment logic.  

3. **Output**  
   - Results are printed to the console or stored in designated output files.  

4. **Extendability**  
   - Core logic is modularized inside `src/` so that new features or modules can be added without breaking the workflow.  

---

## 🛠️ How to Use & Install

### 1. Clone the Repository
```bash
git clone https://github.com/PrinceKumarIITJ/IBY_assignment.git
cd IBY_assignment
```
### 2. Create a Virtual Environment (recommended)
```bash
python3 -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows
```
### 3. Install Dependencies
``` bash
pip install -r requirements.txt
pip install .
```
### 4. Setup Environment Variables
``` bash
cp .env.example .env
```
### 5. Run the Application
``` bash
python main.py
```

## 💻 Tech Stack Used

### Programming Language: Python (>=3.10)

### Dependency Management:

1. pyproject.toml (PEP 621 standard)

2. uv.lock for pinned dependencies

### Environment Management: .env file using python-dotenv

### Version Control: Git & GitHub

### Additional Libraries: Depends on assignment logic inside src/

## 📂 Project Structure

``` bash
IBY_assignment/
├── .env.example             # Example environment variables
├── .gitignore               # Ignored files for Git
├── main.py                  # Main entry point of the project
├── pyproject.toml           # Dependencies & metadata
├── uv.lock                  # Locked dependency versions
└── src/
    └── latest_ai_development/
        └── ...              # Source files & custom modules
```

## 📊 Demo Output

### Here’s a sample run of the project:

### $ python main.py
### ======================================
  ### IBY Assignment - Execution Start
### ======================================

Loading environment variables...

Initializing modules...

Running core logic...

✅ Process completed successfully!
Results saved to output.txt

## 👨‍💻 Author

### Prince Kumar – B.Tech (AI & Data Science), IIT Jodhpur

### GitHub: https://github.com/PrinceKumarIITJ/IBY_assignment
### Video : https://drive.google.com/file/d/1Cep6y6WfwBzo8DY8ZAPCbEdUMG2AA8XY/view?usp=drive_link

