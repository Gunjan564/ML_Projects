import gdown

# Replace these with your actual Google Drive file IDs
file_links = {
    "similarity.zip": "https://drive.google.com/file/d/1Umphlynk-I4_AlJJdgMRebd2clquL0PB/view?usp=drive_link",
    "new_movies.zip": "https://drive.google.com/file/d/1Wcqf_EGRrIOQVj10xIeTxceVrAzeccrR/view?usp=drive_link"
}

filename = "similarity.pkl"
gdown.download(f"https://drive.google.com/uc?id=1Umphlynk-I4_AlJJdgMRebd2clquL0PB", filename, quiet=False)
print("similarity.pkl Downloaded!!")
gdown.download(f"https://drive.google.com/uc?id=1Umphlynk-I4_AlJJdgMRebd2clquL0PB", filename, quiet=False)
print("similarity.pkl Downloaded!!")