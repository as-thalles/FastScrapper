# FastScrapper
Project with the intent of learning FastAPI, as well as some web scraping.

The project is divided in 2 steps: the building of the dataset and the creation of the service.
To create the dataset you can run the `collect_events.py` file and wait for a bit. Those will be saved in json format in the file named `events.json`.
After that you can run the service that is implemented in the `main.py` file using the comand `uvicorn main:app --reload`.
Hardcoded paths in the files should be adjusted according to your use of the project.
