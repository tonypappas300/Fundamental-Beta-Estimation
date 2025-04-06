import pandas as pd
import re
from PyPDF2 import PdfReader

def count_words_in_pdf(pdf_path: str, words: list[str]) -> pd.DataFrame:
    """
    Searches a PDF file for a list of words (case-insensitive) and returns a DataFrame
    with the total count of each word found in the entire document.

    Args:
        pdf_path: The path to the PDF file.
        words: A list of words to search for.

    Returns:
        A pandas DataFrame with one row and columns for each word in the
        `words` list, containing the total count of that word in the PDF.
        Returns an empty DataFrame if the PDF cannot be read.
    """
    word_counts = {word.lower(): 0 for word in words}  # Initialize counts (lowercase for case-insensitive)

    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                if text:
                    for word in words:
                        count = len(re.findall(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE))
                        word_counts[word.lower()] += count

        return pd.DataFrame([word_counts])

    except FileNotFoundError:
        print(f"Error: PDF file not found at '{pdf_path}'")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error reading PDF file '{pdf_path}': {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    pdf_file = 'aapl2024.pdf'  # Replace with the actual path to your PDF
    search_words = ["accrual", "accruals", "accrue", "accrued", "accrues", "accruing", "acquire", "acquired", "acquiree", "acquirer", "acquirers", "acquires", "acquiring", "acquisition", "acquisitions", "affiliate", "affiliated", "affiliates", "affiliation", "affiliations", "alliance", "alliances", "bankrupt", "bankruptcies", "bankruptcy", "carryback", "carryforward", "collaborate", "collaborations", "collaboration", "collaborative", "collaborators", "collateral", "collateralization", "collateralize", "collateralized", "complex", "complexities", "complexity", "contingencies", "contingency", "contingent", "contingently", "contract", "contracted", "contracting", "contracts", "contractual", "contractually", "conversion", "conversions", "convertible", "copyright", "copyrights", "counterparties", "counterparty", "covenant", "covenants", "derivative", "derivatives", "embedded", "entities", "exercisability", "exercisable", "exercised", "floating", "foreign", "franchise", "franchises", "futures", "global", "globally", "hedge", "hedged", "hedges", "hedging", "infringe", "infringed", "infridgement", "infringes", "infringing", "insolvency", "insolvent", "intangible", "intangibles", "interconnection", "international", "internationally", "lawsuit", "lawsuits", "lease", "leaseback", "lease", "leasehold", "leases", "leasing", "lessee", "lessees", "lessor", "lessors", "license", "licensed", "licensee", "licensees", "licenses", "licensing", "licensor", "licensors", "lien", "liens", "liquidate", "liquidated", "liquidating", "liquidation", "liquidations", "liquidator", "litigation", "merge", "merged", "merger", "mergers", "merging", "nationalization", "outsource", "outsourced", "outsourcing", "partner", "partnering", "partners", "partnerships", "partnership", "patent", "patentable", "patented", "patents", "reacquired", "recapitalization", "recapitalizations", "reclassification", "reclassifications", "reclassified", "reclassify", "reissued", "reorganization", "reorganizations", "reorganized", "repatriate", "repatriated", "repatriation", "restructure", "restructured", "restructuring", "restructurings", "revaluation", "revalued", "revocable", "revocation", "revoke", "revoked", "royalties", "royalty", "securitizations", "securitization", "securitized", "segment", "segmented", "segments", "sovereign", "subcontract", "subcontractor", "subcontractors", "subcontracts", "sublease", "subleased", "subleases", "sublet", "sublicense", "subsidiaries", "subsidiary", "subsidies", "subsidy", "swap", "swaps", "takeover", "takeovers", "trademark", "trademarks", "unexercisable", "unexercised", "unrecognized", "unremittted", "venture", "ventures", "warranty", "warranties", "worldwide"]

    word_count_df = count_words_in_pdf(pdf_file, search_words)
    print(word_count_df)
