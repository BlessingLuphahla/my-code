from pytube import YouTube


def download_from_youtube(url, save_path):
    youtube = YouTube(url)
    streams = youtube.streams.filter(file_extension='mp4')
    low_res = streams.get_lowest_resolution()

    low_res.download(output_path=save_path)


url = r''
save_path = r''

download_from_youtube(url, save_path)
