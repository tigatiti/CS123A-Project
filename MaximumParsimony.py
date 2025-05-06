from ete3 import Tree
import itertools

def generate_trees(nodes):
    if len(nodes) == 1:
        return [Tree(nodes[0] + ";")]
    
    trees = []
    seen_splits = set()
    for i in range(1, len(nodes)):
        for left in itertools.combinations(nodes, i):
            right = tuple(sorted(x for x in nodes if x not in left))
            split = (tuple(sorted(left)), right)
            if split in seen_splits or (right, tuple(sorted(left))) in seen_splits:
                continue
            seen_splits.add(split)
            right = [x for x in nodes if x not in left]
            for lt in generate_trees(list(left)):
                for rt in generate_trees(list(right)):
                    t = Tree()
                    t.add_child(lt.copy())
                    t.add_child(rt.copy())
                    trees.append(t)
    return trees

# Main execution for 5 taxa
taxa = ["A", "B", "C", "D", "E"]
trees = generate_trees(taxa)



newicks = set(t.write(format=9, format_root_node=True) for t in trees)

# Output
print(f"Generated {len(newicks)} unique rooted binary trees for 4 taxa.\n")
for newick in newicks:
    t = Tree(newick, format=1)
    print(t.get_ascii(show_internal=True))