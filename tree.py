class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, level=0):
        indent = "  " * level
        print(f"{indent}- {self.data}")
        for child in self.children:
            child.print_tree(level + 1)

    def build_station_tree(self):
        root = TreeNode("Stations")

        # MRT Line 3
        mrt3_stations = TreeNode("MRT Line 3 Stations")

        mrt3_stations.add_child(TreeNode("North Avenue"))
        mrt3_stations.add_child(TreeNode("Quezon Avenue"))
        mrt3_stations.add_child(TreeNode("Kamuning"))
        mrt3_stations.add_child(TreeNode("MRT Cubao"))
        mrt3_stations.add_child(TreeNode("MRT Santolan"))
        mrt3_stations.add_child(TreeNode("Ortigas"))
        mrt3_stations.add_child(TreeNode("Shaw Boulevard"))
        mrt3_stations.add_child(TreeNode("Boni"))
        mrt3_stations.add_child(TreeNode("Guadalupe"))
        mrt3_stations.add_child(TreeNode("Buendia"))
        mrt3_stations.add_child(TreeNode("Ayala"))
        mrt3_stations.add_child(TreeNode("Magallanes"))
        mrt3_stations.add_child(TreeNode("Taft Avenue"))

        # LRT Line 1
        lrt1_stations = TreeNode("LRT Line 1 Stations")

        lrt1_stations.add_child(TreeNode("Baclaran"))
        lrt1_stations.add_child(TreeNode("EDSA"))
        lrt1_stations.add_child(TreeNode("Libertad"))
        lrt1_stations.add_child(TreeNode("Gil Puyat"))
        lrt1_stations.add_child(TreeNode("Vito Cruz"))
        lrt1_stations.add_child(TreeNode("Quirino"))
        lrt1_stations.add_child(TreeNode("Pedro Gil"))
        lrt1_stations.add_child(TreeNode("United Nations"))
        lrt1_stations.add_child(TreeNode("Central Terminal"))
        lrt1_stations.add_child(TreeNode("Carriedo"))
        lrt1_stations.add_child(TreeNode("Doroteo Jose"))
        lrt1_stations.add_child(TreeNode("Bambang"))
        lrt1_stations.add_child(TreeNode("Tayuman"))

        # LRT Line 2
        lrt2_stations = TreeNode("LRT Line 2 Stations")

        lrt2_stations.add_child(TreeNode("Recto"))
        lrt2_stations.add_child(TreeNode("Legarda"))
        lrt2_stations.add_child(TreeNode("Pureza"))
        lrt2_stations.add_child(TreeNode("V. Mapa"))
        lrt2_stations.add_child(TreeNode("J. Ruiz"))
        lrt2_stations.add_child(TreeNode("Gilmore"))
        lrt2_stations.add_child(TreeNode("Betty Go-Belmonte"))
        lrt2_stations.add_child(TreeNode("Araneta Center-Cubao"))
        lrt2_stations.add_child(TreeNode("Anonas"))
        lrt2_stations.add_child(TreeNode("Katipunan"))
        lrt2_stations.add_child(TreeNode("LRT Santolan"))
        lrt2_stations.add_child(TreeNode("Marikina"))
        lrt2_stations.add_child(TreeNode("Antipolo"))

        root.add_child(mrt3_stations)
        root.add_child(lrt1_stations)
        root.add_child(lrt2_stations)

        return root


if __name__ == '__main__':
    root_node = TreeNode("Root")  # Create a root node
    station_tree = root_node.build_station_tree()  # Get the station tree
    station_tree.print_tree()  # Print the entire tree structure