import sqlite3
import logging

def setup_logger():
    """Set up the logger to record the process."""
    logging.basicConfig(
        filename="hash_extractor.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info("Logger initialized.")

def dump_hash_to_file(outfile, data):
    """Writes the hashes to a file."""
    try:
        with open(outfile, "w") as dump:
            dump.write(data)
        logging.info(f"Successfully wrote data to {outfile}.")
    except Exception as e:
        logging.error(f"Failed to write data to {outfile}: {e}")

def db_connect():
    """Connects to the SQLite db"""
    try:
        cursor = sqlite3.connect("./Responder.db")
        logging.info("Successfully connected to Responder.db.")
        return cursor
    except sqlite3.Error as e:
        logging.error(f"Database connection failed: {e}")
        raise

def get_responder_hashes(cursor, hash_type):
    """Extracts NTLMv1 or NTLMv2 hashes from the db"""
    query = (
        f"SELECT fullhash FROM Responder WHERE type LIKE '%{hash_type}%' "
        "AND UPPER(user) IN (SELECT DISTINCT UPPER(user) FROM Responder)"
    )
    output = ""
    try:
        res = cursor.execute(query)
        for row in res.fetchall():
            if "$" in row[0]:
                continue
            output += f"{row[0]}\n"
        logging.info(f"Extracted {hash_type.upper()} hashes.")
    except sqlite3.Error as e:
        logging.error(f"Failed to fetch {hash_type.upper()} hashes: {e}")
        raise
    return output

def main():
    setup_logger()
    try:
        cursor = db_connect()

        # Extract and save NTLMv2 hashes
        logging.info("Extracting NTLMv2 hashes...")
        v2_hashes = get_responder_hashes(cursor, "v2")
        dump_hash_to_file("DumpNTLMv2.txt", v2_hashes)
        print("Dumping NTLMv2 hashes:\n", v2_hashes)

        # Extract and save NTLMv1 hashes
        logging.info("Extracting NTLMv1 hashes...")
        v1_hashes = get_responder_hashes(cursor, "v1")
        dump_hash_to_file("DumpNTLMv1.txt", v1_hashes)
        print("\nDumping NTLMv1 hashes:\n", v1_hashes)

    except Exception as e:
        logging.error(f"An error occurred during execution: {e}")
        print("An error occurred. Check the log file for details.")

if __name__ == "__main__":
    main()

#ph1n3y
