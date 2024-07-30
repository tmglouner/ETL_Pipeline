import os
from flask import Flask, request, render_template
from google.cloud import storage

app = Flask(__name__)

# Set up environment variables for sensitive information
service_account_path = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = service_account_path

# Configure the GCS bucket name and project ID
GCS_BUCKET_NAME = 'sales-pipeline-data'
PROJECT_ID = 'datapipeline-430721'

# Initialize the Google Cloud Storage client
storage_client = storage.Client(project=PROJECT_ID)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            try:
                bucket = storage_client.bucket(GCS_BUCKET_NAME)
                blob = bucket.blob(file.filename)
                blob.upload_from_file(file)
                return f'File {file.filename} uploaded to {GCS_BUCKET_NAME}.'
            except Exception as e:
                return f'An error occurred: {str(e)}'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)