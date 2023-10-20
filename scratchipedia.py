import scratchattach as scratch3
import wikipediaapi as wikipedia
import session as scratch

wiki = wikipedia.Wikipedia('MyProjectName (merlin@example.com)', 'en')

session = scratch.session
conn = session.connect_cloud("852710589") 
client = scratch3.CloudRequests(conn)

def exists_wp(page):
    page_py = wiki.page(page)
    return page_py.exists()

def get_response(message):
    if exists_wp(message) == False:
        return 'PageNotFound'
    pp = wiki.page(message)
    page_data = []
    page_data.append('Title:      ' + pp.title)
    page_data.append('URL:   ' + pp.fullurl)
    page_data.append('Content:                                        ' + pp.text)
    return page_data

@client.request
def chat(arguments):
  print('Wiki request  ' + arguments)
  return get_response(arguments)

@client.event
def on_ready():
  print('Wiki request handler ready')

def start():
  client.run(thread=True)
