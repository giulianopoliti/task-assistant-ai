# AI Operations Executive Challenge – Car Dealership

This repository contains a Python script I created as part of the **AI Operations Executive Challenge**.

The goal of the challenge was to analyze and update two configuration files used for an AI assistant in a car dealership context:

- `flows.json`: defines the logic and flow of the assistant.
- `placeholders.json`: contains values used inside the assistant responses (like assistant name, company info, etc.).

---

## 🛠 Tasks Completed

### ✅ Task 1 – Understand both JSON files
- Analyzed how `flows.json` and `placeholders.json` work together using placeholders.

### ✅ Task 2 – Fix invalid JSON
- Replaced incorrect smart quotes in `flows.json` to make the file valid.

### ✅ Task 3 – Update business hours
- Modified the business hours in `placeholders.json` to include correct Saturday hours.

### ✅ Task 4 – Add new conversation flow
- Added a new flow for users asking about “Administración”.
- The assistant now asks for the full name and transfers if last name is provided.

---

## 🧪 How to Use

Just run the script in a Python environment:

```bash
python update_flows.py
