import requests, re, os

def get_html_files(directory):
    paths = []
    html_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            paths.append(path)
    for path in paths:
        if path.endswith('.html'):
            html_paths.append(path)
    return html_paths

#print (get_html_files('/home/oa/root'))


def find_links(html_paths):
	links = []
	for path in html_paths:
		file = open(path, "r")
		text = file.read()
		regex = r"href=[\'\"]?([^\'\" >]+)"
		founded = re.findall(regex,text)
		links.extend(founded)
	return links

#print(find_links(get_html_files('/home/oa/root')))


def check_validation(links):
    valid_links = []
    for link in links:
        if link.startswith('http'):
            valid_links.append(link)
    return valid_links

#print(check_validation(find_links(get_html_files('/home/oa/root'))))

def check_existing(valid_links):
    print("Getting results ... ")
    for link in valid_links:
        response = requests.get(link)
        status = response.status_code
        if status == 200:
            print('Success')
        else:
            print('Not found')
    return "Checking is Done !"

print(check_existing(check_validation(find_links(get_html_files('/home/oa/Documents')))))
