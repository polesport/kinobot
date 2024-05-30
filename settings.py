
class Genre:
    animation = 'animation'
    comedy = 'comedy'
    horror = 'horror'
    fantasy = 'fantasy'
    crime = 'crime'
    action = 'action'
    history = 'history'
    anime = 'anime'
    mystery = 'mystery'
    adventure = 'adventure'

    @staticmethod
    def get_dir():
        return {Genre.comedy: 'комедия', Genre.horror: 'ужасы',
                Genre.fantasy: 'фэнтези', Genre.crime: 'детектив',
                Genre.action: 'боевик', Genre.history: 'исторический',
                Genre.animation:'мультфильмы', Genre.anime:'аниме', Genre.mystery: 'мистика',
                Genre.adventure:'приключения'}
