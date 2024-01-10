# Qimia AI OpenAI Python SDK Demo

## Introduction

This project is designed to demonstrate the compatibility of OpenAI's services with the Qimia AI API. It enables users to interact with OpenAI's API through a custom endpoint provided by Qimia AI.

## Purpose

This demo showcases how OpenAI's functionalities can be integrated with Qimia AI's services. It's an ideal tool for developers looking to leverage OpenAI's capabilities alongside Qimia AI's unique API and authentication system. It also enables Qimiers to use Qimia AI programmatically.

## Getting Started

### Prerequisites
- Python 3.11 or higher.
- Poetry package manager.

### Installation

#### Using Poetry
1. Clone the repository.
2. Navigate to the project directory.
3. Run `poetry install` to install dependencies.

#### Using pip
Ensure you have `poetry-core` installed, then run `pip install .` in the project directory.

## Obtaining a Qimia AI API Key

To use this demo, you'll need a Qimia AI API key. Follow these steps to obtain one:

1. **Register an Account:**
   - Visit [Qimia AI Registration](https://chat.qimiaai.com).
   - Complete the registration form.
   - Verify your email address by following the instructions sent to your email.

2. **Wait for Account Activation:**
   - After email verification, your account will need to be activated by a Qimia AI administrator.
   - This process might take some time, so please be patient.

3. **Retrieve Your API Key:**
   - Once your account is activated, log in to your account.
   - Navigate to the profile page to find API key section.
   - Generate your API Key with "New API Key" buttom top right.

## Configuration

Configure the API endpoint and API key in `oai_client.py`:

```python
API_URL = "https://api.qimiaai.com"
API_KEY = "your_api_key_here"  # Replace with your Qimia AI API Key
```

## Key-Values

1. **use_cache:**
Use embedded cache (RocksDB) of llama-server for chat. Enabled by default.
2. **session:**
Session (Chat) identifier in UUID. It will try to access the cache when provided, along with if use_cache provided by default value
