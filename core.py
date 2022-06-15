class File:
    def __init__(self, path: str, name: str, cid: str) -> None:
        self.path = path
        self.name = name
        self.cid = cid


class Attachment:
    def __init__(self, image: list, audio: list, archive: list, videos: list, document: list, other: list) -> None:
        self.image = image
        self.audio = audio
        self.archive = archive
        self.videos = videos
        self.document = document
        self.other = other


class Time:
    def __init__(self, hour: int, minute: int) -> None:
        self.hour = hour
        self.minute = minute


class Date:
    def __init__(self, year: int, month: int, day: int) -> None:
        self.year = year
        self.month = month
        self.day = day


class User:
    def __init__(self, id, name, family, username, position) -> None:
        self.id = id
        self.name = name
        self.family = family
        self.username = username
        self.position = position


class Taken:
    def __init__(self, is_taken, user: User, date: Date, time: Time) -> None:
        self.is_taken = is_taken
        self.user = user
        self.date = date
        self.time = time


class Done:
    def __init__(self, is_finished: bool, user: User, date: Date, time: Time) -> None:
        self.is_finished = is_finished
        self.user = user
        self.date = date
        self.time = time


class Created:
    def __int__(self, date, time) -> None:
        self.date = date
        self.time = time


class Deadline:
    def __init__(self, date, time):
        self.date = date
        self.time = time


class Mention:
    def __init__(self, of: User, to: User, date: Date, time: Time) -> None:
        self.of = of
        self.to = to
        self.date = date
        self.time = time


class Task:
    def __init__(self, id: int, name: str, description: str, priority: int, mentions: list, taken: Taken, created: Created, deadline: Deadline, done: Done, attachment: Attachment) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.priority = priority
        self.priority = priority
        self.mentions = mentions
        self.taken = taken
        self.created = created
        self.deadline = deadline
        self.done = done
        self.attachment = attachment
