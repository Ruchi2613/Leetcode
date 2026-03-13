# site connectivity checker


import requests


class check_connectivity:
    def __init__(self, urls):
        self.site_url = urls
        self.result = {}

    def check_connect(self):

        try:
            for url in self.site_url:
                response = requests.get(url, timeout=3)

                if response.status_code == 200:
                    self.result[url] = 'Success'
                else:
                    self.result[url] = f'Unreachable (Status code: {response.status_code})'
        except requests.exceptions.RequestException as e:
            self.result[url] = f'Failed (Error: {e})'

    def display_result(self):

        for url, status in self.result.items():
            print(f'{url}: {status}')


if __name__ == "__main__":
    url_to_check = ["https://www.google.com",
                    "https://www.github.com",
                    "https://www.nonexistentwebsite12345.com"]

    check_obj = check_connectivity(url_to_check)
    check_obj.check_connect()
    check_obj.display_result()


# Word Dictionary


class word_dict:

    def __init__(self):
        self.word_dict = {
            'hi': 'a way of greeting',
            'eyes': 'an organ of seeing'
        }
    def check(self):

        while True:
            input_w = input("Enter a word (or type 'exit' to quit): ").strip()

            if input_w.lower() in self.word_dict:
                print(input_w.lower(),":",self.word_dict[input_w.lower()])
            elif input_w.lower() == 'exit':
                break
            else:
                print(f"The word '{input_w}' is not in the dictionary.")


if __name__ == "__main__":
    word_dictionary = word_dict()
    word_dictionary.check()
