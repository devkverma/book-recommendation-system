# Book Recommendation System

## Overview

The Book Recommendation System is a Python-based project that provides book recommendations based on user-selected titles. It utilizes a dataset of books from Goodreads and applies Natural Language Processing (NLP) techniques to analyze book descriptions, genres, authors, and publishers to suggest similar titles.

## Features

- **Data Cleaning**: The system processes the dataset to handle missing values, clean genres, and format descriptions.
- **Tag Generation**: Combines information from book descriptions, genres, authors, and publishers to create a unique set of tags for each book.
- **Cosine Similarity**: Utilizes cosine similarity to find books that are similar based on their tags.
- **Recommendation Functionality**: Allows users to input a book title and receive a list of recommended books.

## Dataset

The dataset used for this project is `goodreads_top100_from1980to2023_final.csv`, which contains information about the top 100 books from Goodreads, including:

- **Title**
- **Authors**
- **Publisher**
- **Description**
- **Genres**

## Installation

To run this project, ensure you have Python installed (preferably Python 3.6 or later). You will also need the following libraries:

- `numpy`
- `pandas`
- `nltk`
- `scikit-learn`

You can install these packages using pip:

```bash
pip install numpy pandas nltk scikit-learn
