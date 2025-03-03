import os
import subprocess
import datetime

def update_progress_file():
    repo_path = "~/Desktop/workspace - Deborah/freecodecamp-log"  # Substitua pelo caminho do seu repositório local
    file_path = os.path.expanduser(f"{repo_path}/freecodecamp-progress.md")
    
    progress_text = f"### FreeCodeCamp Progress - {datetime.date.today()}\n"
    progress_text += "\n- Curso: JavaScript Algorithms and Data Structures"
    progress_text += "\n- Desafios Concluídos: [X]"
    progress_text += "\n- Última Conquista: [Título do Desafio]"
    progress_text += "\n- Tempo de Estudo: [X horas]"
    progress_text += "\n\n---\n"
    
    with open(file_path, "a") as file:
        file.write(progress_text)

def git_commit_and_push():
    repo_path = os.path.expanduser("~/Desktop/workspace - Deborah/freecodecamp-log")  # Caminho do repositório
    
    subprocess.run(["git", "-C", repo_path, "add", "freecodecamp-progress.md"], check=True)
    subprocess.run(["git", "-C", repo_path, "commit", "-m", "Atualização diária do progresso no FreeCodeCamp"], check=True)
    subprocess.run(["git", "-C", repo_path, "push"], check=True)
    
if __name__ == "__main__":
    update_progress_file()
    git_commit_and_push()
    print("Progresso atualizado e enviado para o GitHub!")
