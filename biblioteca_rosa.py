import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def devolver(self):
        self.disponivel = True


class Emprestimo:
    def __init__(self):
        self.livros = []
        self.data_emprestimo = datetime.now()
        self.data_devolucao = None

    def adicionar_livro(self, livro):
        if livro.emprestar():
            self.livros.append(livro)
            return True
        return False

    def devolver_livro(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn and not livro.disponivel:
                livro.devolver()
                if all(l.disponivel for l in self.livros):
                    self.data_devolucao = datetime.now()
                return True
        return False


class Membro:
    def __init__(self, nome, id_membro):
        self.nome = nome
        self.id = id_membro
        self.emprestimos = []

    def registrar_emprestimo(self, livro):
        emprestimo = None
        for e in self.emprestimos:
            if e.data_devolucao is None:
                emprestimo = e
                break
        if not emprestimo:
            emprestimo = Emprestimo()
            self.emprestimos.append(emprestimo)
        return emprestimo.adicionar_livro(livro)

    def devolver_livro_por_isbn(self, isbn):
        for emprestimo in self.emprestimos:
            if emprestimo.data_devolucao is None:
                if emprestimo.devolver_livro(isbn):
                    return True
        return False


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.membros = []

    def cadastrar_livro(self, livro):
        self.livros.append(livro)

    def cadastrar_membro(self, membro):
        self.membros.append(membro)

    def buscar_livro(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                return livro
        return None

    def buscar_membro(self, id_membro):
        for membro in self.membros:
            if membro.id == id_membro:
                return membro
        return None


class BibliotecaApp:
    def __init__(self, root):
        self.biblioteca = Biblioteca()
        self.root = root
        self.root.title("Sistema de Biblioteca")

        # Define a cor de fundo rosa bebê da janela principal
        self.root.configure(bg="#FADADD")  # Rosa bebê

        # Cabeçalho rosa
        header = tk.Label(root, text="Biblioteca da Sophia", font=("Arial", 24, "bold"), bg="#ff69b4", fg="white",
                          pady=10)
        header.pack(fill=tk.X)

        frame = tk.Frame(root, bg="#FADADD")
        frame.pack(pady=10)

        self.btn_style = {
            "bg": "#ff69b4",
            "fg": "white",
            "activebackground": "#ff1493",
            "activeforeground": "white",
            "bd": 0,
            "font": ("Arial", 10, "bold"),
            "width": 16,
            "height": 2,
            "cursor": "hand2"
        }

        tk.Button(frame, text="Cadastrar Livro", command=self.cadastrar_livro, **self.btn_style).grid(row=0, column=0,
                                                                                                      padx=5, pady=5)
        tk.Button(frame, text="Cadastrar Membro", command=self.cadastrar_membro, **self.btn_style).grid(row=0, column=1,
                                                                                                        padx=5, pady=5)
        tk.Button(frame, text="Fazer Empréstimo", command=self.fazer_emprestimo, **self.btn_style).grid(row=1, column=0,
                                                                                                        padx=5, pady=5)
        tk.Button(frame, text="Fazer Devolução", command=self.fazer_devolucao, **self.btn_style).grid(row=1, column=1,
                                                                                                      padx=5, pady=5)
        tk.Button(frame, text="Listar Empréstimos", command=self.listar_emprestimos, **self.btn_style).grid(row=2,
                                                                                                            column=0,
                                                                                                            columnspan=2,
                                                                                                            pady=10)

    # (Aqui continuam os métodos da classe BibliotecaApp iguais ao código anterior...)

    def cadastrar_livro(self):
        win = tk.Toplevel(self.root)
        win.title("Cadastrar Livro")
        win.configure(bg="#FADADD")

        tk.Label(win, text="Título:", bg="#FADADD").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        tk.Label(win, text="Autor:", bg="#FADADD").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        tk.Label(win, text="ISBN:", bg="#FADADD").grid(row=2, column=0, sticky="e", padx=5, pady=5)

        titulo = tk.Entry(win)
        autor = tk.Entry(win)
        isbn = tk.Entry(win)

        titulo.grid(row=0, column=1, padx=5, pady=5)
        autor.grid(row=1, column=1, padx=5, pady=5)
        isbn.grid(row=2, column=1, padx=5, pady=5)

        def salvar():
            livro = Livro(titulo.get(), autor.get(), isbn.get())
            self.biblioteca.cadastrar_livro(livro)
            messagebox.showinfo("Sucesso", "Livro cadastrado com sucesso!")
            win.destroy()

        tk.Button(win, text="Salvar", command=salvar, **self.btn_style).grid(row=3, column=0, columnspan=2, pady=10)

    def cadastrar_membro(self):
        win = tk.Toplevel(self.root)
        win.title("Cadastrar Membro")
        win.configure(bg="#FADADD")

        tk.Label(win, text="Nome:", bg="#FADADD").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        tk.Label(win, text="ID:", bg="#FADADD").grid(row=1, column=0, sticky="e", padx=5, pady=5)

        nome = tk.Entry(win)
        id_membro = tk.Entry(win)

        nome.grid(row=0, column=1, padx=5, pady=5)
        id_membro.grid(row=1, column=1, padx=5, pady=5)

        def salvar():
            membro = Membro(nome.get(), id_membro.get())
            self.biblioteca.cadastrar_membro(membro)
            messagebox.showinfo("Sucesso", "Membro cadastrado com sucesso!")
            win.destroy()

        tk.Button(win, text="Salvar", command=salvar, **self.btn_style).grid(row=2, column=0, columnspan=2, pady=10)

    def fazer_emprestimo(self):
        win = tk.Toplevel(self.root)
        win.title("Fazer Empréstimo")
        win.configure(bg="#FADADD")

        tk.Label(win, text="ID do Membro:", bg="#FADADD").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        tk.Label(win, text="ISBN do Livro:", bg="#FADADD").grid(row=1, column=0, sticky="e", padx=5, pady=5)

        id_membro = tk.Entry(win)
        isbn = tk.Entry(win)

        id_membro.grid(row=0, column=1, padx=5, pady=5)
        isbn.grid(row=1, column=1, padx=5, pady=5)

        def emprestar():
            membro = self.biblioteca.buscar_membro(id_membro.get())
            livro = self.biblioteca.buscar_livro(isbn.get())

            if not membro:
                messagebox.showerror("Erro", "Membro não encontrado!")
                return
            if not livro:
                messagebox.showerror("Erro", "Livro não encontrado!")
                return

            if membro.registrar_emprestimo(livro):
                messagebox.showinfo("Sucesso", "Empréstimo realizado com sucesso!")
            else:
                messagebox.showerror("Erro", "Livro indisponível!")

            win.destroy()

        tk.Button(win, text="Emprestar", command=emprestar, **self.btn_style).grid(row=2, column=0, columnspan=2,
                                                                                   pady=10)

    def fazer_devolucao(self):
        win = tk.Toplevel(self.root)
        win.title("Fazer Devolução de Livro")
        win.configure(bg="#FADADD")

        tk.Label(win, text="ID do Membro:", bg="#FADADD").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        tk.Label(win, text="ISBN do Livro:", bg="#FADADD").grid(row=1, column=0, sticky="e", padx=5, pady=5)

        id_membro = tk.Entry(win)
        isbn_livro = tk.Entry(win)

        id_membro.grid(row=0, column=1, padx=5, pady=5)
        isbn_livro.grid(row=1, column=1, padx=5, pady=5)

        def devolver():
            membro = self.biblioteca.buscar_membro(id_membro.get())
            if not membro:
                messagebox.showerror("Erro", "Membro não encontrado!")
                return

            if membro.devolver_livro_por_isbn(isbn_livro.get()):
                messagebox.showinfo("Sucesso", "Livro devolvido com sucesso!")
            else:
                messagebox.showerror("Erro", "Livro não encontrado em empréstimos em aberto!")

            win.destroy()

        tk.Button(win, text="Devolver", command=devolver, **self.btn_style).grid(row=2, column=0, columnspan=2, pady=10)

    def listar_emprestimos(self):
        win = tk.Toplevel(self.root)
        win.title("Lista de Empréstimos")
        win.configure(bg="#FADADD")

        text = tk.Text(win, width=60, height=20)
        text.pack(padx=10, pady=10)

        for membro in self.biblioteca.membros:
            text.insert(tk.END, f"Membro: {membro.nome} (ID: {membro.id})\n")
            for e in membro.emprestimos:
                status = "Em aberto" if e.data_devolucao is None else f"Devolvido em {e.data_devolucao.strftime('%d/%m/%Y %H:%M')}"
                livros_titulos = [f"{livro.titulo} ({'Disponível' if livro.disponivel else 'Emprestado'})" for livro in
                                  e.livros]
                text.insert(tk.END, f"  - Livros: {livros_titulos}\n  - Status: {status}\n")
            text.insert(tk.END, "\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()
