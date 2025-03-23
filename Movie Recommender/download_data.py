import gdown

# Replace these with your actual Google Drive file IDs
file_links = {
    "similarity.zip": "https://drive.google.com/uc?id=https://drive.google.com/file/d/1Umphlynk-I4_AlJJdgMRebd2clquL0PB/view?usp=drive_link",
    "new_movies.zip": "https://drive.google.com/uc?id=https://drive.google.com/file/d/1Wcqf_EGRrIOQVj10xIeTxceVrAzeccrR/view?usp=drive_link"
}

# Download each file
for filename, file_id in file_links.items():
    print(f"Downloading {filename}...")
    gdown.download(f"https://drive.google.com/uc?id={file_id}", filename, quiet=False)

print("Download complete!")