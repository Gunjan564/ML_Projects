import gdown

file_links = {
    "similarity.pkl": "https://drive.google.com/file/d/1Umphlynk-I4_AlJJdgMRebd2clquL0PB/view?usp=drive_link",
    "new_movies.pkl": "https://drive.google.com/file/d/1Wcqf_EGRrIOQVj10xIeTxceVrAzeccrR/view?usp=drive_link"
}

file_1 = "similarity.pkl"
file_2 = "new_movies.pkl"
gdown.download(f"https://drive.google.com/uc?id=1Umphlynk-I4_AlJJdgMRebd2clquL0PB", file_1, quiet=False)
print("similarity.pkl Downloaded!!")
gdown.download(f"https://drive.google.com/uc?id=1Wcqf_EGRrIOQVj10xIeTxceVrAzeccrR", file_2, quiet=False)
print("new_movies.pkl Dowloaded!!")