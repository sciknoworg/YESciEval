import pandas as pd
from nltk import sent_tokenize, word_tokenize
from openai import OpenAI
import time
from api_keys import ACADEMICCLOUD_KEY
import random


SPORTS_SENTENCE = "Stephen Curry, LeBron James and Kevin Durant led the Americans to a 98-87 victory against host country France to win gold at the 2024 Paris Olympics on Saturday." # https://www.cbssports.com/olympics/news/usa-basketball-wins-gold-medal-stephen-curry-lebron-james-hold-off-france-at-2024-paris-olympics/live/
BLOG_SENTENCE = "Creativity and thought are seemingly non-deterministic. Machines and by extension artificial intelligence, deterministic. The two worlds are orthogonal, parallel lines that may never meet." # https://medium.com/educreation/can-machines-think-b6f8476584e3
TWEET_SENTENCE = "#jets fans must be really confused with #marksanchez performance as a 2nd string QB for phily!! Lmao" # https://github.com/aritter/twitter_nlp/blob/master/data/annotated/wnut16/data/dev
MODELS = ["qwen2.5-72b-instruct", "meta-llama-3.1-70b-instruct", "meta-llama-3.1-8b-instruct", "mistral-large-instruct"] 
CONJUNCTIONS = {"and", "or", "but", "so", "yet", "for", "while", "thereby", "additionally", "furthermore", "moreover", "also", "however", "nevertheless", "although", "whereas", "because", "since", "therefore", "thus", "hence", "consequently", "similarly", "likewise", "in the same way", "just as", "equally", "even though", "though", "nonetheless", "if", "despite that", "unless", "then", "after", "before", "when", "until", "indeed", "certainly", "surely", "despite", "unlike", "during", "regarding", "instead", "accordingly", "albeit", "besides", "thereafter", "meanwhile"}
MULTI_WORD_CONJUNCTIONS = {"in addition", "on the other hand", "as a result", "provided that", "as long as", "only if", "in fact", "above all", "along with", "together with", "as well as", "in contrast to", "contrary to", "in spite of", "because of", "due to", "owing to", "on account of", "thanks to", "on the contrary"}
DEFAULT_DELAY = 30
PUNCT_LEFT = {",", ".", ")", ":", "!", "?", ";"}
PUNCT_RIGHT = {"("}

client = OpenAI(
    api_key = ACADEMICCLOUD_KEY,
    base_url = "https://chat-ai.academiccloud.de/v1"
)

SYSTEM_PROMPT = "You are an assistant specialized in generating redundant sentences. A redundant sentence repeats information unnecessarily, restates ideas in a different way, or includes superfluous words. Your task is to output exactly one redundant sentence based on the input provided."


def adversarial_creation_subtle(filepath):
    # create adversarial examples by making subtle changes
    
    df = pd.read_excel(filepath)
    for index, row in df.iterrows():
        
        print("###################")
        print(f"Processing row {index}...")

        for model in MODELS:
            print(f"Processing model {model}...")

            same_domain_sentence = find_similar_entry(index, df, model)
            sentences = sent_tokenize(row[f"{model}_synthesis"])

            # 1. Relevancy
            df.at[index, f"{model}_subtle_relevancy"] = row[f"{model}_synthesis"] + " " + same_domain_sentence
            
            # 2. Correctness
            df.at[index, f"{model}_subtle_correctness"] = row[f"{model}_synthesis"] + " " + same_domain_sentence

            # 3. Completeness
            if len(sentences) > 1:
                df.at[index, f"{model}_subtle_completeness"] = " ".join(sentences[:-1])
            else:
                df.at[index, f"{model}_subtle_completeness"] = row[f"{model}_synthesis"]

            # 4. Informativeness
            df.at[index, f"{model}_subtle_informativeness"] = row[f"{model}_synthesis"] + " " + same_domain_sentence

            # 5. Integration
            new_synth = remove_conjunctions(sentences, all=False)
            df.at[index, f"{model}_subtle_integration"] = " ".join(new_synth)
                
            # 6. Cohesion
            if len(sentences) > 1:            
                df.at[index, f"{model}_subtle_cohesion"] = " ".join(sentences[:-2] + [sentences[-1]] + [sentences[-2]])
            else:
                df.at[index, f"{model}_subtle_cohesion"] = row[f"{model}_synthesis"]

            # 7. Coherence
            df.at[index, f"{model}_subtle_coherence"] = row[f"{model}_synthesis"] + " " + same_domain_sentence

            # 8. Readability
            df.at[index, f"{model}_subtle_readability"] = row[f"{model}_synthesis"] + " " + BLOG_SENTENCE

            # 9. Conciseness
            redundant_sentence = redundant_creation(sentences[-1], model)
            if redundant_sentence:
                df.at[index, f"{model}_subtle_conciseness"] = row[f"{model}_synthesis"] + " " + redundant_sentence
            else:
                df.at[index, f"{model}_subtle_conciseness"] = "-redundant error-"
            
            df.to_excel(f"{filepath}_subtle.xlsx", index=False)

        time.sleep(DEFAULT_DELAY)


def adversarial_creation_extreme(filepath):
    # create adversarial examples by making extreme changes

    df = pd.read_excel(filepath)
    for index, row in df.iterrows():

        print("###################")
        print(f"Processing row {index}...")

        for model in MODELS:
            print(f"Processing model {model}...")
            sentences = sent_tokenize(row[f"{model}_synthesis"])

            # 1. Relevancy
            df.at[index, f"{model}_extreme_relevancy"] = row[f"{model}_synthesis"] + " " + SPORTS_SENTENCE
            
            # 2. Correctness
            df.at[index, f"{model}_extreme_correctness"] = row[f"{model}_synthesis"] + " " + SPORTS_SENTENCE

            # 3. Completeness
            if len(sentences) > 1:
                df.at[index, f"{model}_extreme_completeness"] = " ".join(sentences[:-1]) + " " + SPORTS_SENTENCE
            else:
                df.at[index, f"{model}_extreme_completeness"] = row[f"{model}_synthesis"] + " " + SPORTS_SENTENCE

            # 4. Informativeness
            df.at[index, f"{model}_extreme_informativeness"] = row[f"{model}_synthesis"] + " " + SPORTS_SENTENCE

            # 5. Integration 
            new_synth = remove_conjunctions(sentences)
            df.at[index, f"{model}_extreme_integration"] = " ".join(new_synth)
                
            # 6. Cohesion
            df.at[index, f"{model}_extreme_cohesion"] = " ".join(random.sample(sentences, len(sentences)))

            # 7. Coherence
            df.at[index, f"{model}_extreme_coherence"] = row[f"{model}_synthesis"] + " " + SPORTS_SENTENCE

            # 8. Readability
            df.at[index, f"{model}_extreme_readability"] = row[f"{model}_synthesis"] + " " + TWEET_SENTENCE

            # 9. Conciseness
            new_sentences = []
            for sent in sentences:
                new_sentences.append(sent)
                redundant_sentence = redundant_creation(sent, model)
                new_sentences.append(redundant_sentence)
            df.at[index, f"{model}_extreme_conciseness"] = " ".join(new_sentences)
            
            df.to_excel(f"{filepath}_extreme.xlsx", index=False)

            time.sleep(DEFAULT_DELAY)


def remove_conjunctions(sentences, all=True):
    new_synth = []
    found = False
    for sent in sentences:
        new_sent = []
        cur_word = ""
        words = word_tokenize(sent)
        i = 0
        n = len(words)
        while i < n:
            while i < n and words[i] in PUNCT_RIGHT:
                cur_word += words[i]
                i += 1

            if i >= n:
                new_sent.append(cur_word)
                break
            
            multi_word_found = False
            if not found or all:
                for mw_conj in MULTI_WORD_CONJUNCTIONS:
                    mw_len = len(mw_conj.split())
                    if i + mw_len <= n and " ".join(words[i:i + mw_len]).lower() == mw_conj:
                        found = True
                        multi_word_found = True
                        i += mw_len
                        break

                if multi_word_found:
                    continue

            if (not found or all) and words[i].lower() in CONJUNCTIONS:
                found = True
            else:
                cur_word += words[i]

            while i + 1 < n and words[i + 1] in PUNCT_LEFT:
                cur_word += words[i + 1]
                i += 1

            if len(cur_word) > 0:
                new_sent.append(cur_word)

            cur_word = ""
            i += 1
        
        new_synth.append(" ".join(new_sent))
    
    return new_synth


def redundant_creation(sentence, model):
    # create redundant sentece
    user_prompt = f"Rewrite the following sentence in a redundant way by unnecessarily repeating information, restating ideas in a different manner, or including unnecessary words: {sentence}"
    retries = 0
    max_retries = 5
    delay = 120

    while retries < max_retries:
        try:
            chat_completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt}
                ]
            )
            return chat_completion.choices[0].message.content
            
        except Exception as e:
            print(f"Error: {e}. Retrying in {delay} seconds...")
            retries += 1
            time.sleep(delay)
            delay *= 2

    return None


def find_similar_entry(index, df, model):
    # find next entry of same category and return sentence

    # llm4syn
    if "mapped_domain" in df.columns:
        domain = df.at[index, "mapped_domain"]
        cur_question = df.at[index, "research_question"]

        # try to find different question in same domain
        for i in range(index+1, len(df)):
            if df.at[i, "mapped_domain"] == domain and df.at[i, "research_question"] != cur_question:
                sentences = sent_tokenize(df.at[i, f"{model}_synthesis"])
                return sentences[-1]
        for i in range(index):
            if df.at[i, "mapped_domain"] == domain and df.at[i, "research_question"] != cur_question:
                sentences = sent_tokenize(df.at[i, f"{model}_synthesis"])
                return sentences[-1]
        
        # try to find same question in same domain
        for i in range(len(df)):
            if df.at[i, "mapped_domain"] == domain and i != index:
                sentences = sent_tokenize(df.at[i, f"{model}_synthesis"])
                return sentences[-1]
        
        # if no same domain found, return last sentence of first entry
        return sent_tokenize(df.at[0, f"{model}_synthesis"])[-1]
    # BioASQ
    else:
        if index+1 < len(df):
            sentences = sent_tokenize(df.at[index+1, f"{model}_synthesis"])
            return sentences[-1]
        else:
            sentences = sent_tokenize(df.at[0, f"{model}_synthesis"])
            return sentences[-1]


def main():
    
    original_bioasq = "data/BioASQ_dataset_synthesis.xlsx"
    original_llm4syn = "data/llm4syn_dataset_synthesis.xlsx"
    # extreme_bioasq = "data/BioASQ_dataset_adversarial_extreme.xlsx"
    # extreme_llm4syn = "data/llm4syn_dataset_adversarial_extreme.xlsx"
    # subtle_bioasq = "data/BioASQ_dataset_adversarial_subtle.xlsx"
    # subtle_llm4syn = "data/llm4syn_dataset_adversarial_subtle.xlsx"

    adversarial_creation_subtle(original_bioasq)
    adversarial_creation_subtle(original_llm4syn)
    adversarial_creation_extreme(original_bioasq)
    adversarial_creation_extreme(original_llm4syn)
    # adversarial_creation_subtle(subtle_bioasq)
    # adversarial_creation_subtle(subtle_llm4syn)
    # adversarial_creation_extreme(extreme_bioasq)
    # adversarial_creation_extreme(extreme_llm4syn)


def test():
    df = pd.read_excel("data/BioASQ_dataset_synthesis.xlsx")

    for index, row in df.iterrows():
        for model in MODELS:
            if not row[f"{model}_synthesis"].endswith("."):
                print(row[f"{model}_synthesis"])
                print(index)
                print("###################")


if __name__ == "__main__":
    main()

    # test()