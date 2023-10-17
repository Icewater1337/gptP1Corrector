import openai
import os

from corrector import Corrector
from taskParser import load_java_files, extract_text_from_first_pdf

if __name__ == '__main__':
    openai.api_key = os.environ["OPENAI_API_KEY"]
    #corrector.correct("What are 5 vacation destinations for someone who likes to eat pasta?")
    serien_directory = ""
    abgaben_prefix = "\\Abgaben"


    series  = load_java_files(serien_directory+abgaben_prefix)
    extracted_text = extract_text_from_first_pdf(serien_directory)
    task_dict = {"task":extracted_text, "files":[]}
    corrector = Corrector(task_dict)

    for series_name, series_dict in series.items():
        corrector.correct_series(series_dict)




