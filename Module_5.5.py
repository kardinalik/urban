import time

"""
Каждый объект класса User должен обладать следующими атрибутами и методами:
Атрибуты: nickname(имя пользователя, строка), password(в хэшированном
виде, число), age(возраст, число)
"""


class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f'{self.nickname}'

    def __hash__(self):
        return hash(self.password)

    def __int__(self):
        return f'{self.age}'


"""
Каждый объект класса Video должен обладать следующими атрибутами и методами:
Атрибуты: title(заголовок, строка), duration(продолжительность,
секунды), time_now(секунда остановки (изначально 0)),
adult_mode(ограничение по возрасту, bool (False по умолчанию))
"""


class Video:
    def __init__(self, title: str, duration: int, adult_mode=bool(False)):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return f'{self.title}'

    def __int__(self):
        return f'{self.duration}'


"""
Каждый объект класса UrTube должен обладать следующими атрибутами и
методами:
Атрибуты: users(список объектов User), videos(список объектов Video),
current_user
(текущий пользователь User)
"""


class UrTube:
    def __init__(self):
        self.users = []         # (список объектов User)
        self.videos = []        # (список объектов Video)
        self.current_user = None     # (текущий пользователь)

# Метод log_in, который принимает на вход аргументы: nickname, password
# и пытается найти пользователя в users с такими же логином и паролем.
# Если такой пользователь существует, то current_user меняется на
# найденного. Помните, что password передаётся в виде строки, а
# сравнивается по хэшу.

    def log_in(self, nickname, password):
        for User.nickname in self.users:
            if User.nickname == nickname and User.password == password:
                self.current_user = User
                return
            else:
                print('Неверный пароль')

# Метод register, который принимает три аргумента: nickname, password,
# age, и добавляет пользователя в список, если пользователя не существует
# (с таким же nickname). Если существует, выводит на экран: "Пользователь
# {nickname} уже существует". После регистрации, вход выполняется
# автоматически.

    def register(self, nickname: str, password: int, age: int):
        password = hash(password)
        for user in self.users:
            if nickname == user.nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
#       print(f'Вы успешно зарегистрированы под именем {nickname}. Вход в аккаунт осуществлён!')

# Метод log_out для сброса текущего пользователя на None.
    def log_out(self):
        self.current_user = None

# Метод add, который принимает неограниченное кол-во объектов класса
# Video и все добавляет в videos, если с таким же названием видео ещё не
# существует. В противном случае ничего не происходит.
    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

# Метод get_videos, который принимает поисковое слово и возвращает
# список названий всех видео, содержащих поисковое слово. Следует учесть,
# что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать
# регистр).

    def get_videos(self, search_word):
        search_list = []
        for video in self.videos:
            if search_word.lower() in video.title.lower():
                search_list.append(video)
        return search_list

# # Метод watch_video, который принимает название фильма, если не находит
# точного совпадения(вплоть до пробела), то ничего не воспроизводится,
# если же находит - ведётся отчёт в консоль на какой секунде ведётся
# просмотр. После текущее время просмотра данного видео сбрасывается.

    def watch_video(self, film: str):
        if self.current_user:
            for video in self.videos:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу!")
                    return
                if film in video.title:
                    for i in range(1,11):
                        print(i, end=" ")
                        time.sleep(1)
                        video.time_now += 1
                    video.time_now = 0
                    print('Конец видео')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.log_in('vasya_pupkin', 'lolkekcheburek')
# ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')