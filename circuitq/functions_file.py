
import networkx as nx
import copy
import sys

def visualize_circuit_general(graph, save_as):
    """
    Visualises a circuit by creating a figure to an arbitrary path.

    Parameters
    ----------
    graph : NetworkX Graph
        Input circuit
    save_as : String
        Arbitrary figure path
    """
    circuit_func = copy.deepcopy(graph)
    for e in circuit_func.edges.data():
        e[2]['label'] = e[2]['element']
    circuit_vis = nx.nx_agraph.to_agraph(circuit_func)
    circuit_vis.node_attr['width'] = 0.25
    circuit_vis.node_attr['height'] = 0.25
    circuit_vis.node_attr['fixedsize'] = True
    circuit_vis.edge_attr['fontpath'] = '/usr/share/fonts/dejavu'
    circuit_vis.edge_attr['fontname'] = 'DejaVuSans'
    circuit_vis.node_attr['fontpath'] = '/usr/share/fonts/dejavu'
    circuit_vis.node_attr['fontname'] = 'DejaVuSans'
    circuit_vis.draw(save_as + '.png', prog='dot')


