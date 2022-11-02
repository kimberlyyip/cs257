def get_image(search_text):
    from bing_image_downloader import downloader
    downloader.download(search_text, limit=10,  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
