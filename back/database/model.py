class Chatroom(object):
    def __init__(self, tag_name, user_ids=[]):
        #self.chatroom_id = chatroom_id
        # self.tag_id = tag_id
        self.tag_name = tag_name
        self.user_ids = user_ids

    def to_dict(self):
        return {'tag_name': self.tag_name, 'user_ids': self.user_ids}
    
    def __repr__(self):
        return (
            f'Chatroom(\
                tag_name={self.tag_name}\
                user_ids={self.user_ids}\
            )'
        )

class User(object):
    def __init__(self, email, name, tags=[]):
        self.email = email
        self.name = name
        self.tags = tags

    def to_dict(self):
        return {'email': self.email, 'name': self.name, 'tags': self.tags}
    
    def __repr__(self):
        return (
            f'User(\
                email={self.email}, \
                name={self.name}, \
                tags={self.tags}\
            )'
        )

class Tag(object):
    def __init__(self, user_id, tag_name):
        self.tag_name = tag_name
        self.user_id = user_id

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'tag_name': self.tag_name
        }

    def __repr__(self):
        return (
            f'Tag(\
                user_id={self.user_id}, \
                tag_name={self.tag_name}\
            )'
        )
