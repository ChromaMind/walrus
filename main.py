import requests
import json
import os

def upload_json_to_walrus(file_path: str, publisher_url: str, epochs: int = 1):
    """
    Uploads a JSON file to a Walrus publisher.

    Args:
        file_path (str): The path to the local JSON file.
        publisher_url (str): The URL of the Walrus publisher.
        epochs (int, optional): The number of storage epochs. Defaults to 1.

    Returns:
        dict: The JSON response from the Walrus publisher, or None if an error occurs.
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return None

    # Read the content of the JSON file
    with open(file_path, 'r') as f:
        try:
            # Validate if the file is a valid JSON
            json_data = json.load(f)
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON file at {file_path}")
            return None

    # The API expects the raw file content in the body
    with open(file_path, 'rb') as f:
        file_content = f.read()

    # Construct the full URL with parameters
    url = f"{publisher_url}/v1/blobs"
    params = {
        'epochs': epochs
    }

    headers = {
        'Content-Type': 'application/json'
    }

    try:
        response = requests.put(url, params=params, data=file_content, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        # Return the JSON response
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == '__main__':
    # --- Configuration ---
    # URL of a public Walrus publisher for the testnet
    # You can find more publishers in the provided documentation
    PUBLISHER = "https://publisher.walrus-testnet.walrus.space"

    # Path to your local JSON file
    JSON_FILE_PATH = "my_data.json"

    # Number of epochs to store the file for
    STORAGE_EPOCHS = 5

    # --- Create a dummy JSON file for testing ---
    if not os.path.exists(JSON_FILE_PATH):
        dummy_data = {"name": "My Walrus Data", "version": 1}
        with open(JSON_FILE_PATH, 'w') as f:
            json.dump(dummy_data, f, indent=4)
        print(f"Created a dummy JSON file: {JSON_FILE_PATH}")

    # --- Upload the file ---
    upload_response = upload_json_to_walrus(JSON_FILE_PATH, PUBLISHER, STORAGE_EPOCHS)

    # --- Process the response ---
    if upload_response:
        print("\nUpload successful!")
        print("Response from Walrus publisher:")
        print(json.dumps(upload_response, indent=4))

        # --- Accessing your file on Walrus Sites ---
        if 'newlyCreated' in upload_response:
            blob_id = upload_response['newlyCreated']['blobObject']['blobId']
            object_id = upload_response['newlyCreated']['blobObject']['id']
            print("\n--- Accessing your file ---")
            print(f"Blob ID: {blob_id}")
            print(f"Object ID: {object_id}")

            # You can use a public aggregator to view your file
            aggregator_url = "https://aggregator.walrus-testnet.walrus.space/v1/blobs"
            print(f"\nTo view your uploaded JSON file, you can use the following URL with a public aggregator:")
            print(f"{aggregator_url}/{blob_id}")
            print(f"\nAlternatively, you can access it by its object ID:")
            print(f"{aggregator_url}/by-object-id/{object_id}")

        elif 'alreadyCertified' in upload_response:
            blob_id = upload_response['alreadyCertified']['blobId']
            print(f"\nThis blob was already certified with Blob ID: {blob_id}")