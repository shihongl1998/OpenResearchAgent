# Arxiv Paper Database

This repository manages a database of Arxiv papers, including metadata and embeddings. The database consists of four main files:

1. `arxiv_paper_db.json`: Contains metadata about the papers.
2. `faiss_paper_title_embeddings.bin`: Contains embeddings for paper titles.
3. `faiss_paper_abs_embeddings.bin`: Contains embeddings for paper abstracts.
4. `arxivid_to_index_abs.json`: Maps Arxiv IDs to index positions in the FAISS index.

Credit to the original source of the data: https://github.com/AutoSurveys/AutoSurvey

## File Details

### 1. `arxiv_paper_db.json`

This file stores detailed information about each paper in the database. It includes the following fields for each paper:

- **id**: The Arxiv ID of the paper
- **title**: The title of the paper
- **abs**: The abstract of the paper
- **date**: The publication date of the paper
- **authors**: A list of authors
- **cat**: Categories (subjects) of the paper
- **url**: URL to the PDF of the paper on Arxiv

#### Example:
```json
{
  "cs_paper_info": {
    "1": {
      "id": "1811.06122v1",
      "title": "The case for shifting the Renyi Entropy",
      "url": "http://arxiv.org/pdf/1811.06122v1",
      "date": "2018-11-14",
      "abs": "Abstract text...",
      "cat": "cs.IT",
      "authors": ["Author One", "Author Two"]
    },
    "2": {
      "id": "1811.06115v1",
      "title": "Deep Learning in the Wavelet Domain",
      "url": "http://arxiv.org/pdf/1811.06115v1",
      "date": "2018-11-14",
      "abs": "Abstract text...",
      "cat": "cs.CV",
      "authors": ["Author One", "Author Two"]
    }
    // More papers can be added here...
  }
}
```

### 2. `faiss_paper_title_embeddings.bin`

This binary file contains the embeddings for the titles of the papers. These embeddings are used for similarity search and other machine learning tasks.

### 3. `faiss_paper_abs_embeddings.bin`

This binary file contains the embeddings for the abstracts of the papers. Like the title embeddings, these are used for various machine learning tasks.

### 4. `arxivid_to_index_abs.json`

This file provides a mapping from the Arxiv IDs to the index positions in the FAISS index. This mapping is essential for retrieving the correct embeddings from the FAISS index.

#### Example:
```json
{
  "1811.06122v1": 0,
  "1811.06115v1": 1,
  "1811.06114v2": 2,
  "1811.06110v1": 3,
  "1811.06109v1": 4,
  "1811.06106v3": 5,
  "1811.06541v1": 6,
  "1811.06103v1": 7,
  "1811.06100v1": 8,
  "1811.06846v1": 9,
  "1811.06099v1": 10
  // More mappings can be added here...
}
```