import requests
import time


BASE_URL = "http://127.0.0.1:5000"


def baixar_manifesto():
    url = f"{BASE_URL}/manifest.mpd"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        with open("manifest.mpd", "wb") as f:
            f.write(resposta.content)
        print("Manifesto baixado com sucesso!")
    else:
        print("Erro ao baixar manifesto.")
    return resposta


def medir_largura_de_banda():
    url = f"{BASE_URL}/segments/360p_segment.mp4"
    inicio = time.time()
    resposta = requests.get(url)
    fim = time.time()

    tamanho_em_bits = len(resposta.content) * 8
    tempo_segundos = fim - inicio
    largura_banda_mbps = (tamanho_em_bits / tempo_segundos) / 1_000_000

    print(f"Largura de banda medida: {largura_banda_mbps:.2f} Mbps")
    return largura_banda_mbps


def selecionar_qualidade(largura_banda):
    if largura_banda > 5:
        qualidade = "1080p"
    elif largura_banda > 3:
        qualidade = "720p"
    elif largura_banda > 1.5:
        qualidade = "480p"
    else:
        qualidade = "360p"
    print(f"Qualidade selecionada: {qualidade}")
    return qualidade


def baixar_video(qualidade):
    nome_arquivo = f"{qualidade}_segment.mp4"
    url = f"{BASE_URL}/segments/{nome_arquivo}"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        with open(nome_arquivo, "wb") as f:
            f.write(resposta.content)
        print(f"Segmento {qualidade} baixado com sucesso!")
    else:
        print(f"Erro ao baixar segmento {qualidade}.")


if __name__ == "__main__":
    baixar_manifesto()
    largura = medir_largura_de_banda()
    qualidade = selecionar_qualidade(largura)
    baixar_video(qualidade)
