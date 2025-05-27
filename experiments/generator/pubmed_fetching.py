import pandas as pd
from metapub import PubMedFetcher
import time
import json
import matplotlib.pyplot as plt
from collections import Counter


def pubmed_fetch():
    # Prompt the user to enter the path to the CSV file
    input_files = ["data/12B1_golden.json", "data/12B2_golden.json", "data/12B3_golden.json", "data/12B4_golden.json"]
    doc_to_abstract = {}
    doc_to_title = {}
    
    # Initialize the PubMedFetcher
    fetch = PubMedFetcher()

    # Define a function to fetch the abstract given a PMID
    def fetch_abstract(pmid):
        try:
            article = fetch.article_by_pmid(str(pmid))
            return (article.abstract, article.title) if article else None
        except Exception as e:
            print(f"Error fetching abstract for PMID {pmid}: {e}")
            return None

    for file in input_files:

        # Load the CSV file into a DataFrame
        df = pd.read_json(file)
        df.columns = df.columns.str.strip()  # Ensure no extra whitespace in headers

        for val in df["questions"]:
            # only consider summary questions
            if val["type"] != "summary":
                continue

            print(f"Processing {val['body']}")
            i = 0
            for doc in val["documents"]:
                
                if doc in doc_to_abstract:
                    continue

                # make sure we don't exceed the rate limit
                if i == 10:
                    i = 0
                    time.sleep(1)
                else:
                    i += 1

                pmid = doc.split("/")[-1]
                if not pmid:
                    pmid = doc.split("/")[-2]

                response = fetch_abstract(pmid)
                if not response:
                    print(f"Error fetching abstract for doc {doc}")
                    continue
                doc_to_abstract[doc] = response[0]
                doc_to_title[doc] = response[1]
                      
            time.sleep(1)
        

        json.dump(doc_to_abstract, open("data/doc_to_abstract.json", "w"))
        json.dump(doc_to_title, open("data/doc_to_title.json", "w"))


def convert_to_xlsx():
    # Convert the JSON file to an Excel file
    doc_to_abstract = json.load(open("data/doc_to_abstract.json", "r"))
    doc_to_title = json.load(open("data/doc_to_title.json", "r"))
    input_files = ["data/12B1_golden.json", "data/12B2_golden.json", "data/12B3_golden.json", "data/12B4_golden.json"]

    new_df = pd.DataFrame(columns=["research_question", "paper_1_title", "paper_1_abstract", "paper_2_title", "paper_2_abstract", "paper_3_title", "paper_3_abstract", "paper_4_title", "paper_4_abstract", "paper_5_title", "paper_5_abstract", "paper_6_title", "paper_6_abstract", "paper_7_title", "paper_7_abstract", "paper_8_title", "paper_8_abstract", "paper_9_title", "paper_9_abstract", "paper_10_title", "paper_10_abstract", "paper_11_title", "paper_11_abstract", "paper_12_title", "paper_12_abstract", "paper_13_title", "paper_13_abstract", "paper_14_title", "paper_14_abstract", "paper_15_title", "paper_15_abstract", "paper_16_title", "paper_16_abstract", "paper_17_title", "paper_17_abstract", "paper_18_title", "paper_18_abstract", "paper_19_title", "paper_19_abstract", "paper_20_title", "paper_20_abstract", "paper_21_title", "paper_21_abstract", "paper_22_title", "paper_22_abstract", "paper_23_title", "paper_23_abstract", "paper_24_title", "paper_24_abstract", "paper_25_title", "paper_25_abstract", "paper_26_title", "paper_26_abstract", "paper_27_title", "paper_27_abstract", "paper_28_title", "paper_28_abstract", "paper_29_title", "paper_29_abstract", "paper_30_title", "paper_30_abstract", "paper_31_title", "paper_31_abstract", "paper_32_title", "paper_32_abstract", "paper_33_title", "paper_33_abstract", "paper_34_title", "paper_34_abstract", "paper_35_title", "paper_35_abstract", "paper_36_title", "paper_36_abstract", "paper_37_title", "paper_37_abstract", "paper_38_title", "paper_38_abstract", "paper_39_title", "paper_39_abstract", "paper_40_title", "paper_40_abstract"])

    for file in input_files:

        df = pd.read_json(file)
        df.columns = df.columns.str.strip()  # Ensure no extra whitespace in headers
        

        for val in df["questions"]:
            if val["type"] != "summary":
                continue
            
            row = [val["body"]] + ([""] * 80)
            print(f"Processing {val['body']}")
            i = 0
            for doc in val["documents"]:
                if i == 40:
                    break
                
                i += 1

                row[(i*2)-1] = doc_to_title[doc]
                row[i*2] = doc_to_abstract[doc]


            new_df.loc[len(new_df)] = row
        
    new_df.to_excel("BioASQ_dataset.xlsx", index=False)
        

def check_max_answer_length():
    max_sentences = 0
    answer_sentences = []
    min_answer_sentences = []

    input_files = ["data/12B1_golden.json", "data/12B2_golden.json", "data/12B3_golden.json", "data/12B4_golden.json"]

    for file in input_files:

        df = pd.read_json(file)
        df.columns = df.columns.str.strip()

        for val in df["questions"]:
            if val["type"] != "summary":
                continue

            answers = val["ideal_answer"]
            min_answer = 300
            for answer in answers:
                answer = answer.split(".")
                answer = [x for x in answer if x]
                answer_sentences.append(len(answer))
                max_sentences = max(max_sentences, len(answer))
                min_answer = min(min_answer, len(answer))
            min_answer_sentences.append(min_answer)

    answer_sentences.sort()
    print(answer_sentences[len(answer_sentences)//2])
    print(sum(answer_sentences)/len(answer_sentences))

    frequency = Counter(answer_sentences)
    numbers = list(frequency.keys())
    counts = list(frequency.values())

    plt.bar(numbers, counts, edgecolor='black')

    for i, count in enumerate(counts):
        plt.text(numbers[i], count + 0.1, str(count), ha='center', fontsize=10)

    plt.xlabel('Sentence Counts')
    plt.ylabel('Frequency')
    plt.title('Frequency of Sentence Counts in Answers')
    plt.show()

    frequency = Counter(min_answer_sentences)
    numbers = list(frequency.keys())
    counts = list(frequency.values())

    plt.bar(numbers, counts, edgecolor='black')

    for i, count in enumerate(counts):
        plt.text(numbers[i], count + 0.1, str(count), ha='center', fontsize=10)

    plt.xlabel('Sentence Counts')
    plt.ylabel('Frequency')
    plt.title('Minimum Frequency of Sentence Counts in Answers')
    plt.show()


def test():
    input_files = ["data/12B1_golden.json", "data/12B2_golden.json", "data/12B3_golden.json", "data/12B4_golden.json"]

    max_docs = 0
    for file in input_files:

        df = pd.read_json(file)
        df.columns = df.columns.str.strip()

        for val in df["questions"]:
            max_docs = max(max_docs, len(val["documents"]))
    
    print(max_docs)


if __name__ == "__main__":
    pubmed_fetch()
    convert_to_xlsx()
    # test()
    # check_max_answer_length()