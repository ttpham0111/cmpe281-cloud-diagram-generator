import datetime

from flask.json import JSONEncoder, dumps
from sqlalchemy.ext.declarative import DeclarativeMeta


class Encoder(JSONEncoder):
    def __init__(self, **kwargs):
        super(Encoder, self).__init__(**kwargs)
        self._visited = []

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            if obj in self._visited:
                return None
            self._visited.append(obj)

            d = dict(obj.__dict__)
            del d['_sa_instance_state']
            except_raised = False

            for key, value in d.iteritems():
                try:
                    dumps(value)
                except TypeError:
                    except_raised = True
                    if isinstance(value, datetime.date) or isinstance(value, datetime.datetime):
                        value = str(value)
                    elif isinstance(value.__class__, DeclarativeMeta):
                        self._visited.pop()
                        value = self.default(value)
                    elif hasattr(value, '__iter__'):
                        value = [self.default(val) for val in value]
                    else:
                        value = None
                    d[key] = value

            if not except_raised:
                self._visited.pop()

            return d
        return JSONEncoder.default(self, obj)
