class Attachment:
    def __init__(self, image: list, audio: list, archive: list, videos: list, document: list, other: list) -> None:
        self.image = image
        self.audio = audio
        self.archive = archive
        self.videos = videos
        self.document = document
        self.other = other


class Time:
    def __init__(self, hour, minute) -> None:
        self.hour = hour
        self.minute = minute


class Date:
    def __init__(self, year, month, day) -> None:
        self.year = year
        self.month = month
        self.day = day


class Done:
    def __init__(self, is_finished, user) -> None:
        self.is_finished = is_finished
        self.user = user


class Taken:
    def __init__(self, is_taken, user) -> None:
        self.is_taken = is_taken
        self.user = user


class User:
    def __init__(self, id, name, family, username, position) -> None:
        self.id = id
        self.name = name
        self.family = family
        self.username = username
        self.position = position


class Task:
    def __init__(self, id, name, description, priority, mentions, taken, created, deadline, done, attachment) -> None:
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
