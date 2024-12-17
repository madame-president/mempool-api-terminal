# Mempool API Terminal: wallet statement generator for in-depth reports on your address current holdings and previous transactions, including price at time of transaction.

### Key features
- **Seamless download and code base under 150 lines:** optimized for simplicity and minimal maintenance.

- **Built-in functions to fetch the data:** retreive historical transactions using Mempool API server.

- **Transformation of request response into a data frame:** manageable and easier for reporting purposes.

- **Intelligent automation and organized Bitcoin data:** well-organized and actionable insights automatically exported to Excel.

---

### Installing the application

#### Setting Up Your Environment  
Ensure you have the following installed:  
- [Python](https://www.python.org/downloads/)  
- [Git](https://git-scm.com/downloads)  
- [GitHub CLI](https://cli.github.com/)  

#### Verifying Installation  
Run these commands to confirm the installed versions:  
```bash
python --version
git --version
gh --version
```

#### Clone the repository

- Code > Github CLI > copy the command:

```bash
gh repo clone madame-president/mempool-api-terminal
```
- Go to the directory:

```bash
cd mempool-api-terminal
```

- Install dependencies:

```bash
pip install -r requirements.txt
```

- Run the program:

```bash
python run.py
```

