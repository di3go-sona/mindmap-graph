
#%%
import wikipedia
import networkx
import math
import click
from pyvis.network import Network

@click.command()
@click.option('--input_path', default='data/topics.txt', help='The path from where topics list (one per row) should be sourced')
@click.option('--output_path', default='data/topics.html', help='The path where to write the output')
def cli(input_path, output_path):


    with open(input_path, 'r') as fin:
        user_entities = fin.readlines()
        user_entities = [u.strip() for u in user_entities]


    corpus = {}
    for e in user_entities:
        page_names = wikipedia.search(e)
        for page_name in page_names:
            try:
                page = wikipedia.page(page_name)
                print(f"Searching '{e}' on wikipedia, matched '{page_name.title()}'")
                corpus[page_name.title()] = page.links
                break
            except Exception as error:  
                print(f"No result founds for keyword '{e}'")


    edges = []
    for page, entities in corpus.items():
        print(f"Downloading page '{page}' from wikipedia")
        for target_entity in entities:
            if target_entity.lower() in [ k.lower() for k in corpus.keys()] or True:
                # print(page, '->', target_entity)
                edges.append((page.lower(), target_entity.lower()))

    nx = networkx.Graph()
    for e in edges:
        nx.add_edge(*e)

    to_remove = [n for n in nx if len(nx[n]) < 4]
    nx.remove_nodes_from(to_remove)
    for n in nx:
        nx.nodes[n]['mass'] = math.sqrt(len(nx[n]))
        nx.nodes[n]['size'] = math.sqrt(len(nx[n]))

    net = Network("1000px", "1000px")
    net.from_nx(nx)
    net.show_buttons()
    net.show(output_path)


cli()



# %%
