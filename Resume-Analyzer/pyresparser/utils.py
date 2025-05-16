
import spacy
from pdfminer.high_level import extract_text as pdf_extract_text
from spacy.matcher import Matcher
from pdfminer.pdfpage import PDFPage


def get_number_of_pages(file):

    page_count = 0
    with open(file, 'rb') as fh:
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            page_count += 1
    return page_count

def extract_text(file, file_extension):
    
    if file_extension == '.pdf':
        return pdf_extract_text(file)
    elif file_extension == '.docx':
        pass
    else:
        raise ValueError("Unsupported file type")

def extract_entities_wih_custom_model(nlp_model):
    entities = {}
    for ent in nlp_model.ents:
        if ent.label_ == "PERSON":
            entities["Name"] = ent.text
        elif ent.label_ == "EMAIL":
            entities["Email"] = ent.text
        elif ent.label_ == "NUMBER":
            entities["Number"] = ent.text
        elif ent.label_ == "DEGREE":
            entities["Degree"] = ent.text

    return entities

def extract_skills(nlp_model, noun_chunks, skills_file):
    skills = []
    for chunk in noun_chunks:
        if chunk.text in skills_file:
            skills.append(chunk.text)
    
    return skills


def load_skills(skills_file):
    skills_list = []
    with open(skills_file, 'r') as f:
        skills_list = [line.strip() for line in f.readlines()]

def extract_name(nlp_model, matcher):
    patterns = [{'POS': 'PROPN'}, {'POS': 'PROPN'}] 
    matcher.add("NAME", [patterns])
    matches = matcher(nlp_model)
    for match_id, start, end in matches:
        span = nlp_model[start:end]

def extract_email(text):

    email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    match = re.search(email_regex, text)
    return match.group(0) if match else None

def extract_mobile_number(text, custom_regex=None):
    if custom_regex is None:
        custom_regex = r'\+?[0-9]*\s?[0-9]+[-\s]?[0-9]+[-\s]?[0-9]{2,4}'
    match = re.search(custom_regex, text)
    return match.group(0) if match else None

def extract_entity_sections_grad(text):
    sections = {}
    current_section = None
    for line in text.split('\n'):
        line = line.strip()
        if line.isupper():
            current_section = line
            sections[current_section] = []
        elif current_section:
            sections[current_section].append(line)

    for section, content in sections.items():
        sections[section] = ' '.join(content)

    return sections