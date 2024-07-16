## Setting up the app
```conda create -p venv python=3.10 -y```

```conda activate ./venv```

```pip install -r requirements.txt```

While running locally, include a .env file with the variable with the gemini api key 
GOOGLE_API_KEY=""

## Running the app

First execute,
```python sql.py```

Then to run locally,
```streamlit run app-local.py```


## Live App link

[Live App](https://shreyasbgr-gemini-sql-extractor-app-p4aafr.streamlit.app/)
