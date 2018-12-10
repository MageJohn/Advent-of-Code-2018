import graphviz
import solution2


def render_trie(dot, trie, cur_str=''):
    if trie is None:
        return
    for k in trie:
        dot.node(cur_str + k, k)
        dot.edge(cur_str, cur_str + k)
        render_trie(dot, trie[k], cur_str + k)


dot = graphviz.Digraph()
dot.node('')
render_trie(dot, solution2.trie)
dot.render("solution2_render.gv")
