class User:
    password = []
    nickname = []
    age = []

    # def __init__(self ,nickname ,password ,age):
    #     self.nickname = nickname
    #     self.password = password
    #     self.age = age


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title


class UrTube:
    users = User.nickname
    videos = []
    current_user = None

    def add(*args):
        ''''Добавление видео'''
        for i in args:
            if i not in UrTube.videos:
                UrTube.videos.append(i)

    def register(nickname, password, age):
        """"Проверка на наличие пользователя, если такого нет то создает нового """
        if nickname in User.nickname:
            print(f"Пользователь {nickname} уже существует")
        else:
            User.nickname.append(nickname)
            User.password.append(hash(password))
            User.age.append(age)
            UrTube.current_user = nickname

    def watch_video(self):
        """Просмотр видео"""
        from time import sleep
        if UrTube.current_user is None:
            return print('Войдите в аккаунт чтобы смотреть видео')
        else:
            for i in UrTube.videos:
                if i.title == self:
                    if i.adult_mode == True and User.age[User.nickname.index(UrTube.current_user)] >= 18:
                        for j in range(1, i.duration + 1):
                            i.time_now = j
                            sleep(1)
                            print(i.time_now, end=' ')
                        print("Конец видео")
                    else:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    if i.adult_mode == False:
                        for j in range(1, i.duration + 1):
                            i.time_now = j
                            sleep(1)
                            print(i.time_now, end=' ')
                        print("Конец видео")
                    i.time_now = 0
                    break

    def log_in(nickname, password):
        """"Вход в акаунт"""
        if nickname in User.nickname:
            if hash(password) == User.password[User.nickname.index(nickname)]:
                UrTube.current_user = nickname
            else:
                print('Пароль не верный')
        else:
            print('Пользователя не существует')

    def get_videos(self):
        """"Поиск видео по фразе"""
        _search_ = []
        for i in UrTube.videos:
            for j in range(len(i.title) - len(self) + 1):
                if i.title[j:j + len(self)].lower() == self.lower():
                    _search_.append(i.title)
                    break
        return _search_

    def log_out(self=True):
        """"Выход из аккаунта"""
        UrTube.current_user = None


ur = UrTube
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
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
