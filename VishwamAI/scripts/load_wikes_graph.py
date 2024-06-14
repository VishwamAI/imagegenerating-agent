from wikes_toolkit import WikESToolkit, WikESGraph

def load_wikes_graph():
    # Initialize the WikESToolkit
    toolkit = WikESToolkit(save_path="./data")  # save_path is optional

    # Load a sample graph using the toolkit
    G = toolkit.load_graph(
        WikESGraph,
        WikESToolkit.WikES_datasets[3].SMALL,  # Using the SMALL version of the WikiLitArt dataset from the WikES_datasets enumeration
        entity_formatter=lambda e: f"Entity({e.wikidata_label})",
        predicate_formatter=lambda p: f"Predicate({p.label})",
        triple_formatter=lambda t: f"({t.subject_entity.wikidata_label})-[{t.predicate.label}]->({t.object_entity.wikidata_label})"
    )

    # Print basic information about the graph
    print(f"Number of Root Entities: {len(G.root_entities())}")
    print(f"Number of Entities: {len(G.entities())}")

    # Print the first few entities and relations
    print("Sample Entities:")
    for entity in G.entities()[:5]:
        print(entity)

    print("Sample Relations:")
    for relation in G.triples()[:5]:
        print(relation)

if __name__ == "__main__":
    load_wikes_graph()
