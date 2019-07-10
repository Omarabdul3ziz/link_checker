#Summary
This code search a full directory for HTML files and extract the valid URLs existed in the file, then make get request to check if the URL exist.

#Tutorial
every function has type for its parameter and a return with result.
 - get_html_files() > take a directory and return the HTML files existed.
 - find_links() > take a HTML files and return all the URLs.
 - check_validation() > take all URLs and return only the valid.
 - check_existing() > talk the valid links and retuen the result of its 'get request'
