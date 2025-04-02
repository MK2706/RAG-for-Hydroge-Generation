import PyPDF2
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load the pre-trained model and tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained("1MK26/hydro_bart_GEN")
tokenizer = AutoTokenizer.from_pretrained("1MK26/hydro_bart_GEN")

def summarize(input_text=None, pdf_file=None):
    # Check if either input_text or pdf_file is provided
    if input_text is None and pdf_file is None:
        return "Please provide either text input or a PDF file."

    # If input_text is provided, use it
    if input_text:
        input_data = input_text
    else:
        # If pdf_file is provided, attempt to read the PDF
        try:
            with open(pdf_file, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                num_pages = len(pdf_reader.pages)
                input_data = ''

                # Extract text from each page
                for page_num in range(num_pages):
                    page = pdf_reader.pages[page_num]
                    text = page.extract_text()
                    if text:  # Ensure that text is not None
                        input_data += text
        except Exception as e:
            print(f"Error reading file: {e}")
            return "Error reading the file."

    # Tokenize the input data for the model
    inputs = tokenizer(input_data, return_tensors="pt", truncation=True, max_length=1024)

    # Generate the summary
    summary_ids = model.generate(
        **inputs,
        max_length=150,
        num_beams=4,
        early_stopping=True if model.config.early_stopping is None else model.config.early_stopping  # Ensure it's a boolean
    )

    # Decode the generated summary and return it
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary
