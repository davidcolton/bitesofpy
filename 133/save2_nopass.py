def generate_affiliation_link(url):
    parts = url.split(r'/')
    print (f'http://www.amazon.com/dp/{parts[5]}/?tag=pyb0f-20')