class Graph:
    def __init__(self):
        # Menggunakan dictionary untuk Adjacency List
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            # Hapus semua edge yang terhubung ke vertex ini dari vertex lain
            for v in self.adj_list:
                if vertex in self.adj_list[v]:
                    self.adj_list[v].remove(vertex)
            # Hapus vertex dari dictionary
            del self.adj_list[vertex]
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            # Graf tidak berarah (Undirected Graph)
            if v2 not in self.adj_list[v1]:
                self.adj_list[v1].append(v2)
            if v1 not in self.adj_list[v2]:
                self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        success = False
        if v1 in self.adj_list and v2 in self.adj_list[v1]:
            self.adj_list[v1].remove(v2)
            success = True
        if v2 in self.adj_list and v1 in self.adj_list[v2]:
            self.adj_list[v2].remove(v1)
            success = True
        return success

    def display_matrix(self):
        vertices = list(self.adj_list.keys())
        n = len(vertices)
        if n == 0:
            print("Graf masih kosong.")
            return

        # Buat matriks N x N berisi angka 0
        matrix = [[0] * n for _ in range(n)]
        
        # Mapping nama vertex ke indeks matriks
        v_idx = {v: i for i, v in enumerate(vertices)}
        
        # Isi matriks dengan angka 1 jika ada edge
        for u in self.adj_list:
            for v in self.adj_list[u]:
                matrix[v_idx[u]][v_idx[v]] = 1
                
        # Cetak matriks
        print("\n--- Adjacency Matrix ---")
        print("  ", " ".join(vertices))
        for i, row in enumerate(matrix):
            print(vertices[i], "", " ".join(map(str, row)))

    def dfs(self, start, visited=None):
        if start not in self.adj_list:
            print(f"Vertex '{start}' tidak ditemukan dalam graf.")
            return

        if visited is None:
            visited = set()
            
        visited.add(start)
        print(start, end=" ")
        
        for neighbor in self.adj_list[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        if start not in self.adj_list:
            print(f"Vertex '{start}' tidak ditemukan dalam graf.")
            return
            
        visited = set()
        queue = [start]
        visited.add(start)
        
        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")
            
            for neighbor in self.adj_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()


def main():
    g = Graph()
    
    while True:
        print("\n=== MENU GRAPH ===")
        print("1. Tambah Vertex")
        print("2. Hapus Vertex")
        print("3. Tambah Edge")
        print("4. Hapus Edge")
        print("5. Tampilkan graph (Matrix)")
        print("6. Traversal DFS")
        print("7. Traversal BFS")
        print("8. Quit")
        
        pilihan = input("Pilih menu (1-8): ")
        
        if pilihan == '1':
            v = input("Masukkan nama Vertex: ")
            if g.add_vertex(v):
                print(f"Vertex '{v}' berhasil ditambahkan.")
            else:
                print(f"Vertex '{v}' sudah ada.")
                
        elif pilihan == '2':
            v = input("Masukkan nama Vertex yang akan dihapus: ")
            if g.remove_vertex(v):
                print(f"Vertex '{v}' beserta edge yang terhubung berhasil dihapus.")
            else:
                print(f"Vertex '{v}' tidak ditemukan.")
                
        elif pilihan == '3':
            v1 = input("Masukkan Vertex ke-1: ")
            v2 = input("Masukkan Vertex ke-2: ")
            if g.add_edge(v1, v2):
                print(f"Edge antara '{v1}' dan '{v2}' berhasil ditambahkan.")
            else:
                print("Gagal: Pastikan kedua vertex sudah dibuat sebelumnya.")
                
        elif pilihan == '4':
            v1 = input("Masukkan Vertex ke-1: ")
            v2 = input("Masukkan Vertex ke-2: ")
            if g.remove_edge(v1, v2):
                print(f"Edge antara '{v1}' dan '{v2}' berhasil dihapus.")
            else:
                print("Gagal: Edge tidak ditemukan.")
                
        elif pilihan == '5':
            g.display_matrix()
            
        elif pilihan == '6':
            start = input("Masukkan Vertex awal untuk DFS: ")
            print("Hasil DFS: ", end="")
            g.dfs(start)
            print() # Print baris baru
            
        elif pilihan == '7':
            start = input("Masukkan Vertex awal untuk BFS: ")
            print("Hasil BFS: ", end="")
            g.bfs(start)
            
        elif pilihan == '8':
            print("Terima kasih telah menggunakan program Graph!")
            break
            
        else:
            print("Pilihan tidak valid. Silakan pilih 1-8.")

if __name__ == "__main__":
    main()
