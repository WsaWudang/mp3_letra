from youtube_search import YoutubeSearch
from pytube import YouTube


def pesquisar_musica_youtube(nome_musica):
    # Pesquisar a música no YouTube
    results = YoutubeSearch(nome_musica, max_results=1).to_dict()
    if results:
        video_id = results[0]['id']
        video_title = results[0]['title']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        return video_title, video_url
    else:
        return None, None


def baixar_musica(url):
    try:
        video = YouTube(url)
        titulo = video.title
        print(f'Baixando: {titulo}')
        stream = video.streams.filter(only_audio=True).first()
        stream.download()
        print('Download concluído!')
    except Exception as e:
        print(f"Ocorreu um erro durante o download: {str(e)}")


# Programa principal
musica = input("Digite o nome da música: ")

# Pesquisar a música no YouTube
titulo_musica, url_musica = pesquisar_musica_youtube(musica)

if titulo_musica:
    print(f"Música encontrada no YouTube: {titulo_musica}")
    print(f"URL do vídeo: {url_musica}")
    baixar_musica(url_musica)
else:
    print("Nenhuma música encontrada no YouTube.")