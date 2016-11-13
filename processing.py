def permute(lst):
    if not lst:
        return [[]]
    else:
        ret = []
        for i in range(len(lst)):
            ret.extend([[lst[i]] + rst for rst in permute(lst[0:i] + lst[i+1:])])
    return ret

def permute_tree(t):
    if not t.subtrees():
        return [Tree(t.label())]
    elif all([all([not r.subtrees() for r in s.subtrees()]) for s in t.subtrees()]):
        return [Tree(t.label(), t.subtrees())]
    else:
        subperms = permute([permute_tree(s) for s in t.subtrees()])
        subtree_permutations = []
        for subperm in subperms:
            subtree_permutations.extend(permute_lists(subperm))
        return [Tree(t.label(), s) for s in subtree_permutations]

def permute_lists(lst):
    if len(lst) == 1:
        return [[elem] for elem in lst[0]]
    all_perms = []
    for elem in lst[0]:
        all_perms.extend([[elem] + perm for perm in permute_lists(lst[1:])])
    return all_perms

class Tree:
    empty = []

    def __init__(self, label, subtrees=empty):
        #assert subtrees is Tree.empty or all([isinstance(s, Tree) for s in subtrees])
        self.entry = label
        self.children = subtrees

    def label(self):
        return self.entry

    def subtrees(self):
        return self.children

    def leaves(self):
        leaves = []
        for child in self.children:
            if child.subtrees():
                leaves.extend(child.leaves())
            else:
                leaves.append(child.label())
        return leaves

    def flatten(self):
        return Tree(self.label(), self.leaves())

    def __repr__(self):
        return 'Tree({0}, {1})'.format(self.entry, repr(self.children))\
          if self.children is not Tree.empty else 'Tree({0})'.format(self.entry)

    def __str__(self):
        return str(self.leaves())
