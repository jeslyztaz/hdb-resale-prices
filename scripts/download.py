import requests
import json

def download_workflow():
    collectionId = 189
    collection_url = f'https://api-production.data.gov.sg/v2/public/api/collections/{collectionId}/metadata?withDatasetMetadata=false'
    collections = requests.get(collection_url).json()

    datasets = collections['data']['collectionMetadata']['childDatasets']
    # Loop through each dataset ID
    for datasetId in datasets:
        # Get the download link
        initiate_dl = requests.get(
            f"https://api-open.data.gov.sg/v1/public/api/datasets/{datasetId}/poll-download",
            headers={"Content-Type": "application/json"},
            json={}
        )
        data = initiate_dl.json()
        download_url = data['data']['url'] 
        
        file_response = requests.get(download_url)
        if file_response.status_code == 200:
            filename = f"data/raw/{datasetId}.csv"  
            with open(filename, 'wb') as file:
                file.write(file_response.content)
            print(f"Downloaded {filename}")
        else:
            print(f"Failed to download {filename}: {file_response.status_code}")

if __name__ == "__main__":
    download_workflow()

