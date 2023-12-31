
def make_celery(celery, app):
    celery.conf.update(app.config)

    # tu sa rieši aplikačný kontext.
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery
