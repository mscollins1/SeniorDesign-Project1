from bs4 import BeautifulSoup
import urllib.request
from urllib.error import URLError, HTTPError

def print_job_details(jobs):
    jobTitle = jobs.string

    print(jobTitle)
    print_languages(jobs)
    print_description(jobs)
    print_link(jobs)
    print_date_published(jobs)
    print('\n')


def print_languages(jobs):
    for languages in jobs.parent.find_all('category'):
        print(languages.string, end=', ')
    print('', end='\n')

def print_description(jobs):
    for jobBlock in jobs.parent.find_all('description'):
        soup = BeautifulSoup(jobBlock.string, 'html.parser')
        text = soup.get_text()
        for i in range(0, 150, 1):
            print(text[i], end='')
    print('...', end='\n')

def print_link(jobs):
    for link in jobs.parent.find_all('link'):
        print(link.next_sibling)
def print_date_published(jobs):
    for date in jobs.parent.find_all('pubdate'):
        print(date.string)

def get_website_response(url):
    try:
        response = urllib.request.urlopen(url).read()
        return response
    except HTTPError as e:
        print('Error code: ', e.code)
        return ''
    except URLError as e:
        print('not a good url: ', e.reason)
        return ''

def check_user_exit(userInput):
    return userInput == 'e'


def main():
    url = "https://stackoverflow.com/jobs/feed?l=Bridgewater%2c+MA%2c+USA&u=Miles&d=50"
    soup = BeautifulSoup(get_website_response(url), 'html.parser')
    #the title tag is where all the job names are located
    titles = soup.find_all('title')
    #gotta skip the first iteration since it has a lot of garbage, which is why i have a condition in the loop
    firstLoop = False;
    count = 0
    userInput = ''
    for jobs in titles:
        if firstLoop:
            if(count%10==9):#only displays some jobs, can get more by pressing any key
                try: #this try/except is just for the pytest since it fails when it collects input()
                    userInput = input('press any key to continue posting or press e to exit')
                except:
                    userInput = 'e'
            if check_user_exit(userInput):
                break
            print_job_details(jobs)
            count= count+1

        else:
            firstLoop=True


main()

