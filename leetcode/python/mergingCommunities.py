class UnionFind:
    def __init__(self, size: int):
        # This keeps track of the parent of each node
        self.parent = [i for i in range(size)]
        # This keeps track of the size of each community
        self.size = [1] * size

    # This method joins two communities
    def union(self, x: int, y: int) -> None:
        # We find the rep of the two communities
        rep_x, rep_y = self.find(x), self.find(y)
        # If the reps are the same, no joining is required as the communities are already joined
        if rep_x != rep_y:
            # We join the smallest one to the biggest one because it's this require less actions
            if self.size[rep_x] > self.size[rep_y]:
                self.parent[rep_y] = rep_x
                self.size[rep_x] += self.size[rep_y]
            else:
                self.parent[rep_x] = rep_y
                self.size[rep_y] += self.size[rep_x]

    # This method finds the rep of a community based on one of its nodes
    def find(self, x: int) -> int:
        # This checks if the parent of the node x is itself, if it is, it means that the node is the rep of the community and we return it
        if x == self.parent[x]:
            return x

        # Otherwise we do recursion and path compression
        # This makes sure that all the nodes in the same community have only one parent, its rep
        self.parent[x] = self.find(self.parent[x])

        # Then we return the rep
        return self.parent[x]

    # This method gets the size of the community by one of its nodes
    def get_size(self, x: int) -> int:
        return self.size[self.find(x)]


class MergingCommunities:
    def __init__(self, n: int) -> None:
        self.uf = UnionFind(n)

    def connect(self, x: int, y: int) -> None:
        self.uf.union(x, y)

    def get_community_size(self, x: int) -> int:
        return self.uf.get_size(x)


"""
Time complexity of Union Find functions:
- With path compression and union by size optimizations, find has a time complexity of amortized O(1) because the branches of the graph become very short over time, making the function effectively constant-time in most cases
- Since union just uses the find function twice, it also has a time complexity of amortized O(1)
- Since get_size just uses the find function once, it also has a time complexity of amortized O(1)
Therefore the time complexities of connect and get_community_size are both amortized O(1)
The time complexity of the contructuor is O(n) because we initialize two arrays of size n when creating the UnionFind object

Space complexity is O(n) because the Union-Find data structure has two arrays of size n: parent and size.
The space taken up by the recursive all stack is amortized O(1) since the branches of the graph become very short over time, resulting in fewer recursive calls made to the find function
"""
