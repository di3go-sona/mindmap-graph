
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
        if target_entity.lower() in [ k.lower() for k in corpus.keys()]:
            print(page, '->', target_entity)
            edges.append((page.lower(), target_entity.lower()))


# %%
from pyvis.network import Network
net = Network("1000px", "1000px", directed=True)


for e in edges:
    for n in e:
        if e not in net.nodes:
            net.add_node(n)
            
    net.add_edge(*e)
net.show('nx.html')
# %%
