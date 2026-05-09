import main as mn

try:
    with open(".env",'r') as f:
        if "API_KEY=" in f:
            mn.main()
except FileNotFoundError:
    API_KEY=input("Please create an API key in openrouter website and provide the API key here:\n")
    with open(".env",'w') as f:
        f.write(f"API_KEY={API_KEY}")
    mn.main()
