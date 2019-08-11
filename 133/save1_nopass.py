def generate_affiliation_link(url):
    parts = url.split(r'/')
    return f'http://www.amazon.com/dp/{parts[4]}/?tag=pyb0f-20'
