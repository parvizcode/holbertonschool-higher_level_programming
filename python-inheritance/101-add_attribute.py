def add_attribute(obj, name, value):
    """Nesneye yeni bir özellik ekler.

    Args:
        obj: Özellik eklenecek nesne
        name: Özelliğin adı
        value: Özelliğin değeri

    Raises:
        TypeError: Nesneye yeni özellik eklenemezse
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
