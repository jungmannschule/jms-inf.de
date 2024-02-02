from pony.orm import Database, Required, PrimaryKey

db = Database()


class Repository(db.Entity):
    id = PrimaryKey(int, auto=True)
    owner_id = Required(int)
    owner_name = Required(str)
    lower_name = Required(str)
    name = Required(str)
    num_stars = Required(int)
    fork_id = Required(int)
    created_unix = Required(int)
    updated_unix = Required(int)


class Branch(db.Entity):
    id = PrimaryKey(int, auto=True)
    repo_id = Required(int)
    name = Required(str)
    commit_id = Required(str)
    commit_message = Required(str)
    pusher_id = Required(int)


class Issue(db.Entity):
    id = PrimaryKey(int, auto=True)
    poster_id = Required(int)
    repo_id = Required(int)
    is_closed = Required(bool)
