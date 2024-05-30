import requests
from bs4 import BeautifulSoup


def get_films(g: str) -> list:
    film_list = []
    url = f'https://www.film.ru/online/movies/{g}/new'
    try:
        page = requests.get(url)
        page.raise_for_status()
    except requests.RequestException as error:
        logger.error(f"Ошибка при запросе URL: {error}")
        return film_list

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="list_content")
    if results is None:
        logger.info("No results found in the page")
        return film_list

    for job in results.find_all("div", class_="redesign_afisha_movie_main"):
        redesign_afisha_movie = job.find("a", class_="redesign_afisha_movie_main_title")
        if redesign_afisha_movie is None:
            continue

        name = redesign_afisha_movie.find("strong").text
        subtitle_div = job.find("div", class_="redesign_afisha_movie_main_subtitle")
        subtitle_parts = subtitle_div.text.split()
        year = next((part for part in subtitle_parts if part.isdigit()), None)
        info_div = job.find("div", class_="redesign_afisha_movie_main_info")
        info_parts = info_div.text.split('/')
        genre = info_parts[0].strip()
        country = info_parts[1].strip()
        film = {
            'name': name,
            'year': year,
            'genre': genre,
            'country': country,
            'href': "https://www.film.ru" + redesign_afisha_movie['href'],
        }
        film_list.append(film)
        print(film)
    return film_list
