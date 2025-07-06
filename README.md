# Walrus JSON Uploader

A simple Python script to upload a local JSON file to the Walrus decentralized storage network using its public HTTP API.

## Description

This script provides a straightforward way to upload a JSON file to a Walrus publisher. It uses the `requests` library to send an HTTP PUT request as specified in the official [Walrus documentation](https://docs.wal.app/usage/http-api.html). The script handles reading the local file, sending the data to a specified public publisher, and printing the server's response, which includes the Blob ID and Sui Object ID for the uploaded file.

This tool is perfect for developers who need to programmatically store data on Walrus without setting up the full Walrus client CLI.

## Features

-   Upload any JSON file to the Walrus network.
-   Specify the number of storage epochs for the file.
-   Works with any public Walrus publisher on Mainnet or Testnet.
-   Validates that the input file is a valid JSON.
-   Provides direct URLs to access the uploaded file via a public aggregator.

## Prerequisites

-   Python 3.6+
-   The `requests` library

## Installation

1.  **Clone the repository or save the script:**
    Save the Python code provided earlier as a file, for example, `upload_to_walrus.py`.

2.  **Install the required library:**
    Open your terminal or command prompt and install the `requests` library using pip.

    ```bash
    pip install requests
    ```

## Configuration

Before running the script, you need to configure a few variables inside the `if __name__ == '__main__':` block:

1.  **`PUBLISHER`**: The URL of the public Walrus publisher you want to use. The script defaults to a Testnet publisher. You can find a list of public publishers in the [Walrus documentation](https://docs.wal.app/usage/http-api.html#using-a-public-aggregator-or-publisher).

    ```python
    # URL of a public Walrus publisher for the testnet
    PUBLISHER = "https://publisher.walrus-testnet.walrus.space"
    ```

2.  **`JSON_FILE_PATH`**: The path to the local JSON file you want to upload.

    ```python
    # Path to your local JSON file
    JSON_FILE_PATH = "my_data.json"
    ```
    *Note: If this file does not exist, the script will create a dummy `my_data.json` file for demonstration purposes.*

3.  **`STORAGE_EPOCHS`**: (Optional) The number of epochs you want to store the file for.

    ```python
    # Number of epochs to store the file for
    STORAGE_EPOCHS = 5
    ```

## Usage

Once configured, run the script from your terminal:

```bash
python upload_to_walrus.py
```

The script will then:
1.  Check for and (if necessary) create the specified JSON file.
2.  Upload the file to the configured Walrus publisher.
3.  Print the JSON response from the publisher, which contains details about the stored blob.

### Example Output

If the upload is successful, you will see output similar to this:

```
Created a dummy JSON file: my_data.json

Upload successful!
Response from Walrus publisher:
{
    "newlyCreated": {
        "blobObject": {
            "id": "0xe91eee8c5b6f35b9a250cfc29e30f0d9e5463a21fd8d1ddb0fc22d44db4eac50",
            "registeredEpoch": 34,
            "blobId": "M4hsZGQ1oCktdzegB6HnI6Mi28S2nqOPHxK-W7_4BUk",
            "size": 17,
            "encodingType": "RS2",
            "certifiedEpoch": 34,
            "storage": {
                "id": "0x4748cd83217b5ce7aa77e7f1ad6fc5f7f694e26a157381b9391ac65c47815faf",
                "startEpoch": 34,
                "endEpoch": 35,
                "storageSize": 66034000
            },
            "deletable": false
        },
        "resourceOperation": {
            "registerFromScratch": {
                "encodedLength": 66034000,
                "epochsAhead": 1
            }
        },
        "cost": 132300
    }
}

--- Accessing your file ---
Blob ID: M4hsZGQ1oCktdzegB6HnI6Mi28S2nqOPHxK-W7_4BUk
Object ID: 0xe91eee8c5b6f35b9a250cfc29e30f0d9e5463a21fd8d1ddb0fc22d44db4eac50

To view your uploaded JSON file, you can use the following URL with a public aggregator:
https://aggregator.walrus-testnet.walrus.space/v1/blobs/M4hsZGQ1oCktdzegB6HnI6Mi28S2nqOPHxK-W7_4BUk

Alternatively, you can access it by its object ID:
https://aggregator.walrus-testnet.walrus.space/v1/blobs/by-object-id/0xe91eee8c5b6f35b9a250cfc29e30f0d9e5463a21fd8d1ddb0fc22d44db4eac50
```

## Accessing the Uploaded File

After uploading, you can view your file's content through any public Walrus **aggregator**. The script provides direct links using both the `blobId` and the `objectId` returned in the successful response. Simply copy and paste one of these URLs into your browser.

## A Note on Walrus Sites

This script uploads a file to the Walrus storage layer. This is the first step in making data available on the decentralized web.

However, to create a user-facing **Walrus Site** (e.g., `https://my-site.wal.app`), you need to use the dedicated **`walrus-sites` builder tool**. That tool handles the process of uploading all of your site's assets (HTML, CSS, JS, images, data files) and linking them to a SuiNS name for easy access through a Walrus Sites portal like `https://wal.app`.

For more information, please refer to the [Introduction to Walrus Sites](https://docs.wal.app/walrus-sites/intro.html) documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.