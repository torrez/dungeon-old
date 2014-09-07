import os

import tornado.web
from handlers import home


class DungeonApplication(tornado.web.Application):

    DEVELOPMENT = 1
    PRODUCTION = 2
    TESTING = 3

    @classmethod
    def get_environment(cls, env_string="development"):
        environments = dict(development=cls.DEVELOPMENT,
                            production=cls.PRODUCTION, testing=cls.TESTING)
        try:
            return environments[env_string]
        except:
            return cls.DEVELOPMENT

    @staticmethod
    def environment_as_string(env):
        environments = ["development", "production", "testing"]
        try:
            return environments[env - 1]
        except:
            return "unknown"

    @classmethod
    def app_settings(cls, environment):
        dirname = os.path.dirname(os.path.abspath(__file__))
        debug = False
        if environment == cls.DEVELOPMENT:
            debug = True
        return {
            "login_url": "/sign-in",  # unecessary
            "static_path": os.path.join(dirname, "static"),
            "template_path":  os.path.join(dirname, "templates"),
            "debug": debug,
            "environment": environment,
        }

    def __init__(self, *args, **settings):
        super(DungeonApplication, self).__init__(*args, **settings)


def make_application(environment=DungeonApplication.DEVELOPMENT):
    app_settings = DungeonApplication.app_settings(environment)

    app = DungeonApplication([
        (r"/", home.IndexHandler),
    ], **app_settings)

    return app
