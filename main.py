
# %%
import wikipedia




# %%
user_entities = [
    "Artificial intelligence",
    "Cryptography",
    "Cybersecurity",
    "Linux",
    "C (Programming Language)",
    "Machine Learning",
    "Python",
    "Mathematics",
    "Statistics",
    "Programming Language"
    
    ]

corpus = {}
for e in user_entities:
    
    
    page_names = wikipedia.search(e)
    for page_name in page_names:
        try:
            page = wikipedia.page(page_name)
            print(f"###{page}")
            corpus[page_name.title()] = page.links
            break
        except Exception as error:  
            pass
corpus
# %%
edges = []
for page, entities in corpus.items():
    print(f"### {page}")
    for target_entity in entities:
        if target_entity.lower() in [ k.lower() for k in corpus.keys()] or True:
            print(page, '->', target_entity)
            edges.append((page.lower(), target_entity.lower()))


# %%
from pyvis.network import Network
import networkx

nx = networkx.Graph()



for e in edges:
    nx.add_edge(*e)

to_remove = [n for n in nx if len(nx[n]) < 4]
nx.remove_nodes_from(to_remove)
for n in nx:
    nx.nodes[n]['mass'] = len(nx[n]) * 5
    nx.nodes[n]['size'] = len(nx[n]) * 5

net = Network("1000px", "1000px")
net.from_nx(nx)
net.show('nx.html')


# %%
