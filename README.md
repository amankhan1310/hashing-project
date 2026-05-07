# Large-Scale Data Hashing & Rehashing System

A high-performance Python-based data hashing system developed to securely process and transform massive datasets containing millions of records using SHA-256 hashing with salting techniques.

The project was designed for large-scale secure data processing workflows where sensitive mobile number datasets needed to be anonymized, hashed, and matched efficiently while maintaining scalability and memory optimization.

The system successfully processed and secured over **30 million+ records** using chunk-based batch processing techniques.

---

# Overview

Organizations handling sensitive user information require secure methods for storing and processing customer datasets.

This project implements:

* SHA-256 hashing
* Salting mechanisms
* Large-scale chunk processing
* Secure mobile number transformation
* Memory-efficient data pipelines

The system reads massive Excel datasets in chunks, cleans and normalizes mobile numbers, generates secure SHA-256 hashes, and exports processed results into structured CSV outputs.

The architecture was optimized to handle extremely large datasets efficiently without exhausting system memory.

---

# Features

* SHA-256 hashing with salting
* Large-scale batch processing
* Chunk-based memory optimization
* Mobile number normalization
* Secure anonymization pipeline
* Multi-sheet Excel handling
* CSV export support
* High-volume record processing
* Scalable data transformation workflows

---

# Tech Stack

## Programming Language

* Python

## Libraries

* Pandas
* Hashlib
* OpenPyXL
* Regular Expressions (re)
* OS module

## Data Processing

* Excel file handling
* CSV generation
* Chunk-based processing
* Data normalization

## Tools

* Visual Studio Code
* Git
* GitHub

---

# System Workflow

1. Load large Excel dataset
2. Read records in chunks
3. Clean and normalize mobile numbers
4. Append country code formatting
5. Apply SHA-256 hashing
6. Generate secure hashed output
7. Export results into CSV files

---

# Core Functionalities

## Data Cleaning & Normalization

* Removes non-numeric characters
* Extracts valid 10-digit mobile numbers
* Standardizes input formatting

## SHA-256 Hashing

* Applies cryptographic SHA-256 hashing
* Supports salting for enhanced security
* Generates irreversible secure hashes

## Chunk-Based Processing

* Processes datasets in batches
* Prevents memory overflow
* Enables scalable handling of massive datasets

## Multi-Sheet Excel Processing

* Reads multiple Excel sheets dynamically
* Processes large enterprise-style datasets efficiently

---

# Technical Highlights

* Processed over **30M+ records**
* Optimized for low memory consumption
* High-speed batch hashing pipeline
* Automated CSV generation
* Secure anonymization workflow

---

# Challenges Solved

* Memory limitations while handling huge datasets
* Large-scale hashing performance optimization
* Data cleaning inconsistencies
* Efficient chunk processing
* Secure handling of sensitive user information

---

# Security Concepts Used

* SHA-256 cryptographic hashing
* Salting mechanisms
* Data anonymization
* Secure data transformation

---

# Applications

* Secure customer data processing
* Data anonymization pipelines
* Enterprise data migration
* Identity protection systems
* Privacy-preserving analytics

---

# Future Enhancements

* Parallel processing optimization
* Distributed hashing pipeline
* Cloud-based processing support
* AES encryption integration
* GPU-accelerated hashing
* Real-time processing APIs

---

# Installation

## Clone Repository

```bash id="y1q7mn"
git clone <repository-url>
cd hashing-system
```

## Install Dependencies

```bash id="4jz8pr"
pip install pandas openpyxl
```

## Run Project

```bash id="7k2xla"
python hashing_pipeline.py
```

---

# Learning Outcomes

This project helped in understanding:

* Large-scale data engineering
* Cryptographic hashing workflows
* Memory-efficient processing
* Batch data pipelines
* Enterprise-scale dataset handling
* Secure data transformation systems

---

# Author

**Aman Yahya Khan**
AI & Machine Learning Engineer
Pune, Maharashtra, India

GitHub: github.com/amankhan1310
