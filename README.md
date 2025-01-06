# NTLM Hash Extractor

## Overview
This script extracts NTLMv1 and NTLMv2 hashes from a SQLite database. These hashes are commonly used for authentication in Windows environments and can be leveraged for further analysis, auditing, or password cracking during security assessments. The script writes the extracted hashes to separate text files for NTLMv1 and NTLMv2 hashes.

## Features
- Connects to a SQLite database.
- Extracts NTLMv1 and NTLMv2 hashes from the database.
- Filters out system/machine accounts (e.g., those containing `$` in the username).
- Saves extracted hashes to separate text files: `DumpNTLMv1.txt` and `DumpNTLMv2.txt`.
- Provides console output for quick visibility.
- Include a log file (`hash_extractor.log`) for recording the process, ensuring traceability of actions.
- Handle database connection errors.

## Prerequisites
- Python 3.x
- SQLite database file named `Responder.db`.
- Write permissions in the current directory to create output files.

## Usage
1. Place the `Responder.db` file in the same directory as the script.
2. Run the script using the following command:
   ```bash
   python3 HashDumper.py
   ```
3. Check the output files:
   - `DumpNTLMv1.txt` for NTLMv1 hashes.
   - `DumpNTLMv2.txt` for NTLMv2 hashes.
4. Review the `hash_extractor.log` file for process logs.
