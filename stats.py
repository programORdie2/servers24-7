import requests
import scratchattach as scratch3
import session as scratch

session = scratch.session
conn = session.connect_cloud("845576700") 
client = scratch3.CloudRequests(conn)

proxy_url = 'https://apis.scratchconnect.eu.org/free-proxy/get?url='

def u_s(un):
    print('userstats of: ' + un)
    stats = ['?', '?', '?', '?', '?', '?']
    s = requests.get('https://scratchdb.lefty.one/v3/user/info/'+un).json()
    try:
        s['username']
    except Exception:
        return 'UserNotFoundError'
    else:
        try:
            #print(s)
            stats[0] = s["statistics"]["followers"]
            stats[2] = s["statistics"]['views']
            stats[3] = s["statistics"]['loves']
            stats[4] = s["statistics"]['favorites']
            stats[5] = s["statistics"]['comments']
        except:
            pass
        print(stats)
        return stats

def t_u(country='global', fil='followers'):
    print('top users: ' + fil)
    stats = []
    rawd = requests.get('https://scratchdb.lefty.one/v3/user/rank/' + country + '/' + fil + '/0')
    print(rawd)
    rawd = rawd.json()
    for n in range(0, 5):
        stats.append(rawd[n]['username'])
        try:
            stats.append(rawd[n]['statistics'][fil])
        except:
            stats.append('???')
    return stats

def t_p(fil='views'):
    print('top projects: ' + fil)
    stats = []
    rawd = requests.get('https://scratchdb.lefty.one/v2/project/rank/' + fil + '/0/')
    rawd = rawd.json()
    #print(rawd)
    for n in range(0, 5):
        stats.append(rawd['projects'][n]['info']['title'])
        stats.append(rawd['projects'][n]['info']['username'])
        stats.append(rawd['projects'][n]['info']['scratch_id'])
    print(stats)
    return stats

def p_s(p_id):
    print('projects stats: ' + p_id)
    stats = []
    rawd = requests.get(proxy_url + 'https://api.scratch.mit.edu/projects/' + p_id)
    rawd = rawd.json()
    try:
        stats.append(rawd['title'])
        stats.append(rawd['author']['username'])
        stats.append(rawd['stats']['views'])
        stats.append(rawd['stats']['loves'])
        stats.append(rawd['stats']['favorites'])
    except:
        return 'Error'
    return stats

def s_p(q):
    print('search project: ' + q)
    stats = []
    rawd = requests.get(proxy_url + 'https://api.scratch.mit.edu/search/projects?q=' + q)
    rawd = rawd.json()
    for n in range(0, 5):
        try:
            stats.append(rawd[n]['title'])
            stats.append(rawd[n]['author']['username'])
            stats.append(rawd[n]['id'])
        except:
            return 'Error'
    return stats

@client.request
def user_stats(usern='programORdie'):
    return u_s(usern)

@client.request
def top_users(c='global', f='followers'):
    return t_u(c, f)

@client.request
def top_projects(f='views'):
    return t_p(f)

@client.request
def project_stats(p_id):
    return p_s(p_id)

@client.request
def search_project(q):
    return s_p(q)

@client.event
def on_ready():
  print('Stats Request Handler Ready')

def start():
    client.run(thread=True)
